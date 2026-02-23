from file_log_source import FileLogSource
from csv_log_source import CsvLogSource

class LogSourceFactory:

    @staticmethod
    def create(source_type, filename):

        if source_type == "file":
            return FileLogSource(filename)

        elif source_type == "csv":
            return CsvLogSource(filename)

        else:  
            raise ValueError("Unknown source type")