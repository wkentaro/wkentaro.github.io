import datetime
import json
import os.path as osp
import subprocess

import flask
import jinja2
import yaml


here = osp.dirname(osp.abspath(__file__))

app = flask.Flask(__name__)


@app.route("/")
def index():
    filename = osp.join(here, "data/research.yaml")
    with open(filename) as f:
        papers = yaml.safe_load(f)["papers"]
        papers = [paper for paper in papers if paper["selected"]]

    try:
        timestamp = subprocess.check_output(
            'git log -1 --format="%at" templates/include/updates.html',
            shell=True,
            cwd=here,
        )
        timestamp = int(timestamp.strip())
        updated_at = datetime.datetime.fromtimestamp(timestamp)
    except Exception:
        updated_at = None

    return flask.render_template(
        "index.html", name="index", updated_at=updated_at, papers=papers
    )


@app.route("/research/")
def research():
    filename = osp.join(here, "data/research.yaml")
    with open(filename) as f:
        data = yaml.safe_load(f)
        papers = data["papers"]
        other_projects = data["other_projects"]

    return flask.render_template(
        "research.html",
        name="research",
        papers=papers,
        other_projects=other_projects,
    )


@app.route("/software/")
def software():
    filename = osp.join(here, "data/software.yaml")
    with open(filename) as f:
        repos = yaml.safe_load(f)["repositories"]

    filename = osp.join(here, "data/github-colors.json")
    with open(filename) as f:
        colors = json.load(f)

    return flask.render_template(
        "software.html", name="software", repositories=repos, colors=colors,
    )


@app.route("/projects/<project_name>/")
def projects(project_name):
    try:
        return flask.render_template(
            osp.join("projects", project_name + ".html"),
        )
    except jinja2.exceptions.TemplateNotFound:
        return flask.redirect("/")
