#!/usr/bin/env python

import pathlib

import imgviz


H = 300
W = 600

path = pathlib.Path("./wkentaro_com/static/projects")
for project_dir in path.iterdir():
    src_file = project_dir / "thumbnail_original.jpg"
    if not src_file.exists():
        continue

    src = imgviz.io.imread(src_file)

    dst = imgviz.centerize(src, (H, W), cval=255)

    dst_file = project_dir / "thumbnail.jpg"
    imgviz.io.imsave(dst_file, dst)
