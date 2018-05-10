#!/usr/bin/env python
# coding: utf-8

from argparse import (
    ArgumentParser,
    OPTIONAL,
    ZERO_OR_MORE,
    RawDescriptionHelpFormatter
)

parser = ArgumentParser(
    prog="load-template",
    formatter_class=RawDescriptionHelpFormatter,
    description="Create a file from the template with the variables.\n"
                "You can create the templates as freely "
                "if you save it '~/.templates/' directory."
)

parser.add_argument(
    "template",
    action="store",
    nargs=OPTIONAL,
    default=None,
    help="The template name. You can show all templates by '--list'")

parser.add_argument(
    "filename",
    metavar="file",
    action="store",
    nargs=OPTIONAL,
    default=None,
    help="The file name to create.")

parser.add_argument(
    "vars",
    metavar="variables",
    action="store",
    nargs=ZERO_OR_MORE,
    default=None,
    help="The variables formatted 'key=value'.")

parser.add_argument(
    "-l", "--list",
    action="store_true",
    help="Display the template list.")

parser.add_argument(
    "-c", "--contents",
    action="store_true",
    help="Display contents of the template.")

parser.add_argument(
    "-s", "--sync",
    action="store_true",
    help="Sync the default template to local template. "
         "Before using this feature, you have to do `git pull`.")

parser.add_argument(
    "-n", "--no-edit",
    action="store_false",
    dest="edit",
    default=True,
    help="create a file without edit.")

parser.add_argument(
    "-D", "--dev",
    action="store_true",
    help="Run development mode.")
