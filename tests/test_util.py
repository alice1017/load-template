#!/usr/bin/env python
# coding: utf-8

from unittest import TestCase
from load_template.util import parse_variables


class ParserTestCase(TestCase):

    def test_parse(self):

        variables = [
            "key=value",
            "a=b",
            "c=d"
        ]

        self.assertEqual(
            parse_variables(variables),
            {"key": "value", "a": "b", "c": "d"}
        )
