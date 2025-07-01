# Job-Specific Resume Variants

This directory contains tailored resume versions for specific job applications. Each subdirectory represents a different job or role you're applying for.

## Structure

```
jobs/
├── python-backend/          # Example: Python backend developer role
│   ├── personal.toml        # Job-specific contact info
│   ├── summary.toml         # Tailored professional summary
│   ├── skills.toml          # Emphasized relevant skills
│   ├── experience.toml      # Highlighted relevant experience
│   ├── projects.toml        # Focused project examples
│   ├── education.toml       # Relevant education details
│   ├── achievements.toml    # Role-specific achievements
│   ├── learning.toml        # Current learning goals
│   ├── languages.toml       # Language proficiencies
│   ├── metadata.toml        # File metadata
│   ├── job-posting.md       # Original job posting (for reference)
│   └── README.md            # Notes about this application
├── frontend-developer/      # Example: Frontend developer role
│   └── ... (similar structure)
└── README.md                # This file
```

## Creating Job-Specific Resumes

### 1. Create a New Job Directory
```bash
mkdir jobs/your-job-name
```

### 2. Copy Base Resume Data
```bash
cp -r sections/* jobs/your-job-name/
```

### 3. Customize for the Role
- **Update summary**: Tailor to the specific role requirements
- **Emphasize skills**: Highlight relevant technical skills
- **Reorder experience**: Put most relevant experience first
- **Select projects**: Choose projects that match the role
- **Adjust achievements**: Focus on role-specific accomplishments

### 4. Generate Job-Specific Resume
```bash
python3 scripts/resume_generator.py --toml-dir jobs/your-job-name/
```

## Best Practices

### Content Tailoring
- **Keyword matching**: Include keywords from the job posting
- **Relevant experience**: Emphasize experience that matches the role
- **Project selection**: Choose projects that demonstrate required skills
- **Achievement focus**: Highlight achievements relevant to the position

### File Organization
- **Clear naming**: Use descriptive directory names
- **Job posting**: Save the original job posting for reference
- **Notes**: Document your customization decisions
- **Version control**: Track changes for each application

### Template Selection
- **Industry appropriate**: Choose templates that fit the industry
- **Company culture**: Consider the company's style and culture
- **Role requirements**: Some roles may prefer different formats

## Example: Python Backend Developer

The `python-backend/` directory shows an example of tailoring for a Python backend role:

- **Skills emphasis**: Python, FastAPI, Django, databases
- **Experience focus**: Backend development, API design, database optimization
- **Project selection**: Backend services, API development, database projects
- **Achievements**: Performance improvements, scalability, system architecture

## Version Control Strategy

### Git Workflow
1. **Base resume**: Keep `sections/` as your master resume
2. **Job variants**: Create branches for each job application
3. **Customizations**: Commit changes specific to each application
4. **Merge back**: Incorporate successful strategies into base resume

### Branch Naming
```
feature/job-company-name
feature/job-role-name
```

### Commit Messages
```
feat(jobs): add python-backend variant for Company X

- Tailored summary for backend role
- Emphasized Python and database skills
- Reordered experience to highlight relevant work
```

## Tips for Success

1. **Research the company**: Understand their culture and needs
2. **Match keywords**: Use terminology from the job posting
3. **Quantify achievements**: Include specific metrics and results
4. **Keep it relevant**: Focus on experience that applies to the role
5. **Test different versions**: Try different approaches and templates

---

Remember: The goal is to show how your experience and skills specifically match what the employer is looking for! 