#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#
# The MIT License (MIT)
#
# Copyright (C) 2021 - Ericsson
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""See ./README.md for how to use this file."""

import os
import re

NAME = "openapi"
FILE = NAME + ".yaml"
TEMP = NAME + ".tmp"
LICS = NAME + ".license"
UTF8 = "utf-8"

# shutil copy didn't work locally on macOS.
with open(TEMP, 'w', encoding=UTF8) as tmp:
    with open(LICS, encoding=UTF8) as license_text:
        for line in license_text:
            tmp.write(line)
    FILTER = False
    QUERY_P = False
    WADL = False
    with open(FILE, encoding=UTF8) as yaml:
        for line in yaml:
            if re.match(r'^\s\s/.+:$', line):
                # line is a path; check if wadl to remove it:
                WADL = "application.wadl" in line
            elif WADL:
                # wadl stops if no longer within a wadl path:
                WADL = not re.match(r'^\S+:$', line)
            if not WADL:
                if QUERY_P:
                    # previous line was a QueryParameters one, maybe this one is too:
                    QUERY_P = re.match(r'^\s\s\s\s\s\stype: object$', line)
                else:
                    # if QueryParameters lines, will remove these:
                    QUERY_P = re.match(r'^\s\s\s\sQueryParameters:$', line)
                # if Filter lines present unexpectedly, cancel QueryParameters removal:
                FILTER = FILTER or re.match(r'^\s\s\s\sFilter:$', line)
                if not QUERY_P or FILTER:
                    tmp.write(line)

os.rename(TEMP, FILE)
