from github3 import login


def get_contributed_repos(username, password, skip_owners=None):
    gh = login(username, password)
    repos = gh.iter_user_repos(username, type='public')

    for repo in repos:
        if not repo.fork:
            continue

        # FIXME: multiprocessing does not work with repo.refresh
        repo.refresh()
        repo = repo.parent

        owner = repo.owner.login
        repo_name = repo.name

        if skip_owners and owner in skip_owners:
            continue

        for stat in repo.iter_contributor_statistics():
            if stat.author.login == username:
                n_commits = stat.total
                break
        else:
            n_commits = 0

        yield owner, repo_name, n_commits, repo.stargazers
