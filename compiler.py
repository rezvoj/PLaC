import sys
from antlr4 import InputStream, CommonTokenStream
from antlr4.error.ErrorListener import ErrorListener
from antlr.GrammarLexer import GrammarLexer
from antlr.GrammarParser import GrammarParser
from antlr.GrammarVisitor import GrammarVisitor



class SyntaxErrorListener(ErrorListener):
    
    def __init__(self):
        super(SyntaxErrorListener, self).__init__()
        self.errors = []


    def syntaxError(self, _, __, line, ___, msg, ____):
        self.errors.append(f"Syntax error at line {line} {msg}")



class CompilerVisitor(GrammarVisitor):
    defaultValues = {"int": "0", "float": "0.0", "bool": "false", "string": "\"\""}
    operatorInstructions = {
        '+': ["add"], '-': ["sub"], '*': ["mul"], '/': ["div"], 
        "%": ["mod"], ".": ["concat"], '<': ["lt"], '>': ["gt"], 
        '==': ["eq"], '!=': ["eq", "not"], '&&': ["and"], '||': ["or"]
    }
    

    class ExprType:
        def __init__(self, exprType: str, conversions = []):
            self.type = exprType
            self.conversions = conversions


    def __init__(self):
        self.error = False
        self.symbolTable = dict()
        self.instructionList = list()
        self.labelId = 0
        self.conversions = set()


    def _setError(self, errorString: str):
        self.error = True
        print(errorString)
        return CompilerVisitor.ExprType("error")


    def _addInstruction(self, instruction: str):
        if not self.error:
            self.instructionList.append(instruction)

    
    def _getConversionIndex(self):
        return len(self.instructionList)


    def _convertFloat(self, exprTypes: list[ExprType]):
        exprTypeStrs = [exprTypes[0].type, exprTypes[1].type]
        if 'int' in exprTypeStrs and 'float' in exprTypeStrs:
            if exprTypeStrs[0] == 'int':
                self.conversions.update(exprTypes[0].conversions)
            else:
                 self._addInstruction("itof")
            exprTypes[0].type = "float"
            exprTypes[1].type = "float"
        return exprTypes


    def _appendBop(self, bop, exprType = None):
        instructions = CompilerVisitor.operatorInstructions[bop.text]
        for instruction in instructions:
            if exprType is None:
                self._addInstruction(instruction)
            else:
                self._addInstruction(f"{instruction} {exprType}")


    def _checkUnaryExpression(self, exprType: ExprType, allowed: list[str], uop):
        if exprType.type in allowed:
            return exprType
        errorLine, op = uop.line, uop.text
        return self._setError(f"Error at line {errorLine} unary '{op}' is not supported for {exprType.type}")


    def _checkBinaryExpression(self, exprTypes: tuple[ExprType], allowed: list[str], bop, bopType = False):
        self._convertFloat(exprTypes)
        if exprTypes[0].type in allowed and exprTypes[0].type == exprTypes[1].type:
            self._appendBop(bop, exprTypes[0].type if bopType else None)
            exprTypes[0].conversions += exprTypes[1].conversions
            return exprTypes[0]
        errorLine, op = bop.line, bop.text
        errorTypes = f"{exprTypes[0].type} and {exprTypes[1].type}"
        return self._setError(f"Error at line {errorLine} '{op}' is not supported for {errorTypes}")
    

    def _checkBoolExpression(self, exprType: ExprType, stmt: str, token):
        if "bool" != exprType.type and exprType.type != "error":
            errorLine = token.symbol.line
            self._setError(f"Error at line {errorLine} conditional expression in {stmt} must be of type bool")


    def _getForIds(self, count: int, third):
        if count == 3:
            return 0, 1, 2
        if count == 1:
            return None, 0, None
        if isinstance(third, GrammarParser.ExpressionContext):
            return 0, 1, None
        return None, 0, 1


    def visitPrimary(self, primary: GrammarParser.PrimaryContext):
        if primary.expression():
            exprType = self.visit(primary.expression())
            exprType.conversions = [self._getConversionIndex()]
            return exprType
        if primary.INT_LIT():
            self._addInstruction(f"push int {primary.INT_LIT().getText()}")
            return CompilerVisitor.ExprType("int", [self._getConversionIndex()])
        if primary.FLOAT_LIT():
            self._addInstruction(f"push float {primary.FLOAT_LIT().getText()}")
            return CompilerVisitor.ExprType("float", [self._getConversionIndex()])
        if primary.BOOL_LIT():
            self._addInstruction(f"push bool {primary.BOOL_LIT().getText()}")
            return CompilerVisitor.ExprType("bool", [self._getConversionIndex()])
        if primary.STRING_LIT():
            self._addInstruction(f"push string {primary.STRING_LIT().getText()}")
            return CompilerVisitor.ExprType("string", [self._getConversionIndex()])
        identifier = primary.ID().getText()
        if identifier in self.symbolTable:
            self._addInstruction(f"load {identifier}")
            return CompilerVisitor.ExprType(self.symbolTable[identifier], [self._getConversionIndex()])
        errorLine = primary.ID().symbol.line
        return self._setError(f"Error at line {errorLine} variable '{identifier}' not defined")


    def visitExpression(self, expression: GrammarParser.ExpressionContext):
        if expression.primary():
            return self.visit(expression.primary())
        if expression.uop:
            exprType: CompilerVisitor.ExprType = self.visit(expression.expression()[0])
            if exprType.type == "error":
                return exprType
            if expression.uop.text == '-':
                exprType = self._checkUnaryExpression(exprType, ["int", "float"], expression.uop)
                self._addInstruction("uminus")
                return exprType
            if expression.uop.text == '!':
                exprType = self._checkUnaryExpression(exprType, ["bool"], expression.uop)        
                self._addInstruction("not")
                return exprType
        exprTypes: list[CompilerVisitor.ExprType] = (
            self.visit(expression.expression()[0]), 
            self.visit(expression.expression()[1])
        )
        if exprTypes[0].type == "error" or exprTypes[1].type == "error":
            return exprTypes[0]
        if expression.bop.text in ['+', '-', '*', '/']:
            return self._checkBinaryExpression(exprTypes, ["int", "float"], expression.bop)
        if expression.bop.text == '%':
            return self._checkBinaryExpression(exprTypes, ["int"], expression.bop)
        if expression.bop.text == '.':
            return self._checkBinaryExpression(exprTypes, ["string"], expression.bop)
        if expression.bop.text in ['<', '>']:
            exprType = self._checkBinaryExpression(exprTypes, ["int", "float"], expression.bop)
            return CompilerVisitor.ExprType("error" if exprType == "error" else "bool")
        if expression.bop.text in ['==', '!=']:
            exprType = self._checkBinaryExpression(exprTypes, ["int", "float", "string"], expression.bop)
            return CompilerVisitor.ExprType("error" if exprType == "error" else "bool")
        if expression.bop.text in ['&&', '||']:
            return self._checkBinaryExpression(exprTypes, ["bool"], expression.bop)
        primary = expression.expression()[0].primary()
        if not primary or not primary.ID():
            errorLine = expression.bop.line
            return self._setError(f"Error at line {errorLine} expression must be an lvalue")
        variableType = exprTypes[0].type
        if self._convertFloat(exprTypes)[0].type != variableType:
            errorLine = expression.bop.line
            return self._setError(f"Error at line {errorLine} can't store {exprTypes[1].type} into {variableType} variable")
        variableName = primary.ID().getText()
        self._addInstruction(f"save {variableName}")
        self._addInstruction("pop")
        self._addInstruction(f"load {variableName}")
        exprTypes[0].conversions = []
        return exprTypes[0]


    def visitStatement(self, statement: GrammarParser.StatementContext):
        if statement.type_():
            symbolType = "string"
            if statement.type_().INT():
                symbolType = "int"
            elif statement.type_().FLOAT():
                symbolType = "float"
            elif statement.type_().BOOL():
                symbolType = "bool"
            value = CompilerVisitor.defaultValues[symbolType]
            for id in statement.ID():
                identifier = id.getText()
                if identifier not in self.symbolTable:
                    self.symbolTable[identifier] = symbolType
                    self._addInstruction(f"push {symbolType} {value}")
                    self._addInstruction(f"save {identifier}")
                else:
                    errorLine = id.symbol.line
                    self._setError(f"Error at line {errorLine} variable '{identifier}' already defined")
        elif statement.READ():
            for id in statement.ID():
                identifier = id.getText()
                if identifier not in self.symbolTable:
                    errorLine = statement.ID().symbol.line
                    self._setError(f"Error at line {errorLine} variable '{identifier}' not defined")
                else:
                    symbolType = self.symbolTable[identifier]
                    self._addInstruction(f"read {symbolType}")
                    self._addInstruction(f"save {identifier}")
        elif statement.WRITE():
            count = len(statement.expression())
            for i in range(count - 1, -1, -1):
                self.visit(statement.expression()[i])
            self._addInstruction(f"print {count}")
        elif statement.IF():
            firstLabel = self.labelId
            self.labelId += 1
            if statement.ELSE():
                secondLabel = self.labelId
                self.labelId += 1
            exprType = self.visit(statement.expression()[0])
            self._checkBoolExpression(exprType, "if", statement.IF())
            self._addInstruction(f"fjmp {firstLabel}")
            self.visit(statement.statement()[0])
            if statement.ELSE():
                self._addInstruction(f"jmp {secondLabel}")
            self._addInstruction(f"label {firstLabel}")
            if statement.ELSE():
                self.visit(statement.statement()[1])
                self._addInstruction(f"label {secondLabel}")
        elif statement.WHILE():
            firstLabel = self.labelId
            secondLabel = self.labelId + 1
            self.labelId += 2
            self._addInstruction(f"label {firstLabel}")
            exprType = self.visit(statement.expression()[0])
            self._checkBoolExpression(exprType, "while", statement.WHILE())
            self._addInstruction(f"fjmp {secondLabel}")
            self.visit(statement.statement()[0])
            self._addInstruction(f"jmp {firstLabel}")
            self._addInstruction(f"label {secondLabel}")
        elif statement.FOR():
            firstLabel = self.labelId
            secondLabel = self.labelId + 1
            self.labelId += 2
            expressionIds = self._getForIds(len(statement.expression()), statement.children[2])
            if (expressionIds[0] is not None):
                self.visit(statement.expression()[expressionIds[0]])
                self._addInstruction("pop")
            self._addInstruction(f"label {firstLabel}")
            exprType = self.visit(statement.expression()[expressionIds[1]])
            self._checkBoolExpression(exprType, "for", statement.FOR())
            self._addInstruction(f"fjmp {secondLabel}")
            self.visit(statement.statement()[0])
            if (expressionIds[2] is not None):
                self.visit(statement.expression()[expressionIds[2]])
                self._addInstruction("pop")
            self._addInstruction(f"jmp {firstLabel}")
            self._addInstruction(f"label {secondLabel}")
        elif statement.expression():
            self.visit(statement.expression()[0])
            self._addInstruction("pop")
        elif statement.statement():
            for childStatement in statement.statement():
                self.visit(childStatement)


    def visitProgram(self, program: GrammarParser.ProgramContext):
        super().visitProgram(program)
        for offset, idx in enumerate(sorted(list(self.conversions))):
            self.instructionList.insert(offset + idx, "itof")



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
    tree = parser.program()
    if errorListener.errors:
        for error in errorListener.errors:
            print(error)
        return
    visitor = CompilerVisitor()
    visitor.visit(tree)
    if visitor.error:
        return
    try:
        outputFile = open(sys.argv[2], "w")
    except:
        print(f"Can't open file '{sys.argv[2]}'")
        return
    for instruction in visitor.instructionList:
        outputFile.write(f"{instruction}\n")
    outputFile.close()



if __name__ == '__main__':
    main()
