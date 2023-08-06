import sys
import subprocess
import shlex
from pathlib import Path
import json


def run_command(command: str, std_output=False):
    """
    run command using subprocess and return exit code
    """
    command = shlex.split(command)
    if std_output:
        return_data = subprocess.run(command, stderr=sys.stderr, stdout=sys.stdout)
    else:
        return_data = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    return return_data


def create_config(file: Path = Path().home() / 'gitswitch.json', accounts=None, current_user=None) -> None:
    """
    create a config json file in given path
    """
    if accounts is None:
        accounts = []
    accounts = {
        'accounts': accounts,
        'current_user': current_user
    }
    file.write_text(json.dumps(accounts, ensure_ascii=False, indent=2), encoding="utf-8")


def get_accounts(file: Path = Path().home() / 'gitswitch.json') -> list:
    try:
        return json.loads(file.read_text())['accounts']
    except FileNotFoundError:
        print(f"Config file {file} not found. Did you run \"gitswitch init\" yet?")
        sys.exit(-1)


def get_current_user(file: Path = Path().home() / 'gitswitch.json'):
    try:
        return json.loads(file.read_text())['current_user']
    except FileNotFoundError:
        print(f"Config file {file} not found. Did you run \"gitswitch init\" yet?")
        sys.exit(-1)

# ToDo: add a function to create windows shortcuts for each account to switch to
