from app.commands import Command
import sys
sys.path.append('../../IS218_HW3_revised')
from data import appData

class HistoryCommand(Command):
    
    def execute(self):
        # appHistory = Calculator.getHistory()
        # print(appHistory)
        appHistory = appData.retrieve_history()
        print(appHistory)