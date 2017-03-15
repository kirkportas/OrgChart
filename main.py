#! /usr/bin/python
import sys

import organization


def get_int(command):
    args = command.split()
    if len(args) != 2:
        return None
    try:
        # TODO check for valid range of id_dept
        return int(command.split()[1])
    except ValueError:
        return None


def main():
    if len(sys.argv) < 3:
        print("Not enough arguments!")
        return 1
    orgchart_filename = sys.argv[1]
    employees_filename = sys.argv[2]
    org = organization.Organization()
    org.load_csv(orgchart_filename, employees_filename)
    departments = org._departments
    while True:
        command = input("User command: ")
        # TODO check for invalid commands
        if command == "Exit":
            break

        dept_id = get_int(command)
        if dept_id is None:
            # TODO show this error only in combination with a valid command
            print("Invalid number argument!")
            continue

        if command.startswith("Department"):
            departments[dept_id].display_department()
        elif command.startswith("Count"):
            print(departments[dept_id].count_employees())
        elif command.startswith("People"):
            print(', '.join(departments[dept_id].get_employees()))
        elif command.startswith("Avgage"):
            print(departments[dept_id].avg_age())
        else:
            print("Invalid command!")
            # TODO help message with list of commands

if __name__ == "__main__":
    main()