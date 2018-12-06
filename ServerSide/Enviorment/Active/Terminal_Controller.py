#------------------SUMARY-------------------#
#The purpose of this module is to gather
#user input from the terminal,
#parse it into to actionable commands
#then spin up an executioner
#-------------------------------------------#

import queue


class Command_Info:
    def __init__(self, command, help_tip, post_report):
        self.command = command
        self.help_tip = help_tip
        self.post_report = post_report


Help_Message = "Unrecognized Command Input. Commands are not case-sensative. Enter ""help"" for a list of commands." #Displayed when an improper command is entered
Execution_Queue = queue.Queue()
Commands = {}

#Terminal Command Definitions
#Help Command
def command_help(arguments=None):
    print("*------------------------------------------*")
    print("Void Scribe Terminal Commands:")
    for command_name in Commands.keys():
        print(command_name + " - " + Commands[command_name].help_tip)
    print("*------------------------------------------*")
help_tip_help = "Displays all commands and what they do."
def post_report_help():
    return None

#Public Interface
def AddTerminalCommand(command_name, command, help_tip, post_report):
    if command_name in Commands.keys():
        raise KeyError(f"Commands Name {command_name} already exists in commands list.")

    Commands[command_name.lower()] = Command_Info(command, help_tip, post_report)

def InputEntryPoint():
    AddTerminalCommand("help", command_help, help_tip_help, post_report_help)

    while True:
        terminal_input = input()

        if terminal_input.split(' ', 1)[0].lower() not in Commands.keys():
            print(Help_Message)
            continue

        Execution_Queue.put(terminal_input)

def ExecutionerEntryPoint():

    shut_down = False
    def Shutdown_Executioner():
        nonlocal shut_down
        shut_down = True
    from Main import AddShutDownProcess
    AddShutDownProcess(Shutdown_Executioner)

    while True:

        if shut_down:
            break

        try:
            terminal_input = Execution_Queue.get(timeout=1/10)
        except:
            continue

        terminal_input = terminal_input.split(' ')
        command = terminal_input[0].lower()
        terminal_input.pop(0)
        arguments = terminal_input
        result = Commands[command].command(arguments)

        if result != None:
            Commands[command].post_report(result)
        else:
            Commands[command].post_report()
        