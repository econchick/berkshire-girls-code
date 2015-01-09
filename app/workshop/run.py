#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2015 Lynn Root

from app import app


if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])
