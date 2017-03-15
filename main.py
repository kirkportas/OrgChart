#! /usr/bin/python
import csv
import sys

import organization
from organization import Department, Employee, departments


def load_csv(orgchart_filename, employees_filename):
    # TODO check for invalid filenames
    print("Loading orgchart file %s..." % orgchart_filename)
    with open(orgchart_filename, encoding='cp1250') as orgchart_file:
        orgchart_reader = csv.reader(orgchart_file, delimiter=';')
        # TODO skip empty rows
        for row in orgchart_reader:
            dept_id, parent_id, name, city = row
            # TODO verify correct CSV format
            dept_id = int(dept_id)
            if parent_id != '':
                parent_id = int(parent_id)
                # TODO check for non-existing parent_id
                organization.departments[parent_id].add_subdept(dept_id)
            organization.departments[dept_id] = Department(dept_id, parent_id, name, city)

    print("Loading employees file %s..." % employees_filename)
    with open(employees_filename, encoding='utf-8') as employees_file:
        employees_reader = csv.reader(employees_file, delimiter=';')
        for row in employees_reader:
            # TODO fix encoding
            employee_id, first_name, surname, dept_id, birth_date = row
            dept_id = int(dept_id)
            employee_id = int(employee_id)
            new_employee = Employee(employee_id, first_name, surname, dept_id, birth_date)
            organization.departments[dept_id].add_employee(new_employee)

    for department in organization.departments.values():
        print(department)


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