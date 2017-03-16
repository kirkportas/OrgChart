#! /usr/bin/python
import sys

import organization


def get_int(command):
    args = command.split()
    if len(args) != 2:
        return None
    try:
        return int(command.split()[1])
    except ValueError:
        return None


def main():
    list_of_commands = ["Exit", "Department", "Count", "People", "Avgage"]
    if len(sys.argv) < 3:
        print("Not enough arguments!")
        return 1
    orgchart_filename = sys.argv[1]
    employees_filename = sys.argv[2]
    org = organization.Organization()
    org.load_csv(orgchart_filename, employees_filename)
    departments = org.get_departments()
    while True:
        command_with_arg = input("User command: ")
        if not command_with_arg:
            continue
        command = command_with_arg.split()[0]
        if command not in list_of_commands:
            print("Invalid command! Supported commands: " + ', '.join(list_of_commands))
            continue
        if command not in ["Exit"]:                         # hack: for commands with 1 number argument
            dept_id = get_int(command_with_arg)
            if dept_id is None:
                print("Invalid number argument!")
                continue
            elif dept_id not in org.get_departments().keys():
                print("Invalid department ID!")
                continue
        if command == "Exit":
            break
        elif command == "Department":
            departments[dept_id].display_department()
        elif command == "Count":
            print(departments[dept_id].count_employees())
        elif command == "People":
            print(', '.join(departments[dept_id].get_employees()))
        elif command == "Avgage":
            print(departments[dept_id].avg_age())

if __name__ == "__main__":
    main()