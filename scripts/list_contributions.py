#!/usr/bin/env python

import getpass
import os.path as osp
import sys

import tabulate

sys.path.insert(0, osp.join(osp.dirname(__file__), '..'))  # NOQA

from wkentaro_com.utils import github


username = raw_input('Username: ')
passwd = getpass.getpass()

headers = ['owner', 'repo', 'n_stars', 'n_commits']
rows = []

contributions = github.get_contributed_repos(username, passwd)
for owner, repo_name, n_commits, n_stars in contributions:
    if n_stars < 10:
        continue
    if n_commits == 0:
        continue
    rows.append((owner, repo_name, n_stars, n_commits))

rows.sort(key=lambda x: (x[3], x[2]), reverse=True)
print(tabulate.tabulate(rows, headers=headers))
