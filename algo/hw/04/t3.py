import sys
from pathlib import Path
from colorama import Fore, Style

def show_directory(path, indent=0):
    try:
        directory = Path(path).resolve()

        if not directory.exists():
            print(f"{Fore.RED} Error: Path {directory} not exist!")
            return
        if not directory.is_dir():
            print(f"{Fore.RED} Error: {directory} is not a directory!")
            return
        
        for item in directory.iterdir():
            indent_str = " " * indent

            if item.is_dir():
                print(f"{indent_str}{Fore.BLUE}📂 {item.name}{Style.RESET_ALL}")
                show_directory(item, indent + 1)
            else:
                print(f"{indent_str}{Fore.GREEN}📜 {item.name}{Style.RESET_ALL}")
        
    except PermissionError:
        print(f"{Fore.RED} Error: not access to {path}")
    except Exception as e:
        print(f"{Fore.RED} There was an error: {str(e)}")

def main():
    if len(sys.argv) != 2:
        print(f"{Fore.RED} Error: Specify the path to the directory!")
        sys.exit(1)

    path = sys.argv[1]
    print(f"Directory structure: {path}")
    show_directory(path)

if __name__ == "__main__":
    main()