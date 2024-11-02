from app.commands import Command
import sys
from data import appData

class SearchCommand(Command):

    def execute(self):
        type = str(input("Enter the type of operation you wish to view instances of "))
        searchResult = appData.search_by_type(type)
        print(searchResult)
        