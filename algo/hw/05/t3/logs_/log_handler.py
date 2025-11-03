from pathlib import Path
from collections import Counter

def parse_log_line(line: str) -> dict:
    line = line.split(" ", 3)
    log = {'data': line[0], 'time': line[1], 'level': line[2], 'info': line[3]}
    return log

def load_logs(file_path: str) -> list:
    logs = []
    with open(Path(file_path), "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line:
                logs.append(parse_log_line(line))
    return logs

def filter_logs_by_level(logs: list, level: str) -> list:
    return list(filter(lambda log: log['level'] == level.upper(), logs))


def count_logs_by_level(logs: list) -> dict:
    return Counter(log['level'] for log in logs)

def display_log_counter(counts: dict):
    print("Level of log | Quality")
    print("-------------|--------")
    for level, count in counts.items():
        print(f"{level:<13} | {count}")