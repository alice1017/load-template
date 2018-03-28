#!/usr/bin/env python
# coding: utf-8

import sys
# import traceback

from .cli import parser


def main(argv=sys.argv):

    if len(argv) == 1:
        parser.parse_args(["-h"])
        sys.exit(0)

    args = parser.parse_args()

    print args


if __name__ == '__main__':

    main()
