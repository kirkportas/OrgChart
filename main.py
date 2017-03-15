#! /usr/bin/python
import csv
import datetime
import sys


class Department:
    def __init__(self, dept_id, parent_id, name, city):
        assert isinstance(dept_id, int)
        assert isinstance(parent_id, int) or parent_id == ''

        self._dept_id = dept_id
        self._parent_id = parent_id if parent_id != '' else None
        self._name = name
        self._city = city
        self._sub_depts = []
        self._employees = []

    def __repr__(self):
        representation = "[%d (%s), %s, %s]" % (self._dept_id, str(self._parent_id), self._name, self._city)
        if self._sub_depts:
            representation += " [sub_depts: " + ' '.join([str(sub_dept) for sub_dept in self._sub_depts]) + "]"
        if self._employees:
            representation += " [employees: " +\
                              ' '.join([str(employee._employee_id) + "(" + str(employee.get_age) + ")"
                                        for employee in self._employees]) + "]"
        return representation

    def add_subdept(self, sub_dept_id):
        if sub_dept_id not in self._sub_depts:
            self._sub_depts.append(sub_dept_id)

    def display_department(self):
        print("%s, %s" % (self._name, self._city))

    def add_employee(self, employee):
        if employee not in self._employees:
            self._employees.append(employee)

    def count_employees(self):
        count = len(self._employees)
        for sub_dept_id in self._sub_depts:
            count += departments[sub_dept_id].count_employees()
        return count

    def get_employees(self):
        '''
        :return: a list of employees' names
        '''
        list_of_employees = [employee._first_name + ' ' + employee._surname for employee in self._employees]
        for sub_dept_id in self._sub_depts:
            list_of_employees.extend(departments[sub_dept_id].get_employees())
        return list_of_employees


class Employee:
    def __init__(self, employee_id, first_name, surname, dept_id, birth_date):
        assert isinstance(dept_id, int)
        assert isinstance(employee_id, int)

        self._employee_id = employee_id
        self._first_name = first_name
        self._surname = surname
        self._dept_id = dept_id
        self._birth_date = birth_date

    def get_age(self):
        '''
        :return: the integer age of the employee as of today
        '''
        today = datetime.date.today()
        born = datetime.datetime.strptime(self._birth_date, '%d.%m.%Y').date()
        age = today.year - born.year
        if (today.month, today.day) < (born.month, born.day):
            age -= 1
        return age


departments = {}


def load_csv(orgchart_filename, employees_filename):
    global departments

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
                departments[parent_id].add_subdept(dept_id)
            departments[dept_id] = Department(dept_id, parent_id, name, city)

    print("Loading employees file %s..." % employees_filename)
    with open(employees_filename, encoding='utf-8') as employees_file:
        employees_reader = csv.reader(employees_file, delimiter=';')
        for row in employees_reader:
            # TODO fix encoding
            employee_id, first_name, surname, dept_id, birth_date = row
            dept_id = int(dept_id)
            employee_id = int(employee_id)
            new_employee = Employee(employee_id, first_name, surname, dept_id, birth_date)
            departments[dept_id].add_employee(new_employee)

    for department in departments.values():
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
            # TODO implement Avgage
            print("Average age of employees in department %d" % dept_id)
        else:
            print("Invalid command!")
            # TODO help message with list of commands

if __name__ == "__main__":
    main()