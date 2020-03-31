#!/usr/bin/env python

import argparse

from wkentaro_com.views import app


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=5000)
    args = parser.parse_args()

    app.run(port=args.port, debug=True)


if __name__ == "__main__":
    main()
