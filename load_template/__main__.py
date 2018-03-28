#!/usr/bin/env python
# coding: utf-8

import sys
import traceback

from .cli import parser
from .core import (
    TemplateLoader,
    render
)
from .util import parse_variables


def program(args):

    loader = TemplateLoader()
    template_contents = loader.load_template(args.template)

    if len(args.vars) != 0:
        variable_data = parse_variables(args.vars)
        contents = render(template_contents, variable_data)

    else:
        contents = template_contents

    with open(args.filename, "w") as fp:
        fp.write(contents)

    return 0


def main(argv=sys.argv):

    if len(argv) == 1:
        parser.parse_args(["-h"])
        sys.exit(0)

    args = parser.parse_args()
    print args

    try:
        exit_code = program(args)
        sys.exit(exit_code)

    except Exception as e:
        error_name = type(e).__name__
        stacktrace = traceback.format_exc()

        if args.dev:
            print stacktrace.strip()

        else:
            sys.stderr.write("{0}: {1}".format(error_name, e.message))


if __name__ == '__main__':

    main()
