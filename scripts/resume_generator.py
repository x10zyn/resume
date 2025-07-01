#!/usr/bin/env python3
"""
Generates LaTeX and PDF resumes from modular JSON data files using external template files
"""

import argparse
import json
import os
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path


class ResumeGenerator:
    """
    A comprehensive resume generator that loads modular JSON files and generates
    professional LaTeX and PDF outputs using external template files.
    """

    def __init__(self, sections_dir="sections", templates_dir="templates", output_dir="output"):
        self.sections_dir = Path(sections_dir)
        self.templates_dir = Path(templates_dir)
        self.output_dir = Path(output_dir)

        # Ensure output directory exists
        self.output_dir.mkdir(exist_ok=True)

        # Load and combine all modular JSON files
        self.data = self.load_modular_json_data()

    def load_modular_json_data(self):
        """Load all JSON files from sections directory and combine into single data structure"""
        combined_data = {}

        # Define the expected JSON files and their content structure
        json_files = {
            'personal.json': 'personal',
            'summary.json': 'summary',
            'skills.json': 'skills',
            'experience.json': 'experience',
            'projects.json': 'projects',
            'education.json': 'education',
            'achievements.json': 'achievements',
            'learning.json': 'learning',
            'languages.json': 'languages',
            'metadata.json': 'metadata'
        }

        for filename, data_key in json_files.items():
            json_path = self.sections_dir / filename

            if json_path.exists():
                try:
                    with open(json_path, 'r', encoding='utf-8') as f:
                        file_data = json.load(f)
                        combined_data.update(file_data)
                        print(f"✅ Loaded {filename}")
                except Exception as e:
                    print(f"❌ Error loading {filename}: {e}")
            else:
                print(f"⚠️  {filename} not found, skipping...")

        return combined_data

    def clean_phone_for_tel(self, phone):
        """Clean phone number for tel: links"""
        return re.sub(r'[^\d+]', '', phone)
    
    def escape_latex(self, text, preserve_ampersand=False):
        """Escape special LaTeX characters"""
        # Convert markdown bold to LaTeX first
        text = re.sub(r'\*\*(.+?)\*\*', r'\\textbf{\1}', text)
        
        # Basic LaTeX escaping - order matters!
        # Handle backslash first, but preserve already escaped sequences
        text = re.sub(r'\\(?!textbf|&)', r'\\textbackslash{}', text)
        
        latex_special_chars = {
            '%': r'\%',
            '$': r'\$',
            '#': r'\#',
            '^': r'\textasciicircum{}',
            '_': r'\_',
            '{': r'\{',
            '}': r'\}',
            '~': r'\textasciitilde{}',
        }
        
        # Only escape & if not preserving it (for section titles)
        if not preserve_ampersand:
            latex_special_chars['&'] = r'\&'
        
        for char, escape in latex_special_chars.items():
            text = text.replace(char, escape)
        
        return text
    
    def generate_skills_section(self):
        """Generate skills section LaTeX"""
        if 'skills' not in self.data:
            return ""
        
        skills_latex = "\\section{Technical Skills}\n\n"
        
        for skill_group in self.data['skills']:
            category = skill_group['category']
            items = skill_group['items']
            
            # Create a single line with all skills in this category
            skills_text = ", ".join([self.escape_latex(item) for item in items])
            
            skills_latex += f"\\begin{{onecolentry}}\n"
            skills_latex += f"\\textbf{{{self.escape_latex(category)}:}} {skills_text}\n"
            skills_latex += f"\\end{{onecolentry}}\n\n"
            skills_latex += f"\\vspace{{0.2 cm}}\n\n"
        
        return skills_latex
    
    def generate_experience_section(self):
        """Generate experience section LaTeX"""
        if 'experience' not in self.data:
            return ""
        
        experience_latex = "\\section{Experience}\n\n"
        
        for i, exp in enumerate(self.data['experience']):
            if i > 0:
                experience_latex += "\\vspace{0.2 cm}\n\n"
            
            # Format dates
            dates = exp['dates']
            title = self.escape_latex(exp['title'])
            company = self.escape_latex(exp['company'])
            location = self.escape_latex(exp['location'])
            
            # Create header
            experience_latex += f"\\begin{{twocolentry}}{{\n"
            experience_latex += f"{dates}\n"
            experience_latex += f"}}\n"
            experience_latex += f"    \\textbf{{{title}}}, {company}"
            if location and location != "Contract" and location != "Remote" and location != "Part-time":
                experience_latex += f" -- {location}"
            experience_latex += f"\\end{{twocolentry}}\n\n"
            
            # Add description if exists
            if exp.get('description') and exp['description'].strip():
                experience_latex += f"\\vspace{{0.05 cm}}\n"
                experience_latex += f"\\begin{{onecolentry}}\n"
                experience_latex += f"    \\textit{{{self.escape_latex(exp['description'])}}}\n"
                experience_latex += f"\\end{{onecolentry}}\n\n"
            
            # Add highlights
            if exp.get('highlights'):
                experience_latex += f"\\vspace{{0.10 cm}}\n"
                experience_latex += f"\\begin{{onecolentry}}\n"
                experience_latex += f"    \\begin{{highlights}}\n"
                
                for highlight in exp['highlights']:
                    experience_latex += f"        \\item {self.escape_latex(highlight)}\n"
                
                experience_latex += f"    \\end{{highlights}}\n"
                experience_latex += f"\\end{{onecolentry}}\n\n"
        
        return experience_latex
    
    def generate_projects_section(self):
        """Generate projects section LaTeX"""
        if 'projects' not in self.data:
            return ""
        
        projects_latex = "\\section{Projects}\n\n"
        
        for i, project in enumerate(self.data['projects']):
            if i > 0:
                projects_latex += "\\vspace{0.2 cm}\n\n"
            
            name = self.escape_latex(project['name'])
            technologies = self.escape_latex(project['technologies'])
            link = project.get('link', '')
            
            # Create header with link if available
            projects_latex += f"\\begin{{twocolentry}}{{\n"
            if link:
                projects_latex += f"    \\hrefWithoutArrow{{{link}}}{{{link}}}\n"
            else:
                projects_latex += f"    \n"  # Empty if no link
            projects_latex += f"}}\n"
            projects_latex += f"    \\textbf{{{name}}}\\end{{twocolentry}}\n\n"
            
            # Add technologies
            if technologies:
                projects_latex += f"\\vspace{{0.05 cm}}\n"
                projects_latex += f"\\begin{{onecolentry}}\n"
                projects_latex += f"    \\textbf{{Technologies:}} {technologies}\n"
                projects_latex += f"\\end{{onecolentry}}\n\n"
            
            # Add highlights
            if project.get('highlights'):
                projects_latex += f"\\vspace{{0.10 cm}}\n"
                projects_latex += f"\\begin{{onecolentry}}\n"
                projects_latex += f"    \\begin{{highlights}}\n"
                
                for highlight in project['highlights']:
                    projects_latex += f"        \\item {self.escape_latex(highlight)}\n"
                
                projects_latex += f"    \\end{{highlights}}\n"
                projects_latex += f"\\end{{onecolentry}}\n\n"
        
        return projects_latex
    
    def generate_education_section(self):
        """Generate education section LaTeX"""
        if 'education' not in self.data:
            return ""
        
        education_latex = "\\section{Education}\n\n"
        
        for i, edu in enumerate(self.data['education']):
            if i > 0:
                education_latex += "\\vspace{0.2 cm}\n\n"
            
            degree = self.escape_latex(edu['degree'])
            institution = self.escape_latex(edu['institution'])
            dates = edu['dates']
            location = self.escape_latex(edu.get('location', ''))
            note = self.escape_latex(edu.get('note', ''))
            
            # Create header
            education_latex += f"\\begin{{twocolentry}}{{\n"
            education_latex += f"    {dates}\n"
            education_latex += f"}}\n"
            education_latex += f"    \\textbf{{{institution}}}, {degree}"
            if location:
                education_latex += f" -- {location}"
            education_latex += f"\\end{{twocolentry}}\n\n"
            
            # Add note and details
            if note or edu.get('details'):
                education_latex += f"\\vspace{{0.10 cm}}\n"
                education_latex += f"\\begin{{onecolentry}}\n"
                education_latex += f"    \\begin{{highlights}}\n"
                
                if note:
                    education_latex += f"        \\item {note}\n"
                
                for detail in edu.get('details', []):
                    education_latex += f"        \\item {self.escape_latex(detail)}\n"
                
                education_latex += f"    \\end{{highlights}}\n"
                education_latex += f"\\end{{onecolentry}}\n\n"
        
        return education_latex
    
    def generate_achievements_section(self):
        """Generate achievements section LaTeX"""
        if 'achievements' not in self.data or not self.data['achievements'].get('items'):
            return ""
        
        achievements_latex = "\\section{Notable Achievements}\n\n"
        achievements_latex += "\\begin{onecolentry}\n"
        achievements_latex += "    \\begin{highlightsforbulletentries}\n"
        
        for achievement in self.data['achievements']['items']:
            achievements_latex += f"        \\item {self.escape_latex(achievement)}\n"
        
        achievements_latex += "    \\end{highlightsforbulletentries}\n"
        achievements_latex += "\\end{onecolentry}\n\n"
        
        return achievements_latex
    
    def generate_learning_section(self):
        """Generate learning section LaTeX"""
        if 'learning' not in self.data:
            return ""
        
        learning_latex = "\\section{Current Learning \\& Development}\n\n"
        
        # Focus areas
        if self.data['learning'].get('focus_areas'):
            learning_latex += "\\begin{onecolentry}\n"
            learning_latex += "    \\textbf{2025 Focus Areas:}\n"
            learning_latex += "\\end{onecolentry}\n\n"
            learning_latex += "\\begin{onecolentry}\n"
            learning_latex += "    \\begin{highlights}\n"
            
            for area in self.data['learning']['focus_areas']:
                learning_latex += f"        \\item {self.escape_latex(area)}\n"
            
            learning_latex += "    \\end{highlights}\n"
            learning_latex += "\\end{onecolentry}\n\n"
        
        # Continuous learning
        if self.data['learning'].get('continuous_learning'):
            learning_latex += "\\vspace{0.2 cm}\n\n"
            learning_latex += "\\begin{onecolentry}\n"
            learning_latex += "    \\textbf{Continuous Learning:}\n"
            learning_latex += "\\end{onecolentry}\n\n"
            learning_latex += "\\begin{onecolentry}\n"
            learning_latex += "    \\begin{highlights}\n"
            
            for item in self.data['learning']['continuous_learning']:
                learning_latex += f"        \\item {self.escape_latex(item)}\n"
            
            learning_latex += "    \\end{highlights}\n"
            learning_latex += "\\end{onecolentry}\n\n"
        
        return learning_latex
    
    def generate_languages_section(self):
        """Generate languages section LaTeX"""
        if 'languages' not in self.data or not self.data['languages'].get('items'):
            return ""
        
        languages_latex = "\\section{Languages}\n\n"
        
        # Create a single line with all languages
        language_items = []
        for lang_info in self.data['languages']['items']:
            language = self.escape_latex(lang_info['language'])
            proficiency = self.escape_latex(lang_info['proficiency'])
            language_items.append(f"\\textbf{{{language}}}: {proficiency}")
        
        languages_text = ", ".join(language_items)
        
        languages_latex += "\\begin{onecolentry}\n"
        languages_latex += f"    {languages_text}\n"
        languages_latex += "\\end{onecolentry}\n\n"
        
        return languages_latex
    
    def generate_latex_from_template(self, template_name="modern_template.tex"):
        """Generate LaTeX from template file"""
        template_path = self.templates_dir / template_name
        output_path = self.output_dir / "resume.tex"
        
        if not template_path.exists():
            raise FileNotFoundError(f"Template file not found: {template_path}")
        
        # Read template
        with open(template_path, 'r') as f:
            template_content = f.read()
        
        # Extract personal information
        personal = self.data.get('personal', {})
        
        # Prepare replacements
        replacements = {
            'NAME': personal.get('name', 'Your Name'),
            'LOCATION': personal.get('location', 'Your Location'),
            'EMAIL': personal.get('email', 'your.email@example.com'),
            'PHONE': personal.get('phone', '+1 234 567 8900'),
            'PHONE_CLEAN': self.clean_phone_for_tel(personal.get('phone', '+1 234 567 8900')),
            'WEBSITE': personal.get('website', 'yourwebsite.com'),
            'LINKEDIN': personal.get('linkedin', 'linkedin.com/in/yourprofile'),
            'GITHUB': personal.get('github', 'github.com/yourusername'),
            'SUMMARY': self.escape_latex(self.data.get('summary', {}).get('text', 'Your professional summary here')),
            'LAST_UPDATED': self.data.get('metadata', {}).get('last_updated', 'June 2025'),
            'SKILLS_SECTION': self.generate_skills_section(),
            'EXPERIENCE_SECTION': self.generate_experience_section(),
            'PROJECTS_SECTION': self.generate_projects_section(),
            'EDUCATION_SECTION': self.generate_education_section(),
            'ACHIEVEMENTS_SECTION': self.generate_achievements_section(),
            'LEARNING_SECTION': self.generate_learning_section(),
            'LANGUAGES_SECTION': self.generate_languages_section(),
        }
        
        # Replace placeholders
        for key, value in replacements.items():
            placeholder = f"{{{{{{{key}}}}}}}"
            template_content = template_content.replace(placeholder, str(value))
        
        # Write generated LaTeX
        with open(output_path, 'w') as f:
            f.write(template_content)
        
        print(f"✅ Generated LaTeX: {output_path}")
        return output_path
    
    def generate_pdf_from_latex(self, latex_file):
        """Generate PDF from LaTeX file"""
        output_path = self.output_dir / "resume.pdf"
        
        try:
            # Change to output directory for LaTeX compilation
            original_dir = os.getcwd()
            os.chdir(self.output_dir)
            
            # Run pdflatex twice for proper references
            for i in range(2):
                result = subprocess.run([
                    'pdflatex', 
                    '-interaction=nonstopmode', 
                    latex_file.name
                ], capture_output=True, text=True)
                
                if result.returncode != 0:
                    print(f"❌ LaTeX compilation failed on pass {i+1}:")
                    print(result.stderr)
                    return None
            
            # Check if PDF was created (use local path since we're in output dir)
            if Path("resume.pdf").exists():
                print(f"✅ Generated PDF: {output_path}")
                return output_path
            else:
                print("❌ PDF generation failed - file not created")
                return None
                
        except FileNotFoundError:
            print("❌ pdflatex not found. Please install LaTeX distribution.")
            print("Ubuntu/Debian: sudo apt install texlive-latex-base texlive-latex-recommended texlive-latex-extra")
            return None
        except Exception as e:
            print(f"❌ Error generating PDF: {e}")
            return None
        finally:
            os.chdir(original_dir)
    
    def generate_markdown(self):
        """Generate markdown version from JSON data"""
        output_path = self.output_dir / "resume_from_json.md"
        
        markdown_content = []
        
        # Header
        personal = self.data.get('personal', {})
        markdown_content.append(f"# {personal.get('name', 'Your Name')}")
        markdown_content.append("")
        markdown_content.append(f"**{personal.get('title', 'Your Title')}**")
        markdown_content.append("")
        markdown_content.append(f"📧 {personal.get('email', '')} | 📱 {personal.get('phone', '')} | 📍 {personal.get('location', '')}")
        markdown_content.append(f"💻 {personal.get('github', '')} | 🌐 {personal.get('linkedin', '')} | 🌍 {personal.get('website', '')}")
        markdown_content.append("")
        markdown_content.append("---")
        markdown_content.append("")
        
        # Summary
        if 'summary' in self.data:
            markdown_content.append("## 🎯 Professional Summary")
            markdown_content.append("")
            markdown_content.append(self.data['summary']['text'])
            markdown_content.append("")
            markdown_content.append("---")
            markdown_content.append("")
        
        # Skills
        if 'skills' in self.data:
            markdown_content.append("## 💻 Technical Skills")
            markdown_content.append("")
            for skill_group in self.data['skills']:
                markdown_content.append(f"### {skill_group['category']}")
                markdown_content.append("")
                for item in skill_group['items']:
                    markdown_content.append(f"- {item}")
                markdown_content.append("")
            markdown_content.append("---")
            markdown_content.append("")
        
        # Experience
        if 'experience' in self.data:
            markdown_content.append("## 🚀 Professional Experience")
            markdown_content.append("")
            for exp in self.data['experience']:
                markdown_content.append(f"### {exp['title']}")
                markdown_content.append(f"**{exp['company']}** | {exp['dates']} | {exp['location']}")
                if exp.get('description'):
                    markdown_content.append(f"*{exp['description']}*")
                markdown_content.append("")
                for highlight in exp.get('highlights', []):
                    markdown_content.append(f"- {highlight}")
                markdown_content.append("")
            markdown_content.append("---")
            markdown_content.append("")
        
        # Projects
        if 'projects' in self.data:
            markdown_content.append("## 🏗️ Key Projects")
            markdown_content.append("")
            for project in self.data['projects']:
                markdown_content.append(f"### {project['name']}")
                markdown_content.append(f"**Technologies**: {project['technologies']}")
                markdown_content.append("")
                for highlight in project.get('highlights', []):
                    markdown_content.append(f"- {highlight}")
                markdown_content.append("")
            markdown_content.append("---")
            markdown_content.append("")
        
        # Education
        if 'education' in self.data:
            markdown_content.append("## 🎓 Education & Certifications")
            markdown_content.append("")
            for edu in self.data['education']:
                markdown_content.append(f"**{edu['degree']}**")
                markdown_content.append(f"*{edu['institution']}* | {edu['dates']}")
                if edu.get('note'):
                    markdown_content.append(f"**{edu['note']}**")
                markdown_content.append("")
                for detail in edu.get('details', []):
                    markdown_content.append(f"- {detail}")
                markdown_content.append("")
            markdown_content.append("---")
            markdown_content.append("")
        
        # Achievements
        if 'achievements' in self.data:
            markdown_content.append("## 🏆 Notable Achievements")
            markdown_content.append("")
            for achievement in self.data['achievements']['items']:
                markdown_content.append(f"- {achievement}")
            markdown_content.append("")
            markdown_content.append("---")
            markdown_content.append("")
        
        # Learning
        if 'learning' in self.data:
            markdown_content.append("## 🌱 Current Learning & Development")
            markdown_content.append("")
            if self.data['learning'].get('focus_areas'):
                markdown_content.append("**2025 Focus Areas:**")
                for area in self.data['learning']['focus_areas']:
                    markdown_content.append(f"- {area}")
                markdown_content.append("")
            if self.data['learning'].get('continuous_learning'):
                markdown_content.append("**Continuous Learning:**")
                for item in self.data['learning']['continuous_learning']:
                    markdown_content.append(f"- {item}")
                markdown_content.append("")
            markdown_content.append("---")
            markdown_content.append("")
        
        # Languages
        if 'languages' in self.data:
            markdown_content.append("## 🌐 Languages")
            markdown_content.append("")
            for lang_info in self.data['languages']['items']:
                markdown_content.append(f"- **{lang_info['language']}**: {lang_info['proficiency']}")
            markdown_content.append("")
            markdown_content.append("---")
            markdown_content.append("")
        
        # Footer
        last_updated = self.data.get('metadata', {}).get('last_updated', 'June 2025')
        website = personal.get('website', 'yourwebsite.com')
        markdown_content.append(f"*Portfolio: {website} | Last Updated: {last_updated}*")
        
        # Write markdown file
        with open(output_path, 'w') as f:
            f.write('\n'.join(markdown_content))
        
        print(f"✅ Generated Markdown: {output_path}")
        return output_path
    
    def generate_all_formats(self, template_name="modern_template.tex"):
        """Generate all resume formats"""
        print("🚀 Generating resume from JSON data...")
        
        # Generate markdown
        self.generate_markdown()
        
        # Generate LaTeX
        latex_file = self.generate_latex_from_template(template_name)
        
        # Generate PDF from LaTeX
        self.generate_pdf_from_latex(latex_file)
        
        print(f"\n📁 All files generated in: {self.output_dir}")
        print("📄 Available formats:")
        print("   - resume_from_json.md (Markdown from JSON)")
        print("   - resume.tex (LaTeX from template)")
        print("   - resume.pdf (PDF - if LaTeX is installed)")

def main():
    print("🚀 Generating resume from JSON data...")

    parser = argparse.ArgumentParser(description='Generate resume from JSON data using external templates')
    parser.add_argument('--sections-dir', default='sections', help='Directory containing modular JSON files')
    parser.add_argument('--templates-dir', default='templates', help='Directory containing LaTeX template files')
    parser.add_argument('--output-dir', default='output', help='Output directory for generated files')
    parser.add_argument('--latex-only', action='store_true', help='Generate only LaTeX, skip PDF compilation')

    args = parser.parse_args()

    try:
        generator = ResumeGenerator(
            sections_dir=args.sections_dir,
            templates_dir=args.templates_dir,
            output_dir=args.output_dir
        )

        generator.generate_all_formats()

        print("\n🎉 Resume generation complete!")
        print("📁 Generated files:")
        print(f"   - resume_from_json.md (Markdown from JSON)")

        if not args.latex_only:
            print(f"   - resume.pdf (Professional PDF)")
            print(f"   - resume.tex (LaTeX source)")

    except Exception as e:
        print(f"❌ Error during generation: {e}")
        return 1

    return 0

if __name__ == '__main__':
    main() 