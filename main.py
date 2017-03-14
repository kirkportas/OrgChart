#! /usr/bin/python
import csv
import sys


class Department:
    _sub_depts = []
    _employees = []

    def __init__(self, dept_id, parent_id, name, city):
        assert isinstance(dept_id, int)
        assert isinstance(parent_id, int) or parent_id == ''

        self._dept_id = dept_id
        self._parent_id = parent_id if parent_id != '' else None
        self._name = name
        self._city = city

    def __repr__(self):
        return "%d (%s), %s, %s" % (self._dept_id, str(self._parent_id), self._name, self._city)

departments = {}


def load_csv(orgchart_filename, employees_filename):
    global departments
    # TODO check for invalid filenames
    print("Loading orgchart file %s..." % orgchart_filename)
    with open(orgchart_filename, encoding='cp1250') as orgchart_file:
        orgchart_reader = csv.reader(orgchart_file, delimiter=';')
        for row in orgchart_reader:
            dept_id, parent_id, name, city = row
            # TODO verify correct CSV format
            dept_id = int(dept_id)
            if parent_id != '':
                parent_id = int(parent_id)
            departments[dept_id] = Department(dept_id, parent_id, name, city)
            print(departments[dept_id])
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