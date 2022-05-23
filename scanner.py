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
              DIRECTION,
              MODE,
              OPTIONS,
              LEVEL,
              APO,
              BLOCK,
              DOT,
              SPEED,
              CONTROL,
              SCORE,
              ENGINE,
              SHAPE,
              COLOR,
              ORIENTATION,
             }
    
    

    # String containing ignored characters between tokens
    ignore = ' \t'
    ignore_newline = r'\n+'
    
    # Regular expression rules for tokens
    GRID    = r'grid'
    VARIATION = r'variation'
    LEVEL     = r'level'
    BLOCK      = r'block'
    SPEED      = r'speed'
    CONTROL     = r'control'
    SCORE      = r'score'
    ENGINE     = r'engine'
    COLOR      = r'color'
    SHAPE      = r'shape'
    DIRECTION = r'RIGHT_ARROW|UP_ARROW|DOWN_ARROW|LEFT_ARROW'
    MODE      = r'MARATHON|SPRINT|ULTRA'
    ORIENTATION = r'O|T|S|Z|I|J|L'
    OPTIONS   = r'GREEN|RED|CYAN|YELLOW|ORANGE|BLUE|PURPLE'
    ID      = r'[a-zA-Z_][a-zA-Z0-9_]*'
    NUMBER  = r'\d+'
    ASSIGN  = r'='
    LPAREN  = r'\('
    RPAREN  = r'\)'
    COMMA   = r'\,'
    APO = r'\''
    DOT = r'\.'

    @_(r'\d+')
    def NUMBER(self, t):
            t.value = int(t.value)
            return t

    #Line number tracking
    @_(r'\n+')
    def ignore_newline(self,t):
        self.lineno += t.value.count('\n')

    # Error handling rule
    def error(self, t):
        print("Illegal character '%s'" % t.value[0])
        self.index += 1


if __name__ == "__main__":
    file = open("game1.txt","r")
    data = file.read()	
    lexer = GameLexer()
    for tok in lexer.tokenize(data):
        print('type=%r, value=%r lineno:%r' % (tok.type, tok.value, tok.lineno))
    
    print("Number of tokens = ", len(lexer.tokens))                          # Ans. 24
    print("Number of ignore tokens = ", len(lexer.ignore))                   # Ans. 2
    print("Number of patterns = ", len(lexer.tokens) + len(lexer.ignore))    # Ans. 26
   
        