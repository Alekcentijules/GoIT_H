from collections import namedtuple

def parse_log_line(line: str) -> dict:
    line = line.split(" ")
    log = {'data': line[0], 'time': line[1], 'level': line[2], 'info': line[3]}
    return log

def load_logs(file_path: str) -> list:
    
    pass

def filter_logs_by_level(logs: list, level: str) -> list:
    pass

def count_logs_by_level(logs: list) -> dict:
    pass

def display_log_counter(counts: dict):
    pass