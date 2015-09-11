#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from django.db import models

from github3 import login


def get_contributed_repos(username, password):
    gh = login(username, password)
    repos = gh.iter_user_repos(username, type='public')

    repo_stats = []
    for repo in repos:
        if not repo.fork:
            continue

        repo.refresh()
        repo = repo.parent

        owner = repo.owner.login
        repo_name = repo.name

        for stat in repo.iter_contributor_statistics():
            if stat.author.login == username:
                n_commits = stat.total
                break
        else:
            n_commits = 0

        repo_stats.append((owner, repo_name, n_commits))

    repo_stats = sorted(repo_stats, key=lambda x:x[2], reverse=True)
    return repo_stats
