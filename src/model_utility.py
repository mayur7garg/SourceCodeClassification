SYMBOLS = [
    ' ', '\n', '\t', '_', '#', ':', ';', '.', ',', '"', '\'', '?', '@', '$',
    '+', '-', '*', '/', '%', '=', '++', '--', '**', '//', '%%', '==', '===', '+=', '-=', '*=', '/=', '%=', '/*', '*/',
    '<', '>', '<<', '>>', '<>', '<=', '>=', ':=', '<!', '<-', '->',
    '~', '&', '|', '&&', '||', '^',
    '(', ')', '{', '}', '[', ']'
]

if __name__ == "__main__":
    assert(len(SYMBOLS) == len(set(SYMBOLS))) #Check for duplicates
    print(SYMBOLS)