#!/usr/bin/env python
# coding: utf-8

from unittest import TestCase

from load_template.cli import parser


class ParserTestCase(TestCase):

    def test_positional_args(self):

        arg_template = "template"
        arg_filename = "file"
        arg_variable = "key=value"

        args = parser.parse_args([
            arg_template,
            arg_filename,
            arg_variable
        ])

        self.assertEqual(args.template, arg_template)
        self.assertEqual(args.filename, arg_filename)
        self.assertEqual(args.vars[0], arg_variable)

    def test_optional_args(self):

        args = parser.parse_args(["--dev"])
        self.assertTrue(args.dev)

        args = parser.parse_args(["--list"])
        self.assertTrue(args.list)
