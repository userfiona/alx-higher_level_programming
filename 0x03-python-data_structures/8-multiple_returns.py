def multiple_returns(sentence):
    """
    Function that returns a tuple containing the length of the sentence and the first character.

    Args:
        sentence (str): The input sentence.

    Returns:
        tuple: A tuple containing the length of the sentence and the first character, or None if the sentence is empty.

    """
    if len(sentence) == 0:
        result_tuple = len(sentence), None
        return result_tuple
    result_tuple = len(sentence), sentence[0]
    return result_tuple
