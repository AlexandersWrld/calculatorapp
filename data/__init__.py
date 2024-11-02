import pandas as pd

class appData:
    
    history = pd.DataFrame(columns=['Operation', 'Number 1', 'Number 2', 'Result'])

    @classmethod
    def add_record(cls, operation, num1, num2, num3):
        new_row = pd.DataFrame({'Operation': [operation], 'Number 1': [num1], 'Number 2': [num2], 'Result': [num3]})
        cls.history = pd.concat([cls.history, new_row], ignore_index=True)
        cls.history.to_csv('appdata.csv', index=False)

    @classmethod
    def retrieve_history(cls):
        return cls.history
        