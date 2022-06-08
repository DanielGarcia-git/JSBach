# Generated from jsbach.g by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .jsbachParser import jsbachParser
else:
    from jsbachParser import jsbachParser

# This class defines a complete generic visitor for a parse tree produced by jsbachParser.

class jsbachVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by jsbachParser#root.
    def visitRoot(self, ctx:jsbachParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#instructions.
    def visitInstructions(self, ctx:jsbachParser.InstructionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#instruction.
    def visitInstruction(self, ctx:jsbachParser.InstructionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#listInstructions.
    def visitListInstructions(self, ctx:jsbachParser.ListInstructionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#listAddElement.
    def visitListAddElement(self, ctx:jsbachParser.ListAddElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#listCutElement.
    def visitListCutElement(self, ctx:jsbachParser.ListCutElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#listGetElement.
    def visitListGetElement(self, ctx:jsbachParser.ListGetElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#listSize.
    def visitListSize(self, ctx:jsbachParser.ListSizeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#conditional.
    def visitConditional(self, ctx:jsbachParser.ConditionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#while_.
    def visitWhile_(self, ctx:jsbachParser.While_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#read.
    def visitRead(self, ctx:jsbachParser.ReadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#write.
    def visitWrite(self, ctx:jsbachParser.WriteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#assign.
    def visitAssign(self, ctx:jsbachParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#PlayList.
    def visitPlayList(self, ctx:jsbachParser.PlayListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#PlayNoteVar.
    def visitPlayNoteVar(self, ctx:jsbachParser.PlayNoteVarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#list_.
    def visitList_(self, ctx:jsbachParser.List_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#procDef.
    def visitProcDef(self, ctx:jsbachParser.ProcDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#proc.
    def visitProc(self, ctx:jsbachParser.ProcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#expr_bool.
    def visitExpr_bool(self, ctx:jsbachParser.Expr_boolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#Par.
    def visitPar(self, ctx:jsbachParser.ParContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#SumRes.
    def visitSumRes(self, ctx:jsbachParser.SumResContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#Mod.
    def visitMod(self, ctx:jsbachParser.ModContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#Var.
    def visitVar(self, ctx:jsbachParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#Note.
    def visitNote(self, ctx:jsbachParser.NoteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#Num.
    def visitNum(self, ctx:jsbachParser.NumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#ListGetLen.
    def visitListGetLen(self, ctx:jsbachParser.ListGetLenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#MultDiv.
    def visitMultDiv(self, ctx:jsbachParser.MultDivContext):
        return self.visitChildren(ctx)



del jsbachParser