#!/usr/bin/env python

import imgviz
import path


H = 300
W = 600

here = path.Path(__file__).abspath().parent

path = here / "wkentaro_com/data/img"
for project_dir in path.listdir():
    src_file = project_dir / "thumbnail.jpg"
    if not src_file.exists():
        continue

    src = imgviz.io.imread(src_file)

    dst = imgviz.centerize(src, (H, W), cval=255)

    dst_file = (
        here
        / "wkentaro_com/static/img/"
        / project_dir.basename()
        / "thumbnail.jpg"
    )
    dst_file.parent.makedirs_p()

    imgviz.io.imsave(dst_file, dst)
