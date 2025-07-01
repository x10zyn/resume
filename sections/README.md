# Resume Sections - Unified TOML Structure

This directory contains the modular TOML files that make up the complete resume. Each file focuses on a specific section, making maintenance easier and ensuring data consistency.

## Structure

- **`personal.toml`** - Contact information and personal details
- **`summary.toml`** - Professional summary
- **`skills.toml`** - Technical skills organized by category
- **`experience.toml`** - Work experience with highlights
- **`projects.toml`** - Key projects with technologies and achievements
- **`education.toml`** - Educational background and certifications
- **`achievements.toml`** - Notable accomplishments
- **`learning.toml`** - Learning goals and continuous development
- **`languages.toml`** - Language proficiencies
- **`metadata.toml`** - File metadata and versioning

## Benefits of Unified TOML Structure

✅ **Single source of truth** - All data in structured TOML format  
✅ **Easy maintenance** - Edit individual sections independently  
✅ **Version control friendly** - Changes isolated to relevant sections  
✅ **Consistent format** - Standardized data structure across all sections  
✅ **Scalable** - Easy to add new sections or modify existing ones  
✅ **Validation ready** - Structured data enables automated validation  

## Usage

The resume generation script (`scripts/resume_generator.py`) combines these modular TOML files to create the final resume output in various formats (PDF, Markdown, LaTeX).

## Editing

To update any section:
1. Edit the relevant `.toml` file
2. Run the resume generation script: `python3 scripts/resume_generator.py`
3. The changes will be reflected in all output formats

## TOML Format Benefits

- **Human-readable** - Easy to write and understand
- **Type-safe** - Native support for strings, arrays, tables
- **Validated** - Syntax errors caught early
- **Extensible** - Easy to add new fields without breaking existing code
- **Comments** - Add documentation directly in data files

This unified structure eliminates redundancy and provides a clean, maintainable approach to resume management. 