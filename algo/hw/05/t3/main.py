import sys 
from colorama import Fore, init
from logs_.log_handler import load_logs, count_logs_by_level, display_log_counter, filter_logs_by_level, parse_log_line

def main():
    if len(sys.argv) == 2:
        file_path = sys.argv[1]
        logs = load_logs(file_path)
        count = count_logs_by_level(logs)
        display_log_counter(count)
    elif len(sys.argv) == 3:
        file_path = sys.argv[1]
        level = sys.argv[2]
        count = count_logs_by_level(logs)
        display_log_counter(count)
        print(filter_logs_by_level(logs, level))
    else:
        print('Incorrect provide values!')
        return

if __name__ == '__main__':
    main()