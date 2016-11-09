import os.path as osp

import flask


app = flask.Flask(__name__)


@app.route('/')
def index():
    return flask.render_template(
        'index.html',
        page_name='index',
    )


@app.route('/about')
def about():
    return flask.render_template(
        'about.html',
        page_name='about',
    )


@app.route('/research')
def research():
    return flask.render_template(
        'research.html',
        page_name='research',
    )


@app.route('/software')
def software():
    repos = [
        'pfnet/chainer',
        'pfnet/cupy',
        'ros/ros',
        'ros/ros_comm',
        'ros-perception/vision_opencv',
        'ros-perception/image_pipeline',
        'start-jsk/jsk_apc',
        'jsk-ros-pkg/jsk_common',
        'jsk-ros-pkg/jsk_recognition',
        'jsk-ros-pkg/jsk_visualization',
        'wkentaro/fcn',
        'wkentaro/pycd',
        'wkentaro/gshell',
        'wkentaro/gdown',
    ]
    repos = [repo.split('/') for repo in repos]

    return flask.render_template(
        'software.html',
        page_name='software',
        repos=repos,
    )


@app.route('/projects/<project_name>')
def projects(project_name):
    return flask.render_template(
        osp.join('projects', project_name + '.html'),
    )
