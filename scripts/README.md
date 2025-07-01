# Resume Generation Scripts

This directory contains the scripts for generating resumes from TOML data files.

## Scripts

### `resume_generator.py` - Main Generator
The primary script for generating resumes in multiple formats from TOML data files.

**Usage:**
```bash
# Generate all formats (Markdown, LaTeX, PDF)
python3 scripts/resume_generator.py

# Generate specific format
python3 scripts/resume_generator.py --format markdown
python3 scripts/resume_generator.py --format latex
python3 scripts/resume_generator.py --format pdf

# Use custom template
python3 scripts/resume_generator.py --template academic.tex

# Use different TOML file (for job-specific resumes)
python3 scripts/resume_generator.py --toml-file ideal-cvs/python-backend/resume.toml
```

**Options:**
- `--format`: Output format (all, markdown, latex, pdf)
- `--template`: Template file name (default: modern_template.tex)
- `--template-dir`: Template directory (default: resume/templates)
- `--toml-file`: Specific TOML file to use (default: sections/*.toml)
- `--sections-dir`: Sections directory (default: resume/sections)
- `--output-dir`: Output directory (default: resume/output)

### `generate_resume.sh` - Shell Wrapper
Simple shell wrapper for the main Python script.

**Usage:**
```bash
# Generate all formats
./scripts/generate_resume.sh

# Pass arguments to Python script
./scripts/generate_resume.sh --format pdf --template academic.tex
```

## Features

### Multi-Format Output
- **Markdown**: Clean, readable format for online sharing
- **LaTeX**: Professional typesetting for printing
- **PDF**: Final output for job applications

### Template System
- External LaTeX templates with placeholder system
- Easy to create custom templates
- Support for multiple template styles

### Job-Specific Tailoring
- Generate targeted resumes for specific positions
- Use different TOML files for different job applications
- Maintain multiple resume versions

### Error Handling
- Graceful handling of missing data
- Clear error messages for TOML syntax issues
- Validation of required sections

## Dependencies

### Required
- Python 3.x
- `tomllib` (Python 3.11+) or `tomli` (older versions)

### For PDF Generation
- LaTeX distribution (TeX Live, MiKTeX, etc.)

## Installation

```bash
# Install TOML library (if needed)
pip install tomli

# Install LaTeX (Ubuntu/Debian)
sudo apt install texlive-latex-base texlive-latex-recommended texlive-latex-extra texlive-fonts-recommended

# Install LaTeX (macOS)
brew install mactex

# Install LaTeX (Windows)
# Download and install MiKTeX from https://miktex.org/
```

## Examples

### Basic Usage
```bash
# Generate all formats
python3 scripts/resume_generator.py

# Check output
ls resume/output/
```

### Job-Specific Resume
```bash
# Generate resume for Python backend position
python3 scripts/resume_generator.py \
  --toml-file ideal-cvs/python-backend/resume.toml \
  --format pdf
```

### Custom Template
```bash
# Use academic template
python3 scripts/resume_generator.py \
  --template academic.tex \
  --format pdf
```

### Batch Processing
```bash
# Generate resumes for multiple positions
for job in python-backend frontend-developer data-scientist; do
  python3 scripts/resume_generator.py \
    --toml-file "ideal-cvs/$job/resume.toml" \
    --format pdf
done
```

## Troubleshooting

### Common Issues

1. **TOML Syntax Errors**
   - Check TOML syntax with online validator
   - Ensure proper string quoting for multi-line text
   - Verify array formatting

2. **LaTeX Compilation Fails**
   - Install complete LaTeX distribution
   - Check for special characters in text
   - Verify template placeholder syntax

3. **Missing Content**
   - Ensure all required TOML sections exist
   - Check for empty arrays or missing fields
   - Verify file paths and permissions

### Debug Mode
Add `--debug` flag for verbose output:
```bash
python3 scripts/resume_generator.py --debug
```

## Migration from Legacy System

The legacy markdown-based system has been removed. To migrate:

1. **Data**: TOML files in `sections/` are the single source of truth
2. **Scripts**: Use `resume_generator.py` instead of old scripts
3. **Templates**: LaTeX templates in `templates/` directory
4. **Output**: Generated files in `output/` directory

For questions or issues, refer to the main README.md file. 