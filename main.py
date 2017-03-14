#! /usr/bin/python
import csv
import sys


def load_csv(orgchart_filename, employees_filename):
    # TODO check for invalid filenames
    print("Loading orgchart file %s..." % orgchart_filename)
    with open(orgchart_filename, encoding='cp1250') as orgchart_file:
        orgchart_reader = csv.reader(orgchart_file, delimiter=';')
        for row in orgchart_reader:
            print(', '.join(row))
    print("Loading employees file %s..." % employees_filename)
    with open(employees_filename, encoding='cp1250') as employees_file:
        employees_reader = csv.reader(employees_file, delimiter=';')
        for row in employees_reader:
            print('. '.join(row))
    return


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
    load_csv(orgchart_filename, employees_filename)
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
            # TODO implement Department
            print("Show department %d" % dept_id)
        elif command.startswith("Count"):
            # TODO implement Count
            print("Count employees in department %d" % dept_id)
        elif command.startswith("People"):
            # TODO implement People
            print("Employees of department %d" % dept_id)
        elif command.startswith("Avgage"):
            # TODO implement Avgage
            print("Average age of employees in department %d" % dept_id)
        else:
            print("Invalid command!")
            # TODO help message with list of commands

if __name__ == "__main__":
    main()