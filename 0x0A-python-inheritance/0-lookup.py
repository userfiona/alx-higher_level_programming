#!/usr/bin/python3
"""Defines a function for object attribute lookup."""


def lookup(obj):
    """Return a list of an object's available attributes."""
    return list(dir(obj))
