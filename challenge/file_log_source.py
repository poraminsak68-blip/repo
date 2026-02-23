from ilog_source import ILogSource

class FileLogSource(ILogSource):

    def __init__(self, filename):
        self.filename = filename

    def read_logs(self):
        with open(self.filename, encoding="utf-8") as file:
            return file.readlines()   