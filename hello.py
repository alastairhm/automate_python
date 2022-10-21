#!/usr/bin/env python
# -*- coding: utf-8 -*-

import fire


def hello(name="World"):
    return "Hello %s!" % name


if __name__ == "__main__":
    fire.Fire()
