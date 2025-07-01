#!/bin/bash

# Resume Generator - Git Setup Script
# This script helps set up git configuration and prepare the repository

echo "🚀 Setting up Git for Resume Generator"

# Check if git config is already set
if [ -z "$(git config --global user.name)" ] || [ -z "$(git config --global user.email)" ]; then
    echo "⚠️  Git user configuration not found."
    echo "Please set your git identity:"
    echo ""
    echo "git config --global user.name \"Your Name\""
    echo "git config --global user.email \"your.email@example.com\""
    echo ""
    echo "Or set it locally for this repository:"
    echo "git config user.name \"Your Name\""
    echo "git config user.email \"your.email@example.com\""
    echo ""
    read -p "Press Enter after setting your git identity..."
fi

# Check git status
echo "📊 Current git status:"
git status

echo ""
echo "✅ Setup complete!"
echo ""
echo "Next steps:"
echo "1. Review the staged files: git status"
echo "2. Make your first commit: git commit -m \"feat: initial commit\""
echo "3. Add remote repository: git remote add origin <your-repo-url>"
echo "4. Push to GitHub: git push -u origin main"
echo ""
echo "📚 Documentation:"
echo "- README.md - Main project documentation"
echo "- docs/getting-started.md - Quick start guide"
echo "- CONTRIBUTING.md - Contribution guidelines"
echo "- jobs/README.md - Job-specific resume guidance" 
