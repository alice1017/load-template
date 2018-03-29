#!/usr/bin/env python
# coding: utf-8

from unittest import TestCase
from load_template.util import (
    parse_variables,
    separate
)


class UtilitiesTestCase(TestCase):

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

    def test_separate(self):

        testcase = "123456789"

        self.assertEqual(
            list(separate(testcase, 3)),
            ["123", "456", "789"]
        )

        self.assertEqual(
            list(separate(testcase, 2)),
            ["12", "34", "56", "78", "9"]
        )
