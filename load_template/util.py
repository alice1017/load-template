#!/usr/bin/env python
# coding: utf-8


def parse_variables(vars):

    result = {}

    for variable in vars:
        key, value = variable.split("=")
        result[key] = value

    return result
