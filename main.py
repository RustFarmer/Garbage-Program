import os
import subprocess
import sys
import hashlib
import string
import random
from loguru import logger
from pathlib import Path


def generate(length: int = 10) -> str:
    letters = string.ascii_letters
    return "".join(random.choice(letters) for _ in range(length))


def delete_specific_files(target_directory: str):
    path = Path(target_directory)

    if not path.exists() or not path.is_dir():
        print(f"ERROR: NOT FOUND PATH '{target_directory}'.")
        return

    extensions_to_delete = {"._f4_f4g", ".dll"}
    deleted_count = 0

    for file_path in path.rglob("*"):
        if file_path.is_file() and file_path.suffix.lower() in extensions_to_delete:
            try:
                file_path.unlink()
                print(f"┤├ ┤\h|/╎┌├R3d┼┼┌wr┤┼ {file_path.name}")
                deleted_count += 1
            except Exception as e:
                print(f"NOT DELL {file_path.name}: {e}")


class DataBase:
    Intcount = None

    def __init__(self):
        self.Intcount = None

    def hell_work_in_database(self):
        for x in range(20):
            logger.error('█├┌├╓╢┤ ╢╵╵╓┘ ├╢┘╵╢┌', hashlib.sha256(sys.version.encode('utf-8')).hexdigest().encode('utf-8'))

        if sys.platform == "win32":
            logger.warning("╎┤├┼ ╎┌ ┼┘├ ┌┼├█╓╵├┤┼┘┌ \n")
        elif sys.platform == "linux":
            logger.warning("█├┌├╓╢┤ ╢╵╵╓┘ ├╢┘╵╢┌ \n")
        elif sys.platform == "darwin":
            logger.warning("╎┤┼╎├├ ├┤┼ ╵╢├┤┌ \n")

        print(f"С╵╎┤├┼ ╎┼┌╎█├ ├┤┼ ╓├┼┤┼ {hashlib.sha256(sys.executable.encode('utf-8')).hexdigest()}")
        print(self.Intcount)
        try:
            with open('databasefileDontdellet.txt', 'w+', encoding='utf-8') as file:
                file.write(self.Intcount)
                print(type(self.Intcount), '38---')
                try:
                    if int(self.Intcount):
                        logger.critical('NOT ERROR: YOU WRITE CORRECT COUNT')
                except ValueError:
                    logger.critical('ERROR: WRITE INT COUNT')
                    ScreenMain().hellow_screen()
        except FileNotFoundError:
            logger.error('FILE NOT FOUND')

        try:
            for x in range(2):
                logger.info('-----------------------')
                Path(f"{generate()}.dll").touch()
                Path(f"{generate()}._f4_f4g").touch()
        except ImportError:
            print('fuck me')

        try:
            result = subprocess.run(["CppMain.exe"], capture_output=True, text=True, encoding="utf-8")
            print(result.stdout, '┤┼╎├├┤┼╎├├xc ├j┤┼ ╵╢├=r ├┤┼ ╵╢├')
        except FileNotFoundError:
            logger.critical('ERROR FILE CppMain.exe NOT FOUND')

        return ScreenMain().hellow_screen()

    def start_work_database(self):
        print("it's syper mega top database in the word")
        print('-' * 10, "lets GOOOOOOOOOO", '-' * 10)
        self.Intcount = str(input("write you're int count: "))
        self.hell_work_in_database()
        return str(self.Intcount)


class ScreenMain:
    def __init__(self):
        self.takeProgramUser = None

    def hellow_screen(self):
        print('''Hi, you've entered the divinenoob program written in Python and C++.''')
        print('''I suggest you choose from several categories what you can use in it.''')
        self.takeProgramUser = input(
                '''1. Uses top database for save int count \n2. Close program \n3. Encrypt an int value \nWrite number: '''
                )
        self.start_program()
        return self.takeProgramUser

    def start_program(self):
        print(type(self.takeProgramUser))
        match self.takeProgramUser:
            case '1':
                dt = DataBase()
                dt.start_work_database()
            case '2':
                logger.critical('NOT CREATE GO TO HELL DATA BASE')
                ScreenMain().hellow_screen()
            case '3':
                script_dir = os.path.dirname(os.path.abspath(__file__))
                delete_specific_files(script_dir)
                exit(print('FINAL'))
            case _:
                return ValueError, ScreenMain().hellow_screen()


if __name__ == '__main__':
    sc = ScreenMain()
    sc.hellow_screen()
