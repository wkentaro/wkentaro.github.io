import os.path as osp
import datetime

import flask
import gotenshita
import jinja2


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


@app.route('/software')
def software():
    repos = [
        'pfnet/chainer',
        'cupy/cupy',
        'ros/ros',
        'ros/ros_comm',
        'ros-perception/vision_opencv',
        'ros-perception/image_pipeline',
        'PointCloudLibrary/pcl',
        'start-jsk/jsk_apc',
        'jsk-ros-pkg/jsk_common',
        'jsk-ros-pkg/jsk_recognition',
        'jsk-ros-pkg/jsk_visualization',
        'wkentaro/fcn',
        'wkentaro/pycd',
        'wkentaro/gshell',
        'wkentaro/gdown',
        'wk-jphacks/amazon-ar',
    ]
    repos = [repo.split('/') for repo in repos]

    return flask.render_template(
        'software.html',
        page_name='software',
        repos=repos,
    )


@app.route('/projects/<project_name>')
def projects(project_name):
    try:
        return flask.render_template(
            osp.join('projects', project_name + '.html'),
        )
    except jinja2.exceptions.TemplateNotFound:
        return flask.redirect('/')


@app.route('/projects/gotenshita')
def projects_gotenshita():
    now = datetime.datetime.now()
    if gotenshita.is_gotenshita_open(now, verbose=False):
        info = gotenshita.get_open_info_monthly(now)
        daily_info = []
        for period, open_status in sorted(info[now.day].items()):
            if datetime.datetime.strptime(period[0], '%H:%M').hour >= now.hour:
                daily_info.append((period, open_status))
    else:
        daily_info = []
    return flask.render_template('projects/gotenshita.html',
                                 now=now, info=daily_info)


# -----------------------------------------------------------------------------
# Redirects
# -----------------------------------------------------------------------------


@app.route('/projects/gsoc-2016')
def projects_gsoc_2016():
    return flask.redirect('/projects/gsoc2016')
