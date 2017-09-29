#! /usr/bin/env python3
__author__ = 'sihart'

import os
import jinja2

loader = jinja2.FileSystemLoader(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'templates')))

jenv = jinja2.Environment(loader=loader, trim_blocks=True, lstrip_blocks=True)

template = jenv.get_template('simplejinja.j2')

print(template.render(if_name='eth 1/2'))
