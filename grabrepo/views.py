# views.py
import os
import subprocess
import shutil
from django.shortcuts import render
from django.http import HttpResponse
from django import forms
import requests
from django.conf import settings

class GitHubRepoForm(forms.Form):
    repo_url = forms.URLField(label='GitHub Repository URL')

def download_and_analyze(request):
    if request.method == 'POST':
        form = GitHubRepoForm(request.POST)
        if form.is_valid():
            repo_url = form.cleaned_data['repo_url']
            
            # Download the GitHub repository
            repo_name = repo_url.split('/')[-1]
            repo_path = os.path.join(settings.BASE_DIR, repo_name)
            
            # Clone the repository using git
            subprocess.run(['git', 'clone', repo_url, repo_path])
            
            # Run cloc command
            cloc_output = subprocess.check_output(['cloc', repo_path], text=True)
            
            # Delete the downloaded folder
            shutil.rmtree(repo_path)
            
            return render(request, 'result.html', {'cloc_output': cloc_output})

    else:
        form = GitHubRepoForm()

    return render(request, 'index.html', {'form': form})
