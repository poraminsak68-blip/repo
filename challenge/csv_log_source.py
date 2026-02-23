import csv
from ilog_source import ILogSource

class CsvLogSource(ILogSource):

    def __init__(self, filename):
        self.filename = filename

    def read_logs(self):
        logs = []
        with open(self.filename, newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                logs.append(row)
        return logs