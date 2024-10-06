#!/bin/bash

# Check if commit message is passed as an argument
if [ -z "$1" ]; then
  echo "Error: Commit message required."
  echo "Usage: ./deploy.sh \"Your commit message\""
  exit 1
fi

# Navigate to the _site folder
cd _site || { echo "Error: _site directory not found."; exit 1; }

# Add all changes to git
git add ./

# Commit with the provided message
git commit -m "$1"

# Push changes to the current branch
git push

# Print a success message
echo "Changes have been pushed to the repository."
