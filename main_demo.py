from scanner import GameLexer
from parser  import GameParser

if __name__ == '__main__':
    file = open("game1.txt","r")
    data = file.read()

    lexer = GameLexer()
    parser = GameParser()

    tree = parser.parse(lexer.tokenize(data))
    print(tree)
    print(parser.symbol_table)
    file.close()