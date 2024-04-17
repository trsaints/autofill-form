from autofill import autofill
from csv_parser import parse_commands


def initialize():
    commands = parse_commands("commands.csv")

    autofill(commands)

initialize()