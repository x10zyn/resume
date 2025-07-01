# Resume Data Sections

This directory contains modular JSON files that define your resume content. Each file represents a distinct section of your resume, enabling clean separation of concerns and easy maintenance.

## File Structure

```
sections/
├── personal.json       # Contact information and basic details  
├── summary.json        # Professional summary/objective
├── skills.json         # Technical skills and competencies
├── experience.json     # Work experience and achievements
├── projects.json       # Key projects and contributions
├── education.json      # Education, certifications, training
├── achievements.json   # Awards, honors, recognition
├── learning.json       # Current learning goals and interests
├── languages.json      # Language proficiencies
└── metadata.json       # File metadata and generation info
```

## JSON Format Guidelines

### 1. **Structure**
- Use proper JSON syntax with double quotes
- Arrays for multiple items: `["item1", "item2"]`
- Objects for structured data: `{"key": "value"}`
- Consistent indentation (2 spaces recommended)

### 2. **Content Guidelines**
- **Be Specific**: Include metrics, technologies, and impact
- **Use Action Verbs**: Start highlights with strong action words
- **Quantify Results**: Include numbers, percentages, dollar amounts
- **Focus on Value**: Emphasize what you accomplished, not just what you did

### 3. **Validation**
Before committing changes, validate your JSON:
```bash
# Test JSON syntax
python3 -c "import json; json.load(open('sections/personal.json'))"
```

## Section Details

### personal.json
Core contact and identification information.
```json
{
  "personal": {
    "name": "Your Full Name",
    "title": "Professional Title/Role", 
    "email": "your.email@domain.com",
    "phone": "+1 (555) 123-4567",
    "location": "City, State/Province, Country"
  }
}
```

### experience.json
Professional work history with achievements.
```json
{
  "experience": [
    {
      "title": "Job Title",
      "company": "Company Name",
      "dates": "Start Date - End Date",
      "location": "City, State",
      "highlights": [
        "Specific achievement with quantifiable impact",
        "Technical contribution with technologies used"
      ]
    }
  ]
}
```

### projects.json
Key projects demonstrating skills and impact.
```json
{
  "projects": [
    {
      "name": "Project Name",
      "tech": "Technologies, Frameworks, Tools",
      "highlights": [
        "What you built and why it matters",
        "Technical challenges you solved"
      ]
    }
  ]
}
```

## Best Practices

1. **Single Source of Truth**: These JSON files are the authoritative source for all resume formats
2. **Version Control**: Use git to track changes and create resume variants
3. **Modular Updates**: Edit individual files rather than recreating everything
4. **Consistent Formatting**: Follow the established patterns for dates, locations, etc.
5. **Regular Validation**: Check JSON syntax after each edit

## Generating Resumes

After editing these files, generate your resume with:
```bash
python3 scripts/resume_generator.py
```

Check the `output/` directory for generated PDF, LaTeX, and Markdown files. 