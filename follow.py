#!/usr/bin/env python
# -*- coding: utf-8 -*-

import utils

apis = utils.get_apis()
for api in apis:
    utils.follow(api)
