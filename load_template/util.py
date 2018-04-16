#!/usr/bin/env python
# coding: utf-8

import os
import sys

from subprocess import call as run


def parse_variables(vars):

    result = {}

    for variable in vars:
        key, value = variable.split("=")
        result[key] = value

    return result


def separate(items, num):

    for index in range(0, len(items), num):
        yield items[index:(index + num)]


def display_list(template_list):

    first_line = second_line = third_line = ""
    template = "* {}"

    for items in separate(template_list, 3):

        max_length = max([len(item) for item in items]) + 5
        adjust = (lambda item: item.ljust(max_length))

        for index, item in enumerate(items, start=1):

            if index == 1:
                first_line += template.format(adjust(item))

            elif index == 2:
                second_line += template.format(adjust(item))

            elif index == 3:
                third_line += template.format(adjust(item))

    print "\n".join([first_line, second_line, third_line])


def get_editor():

    if sys.platform.startswith("win"):
        return "notepad.exe"

    editor_env = ["VISUAL", "EDITOR"]
    editor_cmd = ["vim", "nano"]

    for env in editor_env:

        editor = os.environ.get(env)
        if editor:
            return editor

    for cmd in editor_cmd:

        which_cmd = "which {0} > /dev/null 2>&1".format(cmd)
        is_exist_cmd = (os.system(which_cmd) == 0)

        if is_exist_cmd:
            return cmd

    return "vi"


def edit(filepath):

    editor = get_editor()
    cmd = [editor, filepath]

    return run(cmd)
