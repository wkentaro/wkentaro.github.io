import os.path as osp
import sys

this_dir = osp.realpath(osp.dirname(__file__))
sys.path.insert(0, this_dir)

from wkentaro_com.views import app as application

# vim: set ft=python;
