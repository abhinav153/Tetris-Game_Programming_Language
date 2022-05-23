from sly import Parser
from scanner import GameLexer


class GameParser(Parser):

	#Get the token list from the lexer
	tokens = GameLexer.tokens

	#create a debugging file
	debugfile = 'parser.out'

	def __init__(self):
		#will function similar to a symbol table for us
		self.symbol_table = {}


	#Specify the rules and actions
	@_('parameter')
	def start(self,p):
		return ('start',p.parameter)

	
	@_('ID')
	def start(self,p):
		try: 
			if self.symbol_table[p.ID]:
				return (self.symbol_table[p.ID])
		except Exception as e:
			print("Exception occured is {}".format(e))
			return "Variable not initialized"

	@_('variation')
	def parameter(self,p):
		return('parameter',p.variation)
	
	@_('grid')
	def parameter(self,p):
		return ('parameter',p.grid)

	@_('level')
	def parameter(self,p):
		return ('parameter',p.level)

	@_('block')
	def parameter(self,p):
		return ('parameter',p.block)
	
	@_('speed')
	def parameter(self,p):
		return ('parameter',p.speed)

	@_('control')
	def parameter(self,p):
		return ('parameter',p.control)

	@_('score')
	def parameter(self,p):
		return ('parameter',p.score)

	@_('engine')
	def parameter(self,p):
		return ('parameter',p.engine)

	@_('GRID ID ASSIGN LPAREN NUMBER COMMA NUMBER RPAREN')
	def grid(self,p):
		self.symbol_table[p.ID] = [(p[4],p[6]),'GRID']
		return ('grid',p.GRID,p.ID,p.ASSIGN,p.LPAREN,p[3],p.COMMA,p[5],p.RPAREN)


	@_('VARIATION ID ASSIGN MODE')
	def variation(self,p):
		self.symbol_table[p.ID] = [p.MODE,'VARIATION']
		return ('variation',p.VARIATION,p.ID,p.ASSIGN,p.MODE) 

	@_('LEVEL ID ASSIGN APO NUMBER APO')
	def level(self,p):
		self.symbol_table[p.ID] = [p.NUMBER,'LEVEL']
		return ('level',p.LEVEL,p.ID,p.ASSIGN,p[3],p.NUMBER,p[5])

	@_('BLOCK ID')
	def block(self,p):
		self.symbol_table[p.ID] = [{'shape':None,'color':None},'BLOCK']
		return ('block',p.BLOCK,p.ID) 


	@_('ID DOT SHAPE LPAREN APO ORIENTATION APO  RPAREN')
	def block(self,p):
		try:
			if self.symbol_table[p.ID]:
				self.symbol_table[p.ID][0]['shape'] = p.ORIENTATION
			return ('block',p.ID,p.DOT,p.SHAPE,p.LPAREN,p[4],p.ORIENTATION,p[6],p.RPAREN)

		except:
			return "BLOCK does not exist"
	@_('ID DOT COLOR LPAREN OPTIONS RPAREN')
	def block(self,p):
		try:
			if self.symbol_table[p.ID]:
				self.symbol_table[p.ID][0]['color'] = p.OPTIONS
			return ('block',p.ID,p.DOT,p.COLOR,p.LPAREN,p.OPTIONS,p.RPAREN)

		except Exception as e:
			print(e)
			return "BLOCK does not exist"


	@_('SPEED ID ASSIGN NUMBER')
	def speed(self,p):
		self.symbol_table[p.ID] = [p.NUMBER,'SPEED']
		return ('speed',p.SPEED,p.ID,p.ASSIGN,p.NUMBER)

	@_('CONTROL ID ASSIGN DIRECTION')
	def control(self,p):
		self.symbol_table[p.ID] = [p.DIRECTION,'CONTROL']
		return ('control',p.CONTROL,p.ID,p.ASSIGN,p.DIRECTION)

	@_('SCORE ID')
	def score(self,p):
		self.symbol_table[p.ID] = [0,'SCORE']
		return ('score',p.SCORE,p.ID)

	@_('ENGINE ID')
	def engine(self,p):
		self.symbol_table[p.ID] = [None,'ENGINE']
		return ('engine',p.ENGINE,p.ID)

	#user defined method for error detection
	def error(self,p):
		if p:
			print(f"Syntax error at token: {p.type} lineno:{p.lineno}")

		else:
			pass
			#print("Syntax error at EOF")
	

	



if __name__ == "__main__":
   	
    lexer = GameLexer()
    parser = GameParser()
    while True:
    	try:
    		text = input('Game Language > ')
    		tree = parser.parse(lexer.tokenize(text))
    		print(tree)

    	except EOFError:
    		break



