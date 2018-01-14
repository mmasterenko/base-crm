TRANS_TO_UNDERSCORE = ''.maketrans(' /-', '___')


def to_snakecase(string):
    return string.translate(TRANS_TO_UNDERSCORE).lower()
