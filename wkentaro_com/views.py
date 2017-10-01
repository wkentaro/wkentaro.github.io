import datetime
import os.path as osp

import flask
import gotenshita
import jinja2
import pytz


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
        'chainer/chainer',
        'cupy/cupy',
        'ros/ros',
        'ros/ros_comm',
        'vcstools/wstool',
        'ros-perception/vision_opencv',
        'ros-perception/image_pipeline',
        'ros-perception/perception_pcl',
        'PointCloudLibrary/pcl',
        'start-jsk/jsk_apc',
        'jsk-ros-pkg/jsk_common',
        'jsk-ros-pkg/jsk_recognition',
        'jsk-ros-pkg/jsk_visualization',
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
    now = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
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
