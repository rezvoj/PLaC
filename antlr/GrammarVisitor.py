# Generated from Grammar.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .GrammarParser import GrammarParser
else:
    from GrammarParser import GrammarParser

# This class defines a complete generic visitor for a parse tree produced by GrammarParser.

class GrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by GrammarParser#program.
    def visitProgram(self, ctx:GrammarParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#statement.
    def visitStatement(self, ctx:GrammarParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#type.
    def visitType(self, ctx:GrammarParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#expression.
    def visitExpression(self, ctx:GrammarParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#primary.
    def visitPrimary(self, ctx:GrammarParser.PrimaryContext):
        return self.visitChildren(ctx)



del GrammarParser