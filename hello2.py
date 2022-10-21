#!/usr/bin/env python
# -*- coding: utf-8 -*-

import fire


def hello(name):
    return "Hello {name}!".format(name=name)


if __name__ == "__main__":
    fire.Fire(hello)
