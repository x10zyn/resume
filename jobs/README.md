# Job-Specific Resume Variants

This directory contains job-specific resume customizations. Each subdirectory represents a tailored version of your resume optimized for a particular role or industry.

## Structure
```
jobs/
├── job-name/                   # Directory per job application
│   ├── personal.json        # Job-specific contact info
│   ├── summary.json         # Tailored professional summary
│   ├── skills.json          # Emphasized relevant skills
│   ├── experience.json      # Highlighted relevant experience
│   ├── projects.json        # Focused project examples
│   ├── education.json       # Relevant education details
│   ├── achievements.json    # Role-specific achievements
│   ├── learning.json        # Current learning goals
│   ├── languages.json       # Language proficiencies
│   ├── metadata.json        # File metadata
│   └── README.md           # Job-specific notes
└── README.md              # This file
```

## Creating Job-Specific Variants

### 1. Copy Base Files
```bash
cp -r sections/ jobs/[job-name]/
```

### 2. Customize Content
Edit the copied JSON files to:
- Emphasize relevant skills and experience
- Reorder sections by importance for the role
- Adjust language and terminology for the industry
- Highlight specific achievements that match job requirements

### 3. Generate Resume
```bash
python3 scripts/resume_generator.py --sections-dir jobs/[job-name]/
```

## Example: Python Backend Role

For a Python backend developer position, you might:

1. **skills.json**: Emphasize Python, databases, APIs
2. **experience.json**: Highlight backend-related achievements
3. **projects.json**: Focus on API development, data processing
4. **summary.json**: Tailor to backend development focus

## Best Practices

1. **Start from Base**: Always copy from `sections/` to maintain consistency
2. **Incremental Changes**: Make targeted adjustments rather than complete rewrites
3. **Track Variants**: Use descriptive directory names (`python-backend`, `frontend-react`, etc.)
4. **Version Control**: Commit each variant separately for easy comparison
5. **Document Changes**: Add README.md explaining customizations for each job

## Generation
```bash
python3 scripts/resume_generator.py --sections-dir jobs/your-job-name/
```

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