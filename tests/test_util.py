#!/usr/bin/env python
# coding: utf-8

import sys

from unittest import TestCase
from load_template.util import (
    parse_variables,
    separate,
    display_list
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

    def test_display(self):

        testcase = ["Alice", "Bob", "Python"]
        result = "* Alice " + " " * 5 + "\n"
        result += "* Bob   " + " " * 5 + "\n"
        result += "* Python" + " " * 5 + "\n"
        fp = self._setup_testcase()

        display_list(testcase)

        stdout = self._get_stdout(fp)

        self.assertEqual(stdout, result)

    def _setup_testcase(self):

        tmpfile = "/tmp/load-template-tmpfile"
        fp = open(tmpfile, "w")

        sys.stdout = fp

        return fp

    def _get_stdout(self, fp):

        sys.stdout = sys.__stdout__
        fp.close()

        tmpfile = "/tmp/load-template-tmpfile"
        with open(tmpfile, "r") as fp:
            return fp.read()
