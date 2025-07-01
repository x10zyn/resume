# Resume Generation System - Unified JSON Edition

This resume generation system creates professional resumes in multiple formats (Markdown, LaTeX, PDF) from structured JSON data files.
- Edit resume data in structured JSON format (easy to write, easy to parse)
- Generate professional resumes in multiple formats (Markdown, LaTeX, PDF)
- Job-specific resume variants from modular data
- External LaTeX templates for consistent professional styling
- Terminal-style webapp for real-time editing and preview

```
project/
├── sections/                   # Modular JSON data files
│   ├── personal.json          # Contact information
│   ├── summary.json           # Professional summary
│   ├── skills.json            # Technical skills
│   ├── experience.json        # Work experience
│   ├── projects.json          # Key projects
│   ├── education.json         # Education & certifications
│   ├── achievements.json      # Notable achievements
│   ├── learning.json          # Learning goals
│   ├── languages.json         # Language proficiencies
│   ├── metadata.json          # File metadata
│   └── README.md              # Section documentation
├── jobs/                      # Job-specific resume variants
│   ├── job-name/             # Tailored for specific job
│   │   └── *.json            # Modified JSON files
│   └── README.md             # Jobs documentation
├── scripts/                   # Generation scripts
│   ├── resume_generator.py   # Main generator script
│   └── README.md             # Scripts documentation
├── templates/                 # LaTeX templates
│   └── modern_template.tex   # Professional LaTeX template
├── webapp/                    # Terminal-style web interface
│   ├── app.py                # FastAPI application
│   ├── templates/            # HTML templates
│   ├── static/               # CSS, JS assets
│   └── README.md             # Webapp documentation
├── output/                    # Generated files (PDF, LaTeX, MD)
└── README.md                 # This file
```

## 🚀 Quick Start

1. **Clone & setup**:
   ```sh
   git clone <repo-url>
   cd resume
   pip install -r requirements.txt
   ```

2. **Edit your data**: Modify the JSON files in `sections/`

3. **Generate resume**:
   ```sh
   python3 scripts/resume_generator.py
   ```

4. **View results**: Check `output/` for generated files

5. **Web interface** (optional):
   ```sh
   cd webapp && uvicorn app:app --reload
   ```

## ✏️ Editing Your Resume (JSON Format)

### JSON Structure
The `sections/` directory contains modular JSON files for each resume section:

```json
// sections/personal.json
{
  "personal": {
    "name": "Your Name",
    "title": "Your Title",
    "email": "you@example.com",
    "phone": "+1234567890",
    "location": "City, Country"
  }
}

// sections/summary.json
{
  "summary": "Your professional summary here..."
}

// sections/skills.json
{
  "skills": {
    "languages": ["Python", "JavaScript"],
    "frameworks": ["FastAPI", "React"],
    "tools": ["Git", "Docker"]
  }
}

// sections/experience.json
{
  "experience": [
    {
      "title": "Software Engineer",
      "company": "Company Name",
      "dates": "2023 - Present",
      "location": "City, Country",
      "highlights": [
        "Achievement 1",
        "Achievement 2"
      ]
    }
  ]
}

// sections/projects.json
{
  "projects": [
    {
      "name": "Project Name",
      "tech": "Technologies used",
      "highlights": ["Feature 1", "Feature 2"]
    }
  ]
}

// sections/education.json
{
  "education": [
    {
      "degree": "Degree Name",
      "institution": "University",
      "year": "2023"
    }
  ]
}
```

### Benefits of JSON Format

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

### JSON-based Architecture
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

1. **Copy JSON files**: `cp -r sections/ jobs/job-name/`
2. **Modify content**: Edit the copied files for specific requirements
3. **Generate**: `python3 scripts/resume_generator.py --json-dir jobs/job-name/`
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
# Use different JSON files
python3 scripts/resume_generator.py --json-file path/to/resume.json

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
        --json-file "ideal-cvs/$job/" \
        --format pdf
done
```

## 🔍 Troubleshooting

### Common Issues

1. **JSON Syntax Errors**
   - Validate JSON syntax using online tools
   - Check string quoting (use `"""` for multi-line strings)
   - Ensure proper array formatting

2. **LaTeX Compilation Fails**
   - Install complete LaTeX distribution
   - Check for special characters in text
   - Verify template placeholder syntax

3. **Missing Content**
   - Ensure all required JSON sections exist
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

1. **Data**: JSON files in `sections/` are the single source of truth
2. **Scripts**: Use `resume_generator.py` instead of old scripts
3. **Templates**: LaTeX templates in `templates/` directory
4. **Output**: Generated files in `output/` directory

### From Single Markdown File
1. Extract sections from `archive/resume_legacy.md`
2. Convert to JSON format following the schema
3. Create or customize a LaTeX template
4. Generate with new system

## 📚 Examples

### Adding New Experience
```json
{
  "experience": [
    {
      "title": "Senior Software Engineer",
      "company": "New Company",
      "dates": "June 2025 - Present",
      "location": "Remote",
      "highlights": [
        "Architected microservices handling 1M+ daily transactions",
        "Reduced API response time by 40% through optimization",
        "Mentored team of 5 junior developers"
      ]
    }
  ]
}
```

### Adding New Skill Category
```json
{
  "skills": {
    "languages": ["Python", "JavaScript"],
    "frameworks": ["FastAPI", "React"],
    "tools": ["Git", "Docker"]
  }
}
```

### Creating Academic Template
Create `templates/academic_template.tex` with different sections like Publications, Research, Teaching Experience, etc.

---

## 📊 Version History

- **v3.0**: Unified JSON-based system with external templates
- **v2.0**: Modular section-based architecture (deprecated)
- **v1.0**: Single-file markdown with parsing-based generation (archived)

---

*For questions or contributions, see the project repository or contact information in the resume.*