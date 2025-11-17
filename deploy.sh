#!/bin/bash
# Quick deployment helper script

set -e

echo "🚀 S2S Geospatial Deployment Helper"
echo "===================================="
echo ""

# Check if git is configured
if ! git config user.name > /dev/null 2>&1; then
    echo "⚙️  Git not configured. Please configure:"
    echo ""
    read -p "Enter your name: " git_name
    read -p "Enter your email: " git_email
    git config user.name "$git_name"
    git config user.email "$git_email"
    echo "✅ Git configured"
fi

echo ""
echo "📝 Before deploying, you need to:"
echo ""
echo "1. Create GitHub repository at https://github.com/new"
echo "   Suggested name: YOUR_USERNAME.github.io"
echo ""
read -p "Have you created the GitHub repo? (y/n): " created_repo

if [ "$created_repo" != "y" ]; then
    echo "Please create the repo first, then run this script again."
    exit 1
fi

echo ""
read -p "Enter your GitHub username: " gh_username
read -p "Enter your repo name: " repo_name

echo ""
echo "📦 Updating configuration..."

# Update config.toml baseURL
sed -i.bak "s|baseURL = \"https://YOUR_USERNAME.github.io/YOUR_REPO_NAME/\"|baseURL = \"https://${gh_username}.github.io/${repo_name}/\"|" config.toml
rm config.toml.bak

echo "✅ Updated config.toml"

echo ""
echo "🔧 Git setup..."

# Add remote if not exists
if ! git remote get-url origin > /dev/null 2>&1; then
    git remote add origin "https://github.com/${gh_username}/${repo_name}.git"
    echo "✅ Added remote origin"
else
    echo "ℹ️  Remote origin already exists"
fi

echo ""
echo "📤 Committing and pushing to GitHub..."

git add -A
git commit -m "Initial commit - S2S Geospatial site" || echo "Nothing to commit"
git branch -M main
git push -u origin main

echo ""
echo "✅ Code pushed to GitHub!"
echo ""
echo "📋 Next steps:"
echo ""
echo "1. Enable GitHub Pages:"
echo "   → Go to: https://github.com/${gh_username}/${repo_name}/settings/pages"
echo "   → Source: Select 'GitHub Actions'"
echo ""
echo "2. Deploy Dashboard to Hugging Face Spaces:"
echo "   → See detailed instructions in DEPLOYMENT.md"
echo "   → Upload files from dashboard/ folder"
echo ""
echo "3. After HF Space is live, update the dashboard iframe:"
echo "   → Edit content/dashboard/index.md"
echo "   → Replace YOUR_USERNAME and YOUR_SPACE_NAME"
echo "   → git add, commit, and push again"
echo ""
echo "Your site will be live at:"
echo "https://${gh_username}.github.io/${repo_name}/"
echo ""
echo "Happy deploying! 🎉"
