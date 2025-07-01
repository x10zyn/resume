# Getting Started with Resume Generator

This guide will help you get up and running with the TOML-based resume generation system.

## Quick Start

### 1. Prerequisites

- **Python 3.7+**: The generator script requires Python 3.7 or higher
- **LaTeX** (optional): For PDF generation
- **Git**: For version control

### 2. Installation

1. **Clone the repository**:
   ```bash
   git clone <your-repo-url>
   cd resume
   ```

2. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Install LaTeX** (for PDF generation):
   ```bash
   # Ubuntu/Debian
   sudo apt install texlive-latex-base texlive-latex-recommended texlive-latex-extra texlive-fonts-recommended

   # macOS
   brew install mactex

   # Windows
   # Download and install MiKTeX from https://miktex.org/
   ```

### 3. Generate Your First Resume

1. **Edit your data**: Modify the TOML files in `sections/`
2. **Generate resume**: Run the generator script
   ```bash
   python3 scripts/resume_generator.py
   ```
3. **Find output**: Check the `output/` directory for generated files

## Understanding the Structure

### Data Files (`sections/`)

Your resume data is stored in TOML format across multiple files:

- `personal.toml` - Contact information
- `summary.toml` - Professional summary
- `skills.toml` - Technical skills
- `experience.toml` - Work experience
- `projects.toml` - Key projects
- `education.toml` - Education & certifications
- `achievements.toml` - Notable achievements
- `learning.toml` - Learning goals
- `languages.toml` - Language proficiencies
- `metadata.toml` - File metadata

### Templates (`templates/`)

LaTeX templates define the visual layout:

- `modern_template.tex` - Default modern template
- Create custom templates for different styles

### Scripts (`scripts/`)

- `resume_generator.py` - Main generation script
- `generate_resume.sh` - Shell wrapper

## Basic Usage

### Generate All Formats
```bash
python3 scripts/resume_generator.py
```

### Generate Specific Format
```bash
# Markdown only
python3 scripts/resume_generator.py --format markdown

# LaTeX only
python3 scripts/resume_generator.py --format latex

# PDF only
python3 scripts/resume_generator.py --format pdf
```

### Use Custom Template
```bash
python3 scripts/resume_generator.py --template my_template.tex
```

## Editing Your Resume

### 1. Personal Information
Edit `sections/personal.toml`:
```toml
[personal]
name = "Your Name"
title = "Your Professional Title"
location = "Your Location"
email = "your.email@example.com"
phone = "+1 234 567 8900"
github = "github.com/yourusername"
linkedin = "linkedin.com/in/yourprofile"
```

### 2. Skills
Edit `sections/skills.toml`:
```toml
[[skills]]
category = "Programming Languages"
items = [
    "**Python** (Expert) - FastAPI, Django, Flask",
    "**JavaScript** (Advanced) - Node.js, React, Vue.js"
]
```

### 3. Experience
Edit `sections/experience.toml`:
```toml
[[experience]]
title = "Software Engineer"
company = "Company Name"
dates = "Jan 2020 - Present"
location = "City, State"
description = "Brief role description"
highlights = [
    "Achievement 1 with specific impact",
    "Achievement 2 with metrics"
]
```

## Job-Specific Resumes

Create tailored versions for specific job applications:

1. **Copy data files**:
   ```bash
   cp -r sections/ jobs/job-name/
   ```

2. **Modify content** for the specific role

3. **Generate job-specific resume**:
   ```bash
   python3 scripts/resume_generator.py --toml-dir jobs/job-name/
   ```

## Troubleshooting

### Common Issues

1. **TOML Syntax Error**:
   - Check for missing quotes or brackets
   - Validate with: `python3 -c "import toml; toml.load('sections/personal.toml')"`

2. **LaTeX Compilation Error**:
   - Ensure LaTeX is properly installed
   - Check template syntax
   - Review LaTeX logs in `output/`

3. **Missing Dependencies**:
   - Install required packages: `pip install -r requirements.txt`
   - Ensure Python 3.7+ is installed

### Getting Help

- Check the main README.md for detailed documentation
- Review the CONTRIBUTING.md for development guidelines
- Create an issue for bugs or questions

## Next Steps

- Explore advanced features in the main README
- Learn about custom templates
- Set up version control for your resume data
- Create job-specific variants

---

Happy resume building! 🚀 