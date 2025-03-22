# Generated from Scheduler.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SchedulerParser import SchedulerParser
else:
    from SchedulerParser import SchedulerParser

# This class defines a complete listener for a parse tree produced by SchedulerParser.
class SchedulerListener(ParseTreeListener):

    # Enter a parse tree produced by SchedulerParser#command.
    def enterCommand(self, ctx:SchedulerParser.CommandContext):
        pass

    # Exit a parse tree produced by SchedulerParser#command.
    def exitCommand(self, ctx:SchedulerParser.CommandContext):
        pass


    # Enter a parse tree produced by SchedulerParser#setEventCmd.
    def enterSetEventCmd(self, ctx:SchedulerParser.SetEventCmdContext):
        pass

    # Exit a parse tree produced by SchedulerParser#setEventCmd.
    def exitSetEventCmd(self, ctx:SchedulerParser.SetEventCmdContext):
        pass


    # Enter a parse tree produced by SchedulerParser#getScheduleCmd.
    def enterGetScheduleCmd(self, ctx:SchedulerParser.GetScheduleCmdContext):
        pass

    # Exit a parse tree produced by SchedulerParser#getScheduleCmd.
    def exitGetScheduleCmd(self, ctx:SchedulerParser.GetScheduleCmdContext):
        pass


    # Enter a parse tree produced by SchedulerParser#getDateCmd.
    def enterGetDateCmd(self, ctx:SchedulerParser.GetDateCmdContext):
        pass

    # Exit a parse tree produced by SchedulerParser#getDateCmd.
    def exitGetDateCmd(self, ctx:SchedulerParser.GetDateCmdContext):
        pass


    # Enter a parse tree produced by SchedulerParser#time.
    def enterTime(self, ctx:SchedulerParser.TimeContext):
        pass

    # Exit a parse tree produced by SchedulerParser#time.
    def exitTime(self, ctx:SchedulerParser.TimeContext):
        pass


    # Enter a parse tree produced by SchedulerParser#date.
    def enterDate(self, ctx:SchedulerParser.DateContext):
        pass

    # Exit a parse tree produced by SchedulerParser#date.
    def exitDate(self, ctx:SchedulerParser.DateContext):
        pass



del SchedulerParser