from scanner import GameLexer
from parser  import GameParser
from interpreter import GameEngine
from interpreter import GameConfig

if __name__ == '__main__':
    file = open("game1.txt","r")
    Lines = file.readlines()
    
    lexer = GameLexer()
    parser = GameParser()

    #our parses our game programming file line by line
    for line in Lines:
        tree = parser.parse(lexer.tokenize(line))
        #print(tree)
    parameters = parser.symbol_table
    GameEngine(GameConfig,parameters)
    
    file.close()

    