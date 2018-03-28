#!/usr/bin/env python
# coding: utf-8

import sys
# import traceback

from .cli import parser
from .core import (
    TemplateLoader,
    render
)
from .util import parse_variables


def main(argv=sys.argv):

    if len(argv) == 1:
        parser.parse_args(["-h"])
        sys.exit(0)

    args = parser.parse_args()
    print args

    loader = TemplateLoader()
    template_contents = loader.load_template(args.template)

    if len(args.vars) != 0:
        variable_data = parse_variables(args.vars)
        contents = render(template_contents, variable_data)

    else:
        contents = template_contents

    print contents
    with open(args.filename, "w") as fp:
        fp.write(contents)


if __name__ == '__main__':

    main()
