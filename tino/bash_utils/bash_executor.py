import subprocess


def format_commands(options):
    return ';'.join(options)


def add_logging_to_commands(raw_commands):
    _commands = []
    for scriptlet in raw_commands:
        _commands.append('echo -e "${GREEN}' + scriptlet + '${NC}"')
        _commands.append(scriptlet + "")

    return _commands


def exec_commands(commands):
    p1 = subprocess.Popen(['/bin/bash', '-c', commands])
    p1.wait()


def execute_script(variable_values, commands):
    colour_commands = [
        "GREEN='\\033[0;32m'",
        "NC='\\033[0m'"]

    variable_commands = []
    for variableName, variableValue in variable_values.items():
        variable_commands.append(variableName + '="' + str(variableValue) + '"')

    commands_with_logging = add_logging_to_commands(variable_commands + commands)
    commands_in_single_string = format_commands(colour_commands + commands_with_logging)

    exec_commands(commands_in_single_string)
