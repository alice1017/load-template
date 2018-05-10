#!/usr/bin/env python
# coding: utf-8

import sys
import codecs
import traceback

from .cli import parser
from .core import (
    TemplateLoader,
    render
)
from .util import (
    parse_variables,
    display_list,
    edit
)


def program(args):

    loader = TemplateLoader()

    if args.list:
        display_list(loader.templates_list)
        return 0

    if args.sync:

        loader._sync_templates(loader.template_dir, loader.default_dir)
        return 0

    if args.contents:

        if not args.template:
            raise ValueError("Please write template name.")

        template_contents = loader.load_template(args.template)
        print template_contents
        return 0

    template_contents = loader.load_template(args.template)

    if len(args.vars) != 0:
        variable_data = parse_variables(args.vars)
        contents = render(template_contents, variable_data)

    else:
        contents = template_contents

    with codecs.open(args.filename, "w", "utf-8") as fp:
        fp.write(contents)

    if args.edit:
        return edit(args.filename)

    else:
        return 0


def main(argv=sys.argv):

    if len(argv) == 1:
        parser.parse_args(["-h"])
        sys.exit(0)

    args = parser.parse_args()

    try:
        exit_code = program(args)
        sys.exit(exit_code)

    except Exception as e:
        error_name = type(e).__name__
        stacktrace = traceback.format_exc()

        if args.dev:
            print stacktrace.strip()

        else:
            sys.stderr.write("{0}: {1}\n".format(error_name, e.message))


if __name__ == '__main__':

    main()
