# Resume Generation System - Unified TOML Edition

This directory contains a modern resume management system that allows you to:
- Edit resume data in structured TOML format (easy to write, easy to parse)
- Use external LaTeX templates (no hardcoded templates in scripts)
- Generate professional LaTeX and PDF formats automatically
- Maintain separation between content and presentation
- Version control resume data independently from templates

## 📁 Directory Structure

```
resume/
├── sections/                   # Modular TOML data files
│   ├── personal.toml          # Contact information
│   ├── summary.toml           # Professional summary
│   ├── skills.toml            # Technical skills
│   ├── experience.toml        # Work experience
│   ├── projects.toml          # Key projects
│   ├── education.toml         # Education & certifications
│   ├── achievements.toml      # Notable achievements
│   ├── learning.toml          # Learning goals
│   ├── languages.toml         # Language proficiencies
│   ├── metadata.toml          # File metadata
│   └── README.md              # Section documentation
├── templates/                  # LaTeX templates
│   └── modern_template.tex    # Default template
├── scripts/                    # Generation scripts
│   ├── resume_generator.py    # Main generator script
│   ├── generate_resume.sh     # Shell wrapper
│   └── README.md              # Script documentation
├── jobs/                       # Job-specific resume variants
│   └── python-backend/        # Example: Python backend role
├── docs/                       # Documentation
│   └── getting-started.md     # Quick start guide
├── archive/                    # Legacy files (for reference)
├── output/                     # Generated files (gitignored)
├── .gitignore                  # Git ignore patterns
├── CONTRIBUTING.md             # Contribution guidelines
├── LICENSE                     # MIT License
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```

## 🚀 Quick Start

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
python3 scripts/resume_generator.py --template my_custom_template.tex --template-dir my_templates/
```

## ✏️ Editing Your Resume (TOML Format)

### TOML Structure
The `sections/` directory contains modular TOML files for each resume section:

```toml
# sections/personal.toml
[personal]
name = "Your Name"
title = "Your Professional Title"
location = "Your Location"
email = "your.email@example.com"
phone = "+1 234 567 8900"
github = "github.com/yourusername"
linkedin = "linkedin.com/in/yourprofile"
website = "yourwebsite.com"

# sections/summary.toml
[summary]
text = """Your professional summary here..."""

# sections/skills.toml
[[skills]]
category = "Backend Development"
items = [
    "**Python** (Expert) - FastAPI, Django, Flask",
    "**Node.js** (Advanced) - Express, RESTful APIs"
]

# sections/experience.toml
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

# sections/projects.toml
[[projects]]
name = "Project Name"
technologies = "Tech1, Tech2, Tech3"
link = "https://github.com/user/repo"
highlights = [
    "What you built and why",
    "Technical challenges solved"
]

# sections/education.toml
[[education]]
degree = "Your Degree"
institution = "University Name"
dates = "2016-2020"
location = "City, State"
note = "Cum Laude, GPA: 3.9/4.0"
details = [
    "Relevant coursework or achievements"
]
```

### Benefits of TOML Format

1. **Easy to Write**: Human-readable syntax, similar to INI files
2. **Easy to Parse**: Structured data that computers can easily process
3. **Type Safety**: Native support for strings, arrays, tables
4. **Comments**: Add comments to document your data
5. **Validation**: Syntax errors are caught early
6. **Extensible**: Easy to add new fields without breaking existing code

## 🎨 Template System

### Using External Templates
Templates are stored in `templates/` and use placeholder syntax:

```latex
\documentclass[10pt, letterpaper]{article}
% ... preamble ...

\begin{document}
    \begin{header}
        \fontsize{25 pt}{25 pt}\selectfont {{{NAME}}}
        
        \normalsize
        \mbox{ {{{LOCATION}}} }%
        \AND%
        \mbox{\hrefWithoutArrow{mailto:{{{EMAIL}}} }{ {{{EMAIL}}} }}%
        % ... more contact info ...
    \end{header}

    \section{Professional Summary}
    \begin{onecolentry}
        {{{SUMMARY}}}
    \end{onecolentry}

    {{{SKILLS_SECTION}}}
    {{{EXPERIENCE_SECTION}}}
    % ... more sections ...
