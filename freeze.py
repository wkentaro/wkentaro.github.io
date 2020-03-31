#!/usr/bin/env python

from flask_frozen import Freezer

from wkentaro_com.views import app


def main():
    freezer = Freezer(app)

    @freezer.register_generator
    def projects():
        yield {"project_name": "gsoc2016"}

    freezer.freeze()

    with open("wkentaro_com/build/CNAME", "w") as f:
        f.write("www.wkentaro.com\n")


if __name__ == "__main__":
    main()
