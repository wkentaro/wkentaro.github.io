#!/usr/bin/env python

from __future__ import annotations

from collections.abc import Iterator

from flask_frozen import Freezer

from wkentaro_com.views import app


def main() -> None:
    freezer = Freezer(app)

    @freezer.register_generator
    def project() -> Iterator[dict[str, str]]:
        yield {"project_name": "gsoc2016"}

    freezer.freeze()

    with open("wkentaro_com/build/CNAME", "w") as f:
        f.write("www.wkentaro.com\n")


if __name__ == "__main__":
    main()