\end{document}
```

### Available Placeholders
- `{{{NAME}}}` - Full name
- `{{{LOCATION}}}` - Location
- `{{{EMAIL}}}` - Email address
- `{{{PHONE}}}` - Phone number
- `{{{PHONE_CLEAN}}}` - Phone number (digits only for tel: links)
- `{{{WEBSITE}}}` - Website URL
- `{{{LINKEDIN}}}` - LinkedIn profile
- `{{{GITHUB}}}` - GitHub profile
- `{{{SUMMARY}}}` - Professional summary
- `{{{LAST_UPDATED}}}` - Last updated date
- `{{{SKILLS_SECTION}}}` - Generated skills section
- `{{{EXPERIENCE_SECTION}}}` - Generated experience section
- `{{{PROJECTS_SECTION}}}` - Generated projects section
- `{{{EDUCATION_SECTION}}}` - Generated education section
- `{{{ACHIEVEMENTS_SECTION}}}` - Generated achievements section
- `{{{LEARNING_SECTION}}}` - Generated learning section
- `{{{LANGUAGES_SECTION}}}` - Generated languages section

### Creating Custom Templates

1. Create a new `.tex` file in `templates/`
2. Use the placeholder syntax `{{{PLACEHOLDER_NAME}}}`
3. Include necessary LaTeX packages and environments
4. Test with: `python3 scripts/resume_generator.py --template your_template.tex`

## 🔧 System Requirements

### Basic Generation (Markdown + LaTeX)
- Python 3.x
- python3-tomli (`sudo apt install python3-tomli`)

### PDF Generation
- LaTeX distribution:
  ```bash
  # Ubuntu/Debian
  sudo apt install texlive-latex-base texlive-latex-recommended texlive-latex-extra texlive-fonts-recommended

  # macOS
  brew install mactex

  # Windows
  # Install MiKTeX from https://miktex.org/
  ```

## 📋 Features

### TOML-based Architecture
- **Structured Data**: Well-defined schema for resume content
- **Type Safety**: Proper data types (strings, arrays, tables)
- **Easy Editing**: Human-readable format with syntax highlighting
- **Validation**: Automatic syntax checking and error reporting
- **Extensible**: Easy to add new fields or sections

### Template System
- **External Templates**: LaTeX templates stored separately from code
- **Placeholder System**: Simple `{{{PLACEHOLDER}}}` syntax
- **Multiple Templates**: Support for different resume styles
- **Custom Templates**: Easy to create new layouts
- **Professional Output**: High-quality PDF generation

### Smart Processing
- **LaTeX Escaping**: Automatic escaping of special characters
- **Markdown Support**: Bold text conversion (`**text**` → `\textbf{text}`)
- **URL Handling**: Automatic link generation for contact info
- **Section Generation**: Dynamic section creation from data
- **Error Handling**: Graceful handling of missing data or compilation errors

## 🎯 Job-Specific Tailoring

Create job-specific versions by:

1. **Copy TOML files**: `cp -r sections/ jobs/job-name/`
2. **Modify content**: Edit the copied files for specific requirements
3. **Generate**: `python3 scripts/resume_generator.py --toml-dir jobs/job-name/`
4. **Track versions**: Use git to manage different resume variants

See `jobs/README.md` for detailed guidance on creating tailored resumes.

## 📚 Documentation

- **[Getting Started](docs/getting-started.md)** - Quick start guide for new users
- **[Contributing](CONTRIBUTING.md)** - Guidelines for contributors
- **[Job Tailoring](jobs/README.md)** - Creating job-specific resume variants

## 🛠️ Advanced Usage

### Multiple Output Formats
```bash
# Generate all formats
python3 scripts/resume_generator.py --format all

# Generate only specific format
python3 scripts/resume_generator.py --format pdf
```

### Custom Paths
```bash
# Use different TOML files
python3 scripts/resume_generator.py --toml-file path/to/resume.toml

# Use different template directory
python3 scripts/resume_generator.py --template-dir my_templates/

# Use specific template
python3 scripts/resume_generator.py --template academic_template.tex
```

### Batch Processing
```bash
# Generate resumes for multiple job applications
for job in marketing tech finance; do
    python3 scripts/resume_generator.py \
        --toml-file "ideal-cvs/$job/" \
        --format pdf
done
```

## 🔍 Troubleshooting

### Common Issues

1. **TOML Syntax Errors**
   - Validate TOML syntax using online tools
   - Check string quoting (use `"""` for multi-line strings)
   - Ensure proper array formatting

2. **LaTeX Compilation Fails**
   - Install complete LaTeX distribution
   - Check for special characters in text
   - Verify template placeholder syntax

3. **Missing Content**
   - Ensure all required TOML sections exist
   - Check for empty arrays or missing fields
   - Verify file paths and permissions

### Debug Mode
Add debug prints to the generator script or check the `.log` file in the output directory for detailed LaTeX compilation information.

## 🌟 Benefits of Unified System

### vs. Hardcoded Templates
1. **Flexibility**: Easy to switch between different resume styles
2. **Maintenance**: Template updates don't require code changes
3. **Customization**: Create templates for different industries/roles
4. **Collaboration**: Designers can create templates without coding

### vs. Markdown Files
1. **Structure**: Enforced data schema prevents inconsistencies
2. **Validation**: Syntax errors caught early
3. **Processing**: Easier to parse and manipulate programmatically
4. **Extensibility**: Simple to add new fields or sections

### vs. Manual LaTeX
1. **Automation**: No manual template editing required
2. **Consistency**: Uniform formatting across all sections
3. **Efficiency**: Generate multiple formats from single source
4. **Version Control**: Track content changes independently of formatting

## 📊 Migration Guide

### From Legacy System
The legacy markdown-based system has been removed. To migrate:

1. **Data**: TOML files in `sections/` are the single source of truth
2. **Scripts**: Use `resume_generator.py` instead of old scripts
3. **Templates**: LaTeX templates in `templates/` directory
4. **Output**: Generated files in `output/` directory

### From Single Markdown File
1. Extract sections from `archive/resume_legacy.md`
2. Convert to TOML format following the schema
3. Create or customize a LaTeX template
4. Generate with new system

## 📚 Examples

### Adding New Experience
```toml
[[experience]]
title = "Senior Software Engineer"
company = "New Company"
dates = "June 2025 - Present"
location = "Remote"
description = "Leading backend development for fintech platform"
highlights = [
    "Architected microservices handling 1M+ daily transactions",
    "Reduced API response time by 40% through optimization",
    "Mentored team of 5 junior developers"
]
```

### Adding New Skill Category
```toml
[[skills]]
category = "Cloud & DevOps"
items = [
    "**AWS** (Advanced) - EC2, Lambda, RDS, S3",
    "**Docker** (Expert) - Multi-stage builds, orchestration",
    "**Kubernetes** (Intermediate) - Deployments, services, ingress"
]
```

### Creating Academic Template
Create `templates/academic_template.tex` with different sections like Publications, Research, Teaching Experience, etc.

---

## 📊 Version History

- **v3.0**: Unified TOML-based system with external templates
- **v2.0**: Modular section-based architecture (deprecated)
- **v1.0**: Single-file markdown with parsing-based generation (archived)

---

*For questions or contributions, see the project repository or contact information in the resume.*