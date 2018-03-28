#!/usr/bin/env python
# coding: utf-8

import os
import codecs
import shutil

TEMPLATE_DIR = os.path.join(os.environ["HOME"], ".templates")

DEFAULT_TEMPLATE_DIR = os.path.abspath(
    os.path.join(__file__, "../../templates")
)


class TemplateLoader:

    def __init__(
            self, template_dir=TEMPLATE_DIR, default_dir=DEFAULT_TEMPLATE_DIR):

        if not os.path.isdir(template_dir):
            self._initialize_dir(template_dir, default_dir)

        self.template_dir = template_dir

    @property
    def templates_list(self):

        return os.listdir(self.template_dir)

    @property
    def templates_data(self):

        data = {}

        for template in self.templates_list:

            template_path = os.path.join(self.template_dir, template)
            with codecs.open(template_path, "r", "utf-8") as fp:
                content = fp.read()

            data[template] = content

        return data

    def load_template(self, template):

        if template in self.templates_data:
            return self.templates_data[template]

        else:
            raise KeyError("Template has not found: '{0}'".format(template))

    def _initialize_dir(self, template_dir, default_dir):

        os.mkdir(template_dir)

        for template in os.listdir(default_dir):

            template_path = os.path.join(default_dir, template)
            shutil.copy(template_path, template_dir)


def render(template, variables):

    return template.format(**variables)
