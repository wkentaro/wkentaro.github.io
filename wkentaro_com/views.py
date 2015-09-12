import os
from datetime import datetime, timedelta

from utils.github import get_contributed_repos

from django.shortcuts import render
from django.http import HttpResponse
from django.core.cache import cache


def index(request):
    template_name = 'index.html'
    return render(request, template_name, {'page_name': 'index'})


def about(request):
    template_name = 'about.html'
    return render(request, template_name, {'page_name': 'about'})


def research(request):
    template_name = 'research.html'
    return render(request, template_name, {'page_name': 'research'})


def software(request):
    template_name = 'software.html'

    GITHUB_USERNAME = 'wkentaro'
    GITHUB_PASSWORD = os.environ.get('GITHUB_PASSWORD')
    repo_stats_cache = cache.get('repo_stats')
    if ((repo_stats_cache is None) or
            (repo_stats_cache[0] < datetime.now() - timedelta(days=1))):
        repo_stats = get_contributed_repos(GITHUB_USERNAME,
                                           GITHUB_PASSWORD,
                                           skip_owners=['utmi-2014'])
        cache.set('repo_stats', (datetime.now(), repo_stats))

    return render(request, template_name, {'page_name': 'software',
                                           'repo_stats': repo_stats[:20]})
