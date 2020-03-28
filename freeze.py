#!/usr/bin/env python

import argparse

from flask_frozen import Freezer

from wkentaro_com.views import app


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, default=5000)
    args = parser.parse_args()

    port = args.port
    debug = True

    freezer = Freezer(app)

    @freezer.register_generator
    def projects():
        yield {"project_name": "gsoc2016"}

    freezer.freeze()


if __name__ == '__main__':
    main()
