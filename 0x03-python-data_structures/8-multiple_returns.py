#!/usr/bin/python3
def multiple_returns(sentence):
    """Write a function that returns a tuple with the length of a string and its first character."""
    if len(sentence) == 0:
        result_tuple = len(sentence), None
        return result_tuple
    result_tuple = len(sentence), sentence[0]
    return result_tuple
