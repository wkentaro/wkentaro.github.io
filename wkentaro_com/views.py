import collections
import json
import os.path as osp

import flask
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
    repos = collections.OrderedDict([
        ('Deep Learning + Computer Vision', [
            'wkentaro/labelme',
            'wkentaro/pytorch-fcn',
            'wkentaro/fcn',
            'wkentaro/chainer-mask-rcnn',
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


# -----------------------------------------------------------------------------
# Redirects
# -----------------------------------------------------------------------------


@app.route('/projects/gsoc-2016')
def projects_gsoc_2016():
    return flask.redirect('/projects/gsoc2016')
