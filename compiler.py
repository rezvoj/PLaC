import sys
from antlr4 import InputStream, CommonTokenStream
from antlr4.error.ErrorListener import ErrorListener
from antlr.GrammarLexer import GrammarLexer
from antlr.GrammarParser import GrammarParser



class SyntaxErrorListener(ErrorListener):
    
    def __init__(self):
        super(SyntaxErrorListener, self).__init__()
        self.errors = []


    def syntaxError(self, _, __, line, ___, msg, ____):
        self.errors.append(f"Syntax error at line {line} {msg}")



def main():
    if len(sys.argv) < 3:
        print("Error: wrong compiler arguments")
        return
    try:
        inputFile = open(sys.argv[1])
    except:
        print(f"File '{sys.argv[1]}' does not exist")
        return
    input = inputFile.read()
    inputFile.close()
    inputStream = InputStream(input)
    lexer = GrammarLexer(inputStream)
    tokenStream = CommonTokenStream(lexer)
    parser = GrammarParser(tokenStream)
    parser.removeErrorListeners()
    errorListener = SyntaxErrorListener()
    parser.addErrorListener(errorListener)
    parser.program()
    if errorListener.errors:
        for error in errorListener.errors:
            print(error)
    else:
        print("No errors encountered")



if __name__ == '__main__':
    main()
