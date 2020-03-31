#!/usr/bin/env python

import pathlib

import imgviz


# W / H
aspect_ratio = 2

path = pathlib.Path("./wkentaro_com/static/projects")
for project_dir in path.iterdir():
    src_file = project_dir / "thumbnail_original.jpg"
    if not src_file.exists():
        continue

    src = imgviz.io.imread(src_file)
    H, W = src.shape[:2]

    W_dst = H * aspect_ratio
    dst = imgviz.centerize(src, (H, W_dst), cval=255)

    dst_file = project_dir / "thumbnail.jpg"
    imgviz.io.imsave(dst_file, dst)
