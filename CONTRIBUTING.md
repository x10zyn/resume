# Contributing to Resume Generator

Thank you for your interest in contributing to this resume generation system! This document provides guidelines for contributing to the project.

## Project Overview

This is a TOML-based resume generation system that creates professional resumes in multiple formats (Markdown, LaTeX, PDF) from structured data files.

## Development Setup

### Prerequisites
- Python 3.7+
- LaTeX distribution (for PDF generation)
- Git

### Installation
1. Clone the repository
2. Install Python dependencies: `pip install toml`
3. Install LaTeX (if PDF generation is needed)

## Project Structure

```
resume/
├── sections/          # TOML data files
├── templates/         # LaTeX templates
├── scripts/          # Generation scripts
├── jobs/             # Job-specific resume variants
├── archive/          # Legacy files
└── output/           # Generated files (gitignored)
```

## Making Changes

### Adding New Resume Sections

1. Create a new TOML file in `sections/`
2. Follow the existing TOML structure
3. Update the generator script to handle the new section
4. Add the section to templates if needed

### Modifying Templates

1. Templates are in `templates/` directory
2. Use placeholder syntax: `{{{PLACEHOLDER_NAME}}}`
3. Test with: `python3 scripts/resume_generator.py --template your_template.tex`

### Updating Scripts

1. Follow Python PEP 8 style guidelines
2. Add proper error handling
3. Include docstrings for functions
4. Test your changes thoroughly

## Code Style

### Python
- Follow PEP 8 style guide
- Use meaningful variable names
- Add type hints where appropriate
- Include docstrings for functions and classes

### TOML
- Use consistent indentation
- Group related fields together
- Add comments to explain complex data
- Validate syntax before committing

### LaTeX
- Use consistent formatting
- Include proper comments
- Follow LaTeX best practices
- Test compilation before committing

## Testing

Before submitting changes:

1. **Test TOML syntax**: Ensure all TOML files are valid
2. **Test generation**: Run the generator script and verify output
3. **Test templates**: Ensure LaTeX templates compile correctly
4. **Test job variants**: Verify job-specific resumes work

```bash
# Test TOML syntax
python3 -c "import toml; toml.load('sections/personal.toml')"

# Test generation
python3 scripts/resume_generator.py

# Test specific template
python3 scripts/resume_generator.py --template templates/modern_template.tex
```

## Commit Guidelines

### Commit Message Format
```
type(scope): description

[optional body]

[optional footer]
```

### Types
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

### Examples
```
feat(sections): add certifications section

fix(templates): resolve LaTeX compilation error

docs(readme): update installation instructions
```

## Pull Request Process

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/your-feature-name`
3. **Make your changes**
4. **Test thoroughly**
5. **Commit with clear messages**
6. **Push to your fork**
7. **Create a pull request**

### Pull Request Checklist

- [ ] Code follows project style guidelines
- [ ] All tests pass
- [ ] Documentation is updated
- [ ] Commit messages are clear and descriptive
- [ ] Changes are focused and minimal

## Issue Reporting

When reporting issues:

1. **Use the issue template** (if available)
2. **Provide clear description** of the problem
3. **Include steps to reproduce**
4. **Add relevant files** (TOML, templates, etc.)
5. **Specify your environment** (OS, Python version, etc.)

## Questions or Need Help?

- Check the README.md for basic usage
- Look at existing issues and pull requests
- Create an issue for questions or problems

## License

By contributing to this project, you agree that your contributions will be licensed under the same license as the project.

---

Thank you for contributing to making this resume generator better! 