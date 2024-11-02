import sys
from app.commands import Command


class MenuCommand(Command):
    def execute(self):
        print(f'Welcome to the Calulator App')
        print(f'Simply enter add, subtract, divide or multiply to begin')
        print(f'Past calculattions may be viewed by entering: history')
        print(f'You may also search previous calculations by simply entering search or last (returning the last calculation)')

