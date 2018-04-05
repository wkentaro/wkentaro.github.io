#!/usr/bin/env python

import argparse

from wkentaro_com.views import app


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, default=5000)
    args = parser.parse_args()

    port = args.port
    debug = True

    app.run(host='localhost', port=port, debug=debug)


if __name__ == '__main__':
    main()
