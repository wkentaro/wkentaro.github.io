import collections
import datetime
import json
import os
import os.path as osp

import flask
import github3
import gotenshita
import jinja2
import pytz
from werkzeug.contrib.cache import SimpleCache


app = flask.Flask(__name__)
cache = SimpleCache()


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
    token = os.environ.get('GITHUB_TOKEN')
    if token is None:
        return flask.redirect('https://github.com/wkentaro')

    # get repos from github api
    repos = cache.get('repos')
    if repos is None:
        repos = collections.OrderedDict([
            ('Deep Learning + Computer Vision', [
                'wkentaro/labelme',
                'wkentaro/pytorch-fcn',
                'wkentaro/fcn',
                'wkentaro/pascal3d',
                'aleju/imgaug',
            ]),
            ('Deep Learning + Computer Graphics', [
                'wkentaro/chainer-bicyclegan',
                'wkentaro/chainer-cyclegan',
                'wkentaro/real-harem',
            ]),
            ('Deep Learning Library', [
                'chainer/chainer',
                'cupy/cupy',
                'wkentaro/pytorch-for-numpy-users',
                # 'pytorch/pytorch',
            ]),
            ('Computer Vision + Robotics', [
                # 'wkentaro/label_octomap',
                # 'wkentaro/hrp2_apc',
                'wkentaro/label-fusion',
                'start-jsk/jsk_apc',
                'jsk-ros-pkg/jsk_recognition',
                'jsk-ros-pkg/jsk_visualization',
                # 'jsk-ros-pkg/jsk_common',
                'ros-perception/vision_opencv',
                'ros-perception/image_pipeline',
                'ros-perception/perception_pcl',
                # 'PointCloudLibrary/pcl',
                'ros/ros_comm',
                'ros/nodelet_core',
            ]),
            ('Utility', [
                'wkentaro/gdown',
                'wkentaro/gshell',
                'wkentaro/dotfiles',
                # 'wkentaro/wkentaro.zsh-theme',
                'wkentaro/pycd',
                'wkentaro/wstool_cd',
                'wkentaro/gotenshita',
            ]),
        ])
        gh = github3.login(token=token)
        for desc, slugs in repos.items():
            for i, slug in enumerate(slugs):
                owner, name = slug.split('/')
                repo = gh.repository(owner, name)
                repo._my_contributions = None
                for c in repo.iter_contributor_statistics():
                    if c.author.login == 'wkentaro':
                        repo._my_contributions = c.total
                slugs[i] = repo
        cache.set('repos', repos, timeout=60 * 60)  # 1h

    colors_json = osp.join(
        app.static_folder, 'resource/github-colors/colors.json')
    colors = json.load(open(colors_json))

    return flask.render_template(
        'software.html',
        page_name='software',
        repositories=repos,
        colors=colors,
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
