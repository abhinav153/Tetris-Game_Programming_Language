from sly import Lexer

class GameLexer(Lexer):
    
    #set of token names.
    tokens = {ID,
              NUMBER,
              ASSIGN,
              LPAREN,
              RPAREN,
              GRID,
              COMMA,
              VARIATION,
              CONSTANT,
              LEVEL,
              APO,
              BLOCK_LIST,
              BLOCK,
              DOT,
              QUEUE,
              SPEED,
              CONTROL,
              SCORE,
              ENGINE,
              START,
              WHILE,
              LEFT_CURLY,
              RIGHT_CURLY,
              INPUT,
              UPDATE,
              ADD,
              SHAPE,
              ORIENTATION,
              BOOLEAN
             }
    
    

    # String containing ignored characters between tokens
    ignore = ' \t'
    ignore_newline = r'\n+'
    
    # Regular expression rules for tokens
    GRID    = r'grid'
    VARIATION = r'variation'
    LEVEL     = r'level'
    BLOCK_LIST = r'block_list'
    BLOCK      = r'block'
    QUEUE      = r'queue'
    SPEED      = r'speed'
    CONTROL     = r'control'
    SCORE      = r'score'
    ENGINE     = r'engine'
    START      = r'start'
    WHILE      = r'while'
    INPUT      = r'input'
    UPDATE     = r'update'
    ADD        = r'add' 
    SHAPE      = r'shape'
    BOOLEAN    = r'TRUE'
    ORIENTATION = r'O|T'
    CONSTANT = r'MARATHON|GREEN|LEFT_ARROW|RIGHT_ARROW|UP_ARROW|DOWN_ARROW'
    ID      = r'[a-zA-Z_][a-zA-Z0-9_]*'
    NUMBER  = r'\d+'
    ASSIGN  = r'='
    LPAREN  = r'\('
    RPAREN  = r'\)'
    COMMA   = r'\,'
    APO = r'\''
    DOT = r'\.'
    LEFT_CURLY = r'\{'
    RIGHT_CURLY = r'\}'


if __name__ == "__main__":
    file = open("example.txt","r")
    data = file.read()	
    lexer = GameLexer()
    for tok in lexer.tokenize(data):
        print('type=%r, value=%r' % (tok.type, tok.value))
        