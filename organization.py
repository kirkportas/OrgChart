import csv
import datetime
import sys


class Organization:
    def __init__(self):
        self._departments = {}

    def get_departments(self):
        return self._departments

    def load_csv(self, orgchart_filename, employees_filename):
        try:
            print("Loading orgchart file %s..." % orgchart_filename)
            self.load_departments_csv(orgchart_filename)
        except OSError:
            print("Can't open file %s!" % orgchart_filename)
            sys.exit(1)
        try:
            print("Loading employees file %s..." % employees_filename)
            self.load_employees_csv(employees_filename)
        except OSError:
            print("Can't open file %s!" % employees_filename)
            sys.exit(1)
        for department in self._departments.values():
            print(department)

    def load_departments_csv(self, orgchart_filename):
        with open(orgchart_filename, encoding='cp1250') as orgchart_file:
            orgchart_reader = csv.reader(orgchart_file, delimiter=';')
            for row in orgchart_reader:
                if not row:               # skip empty rows
                    continue
                try:
                    dept_id, parent_id, name, city = row
                    dept_id = int(dept_id)
                    if parent_id != '':
                        parent_id = int(parent_id)
                        if parent_id not in self._departments:
                            self._departments[parent_id] = Department.from_dept_id(self, parent_id)
                        self._departments[parent_id].add_subdept(dept_id)
                except ValueError:
                    print("Wrong format in %s!" % orgchart_filename)
                    sys.exit(2)
                existing_sub_depts = []                     # backup self._departments to copy to a new instance
                if dept_id in self._departments:
                    existing_sub_depts = self._departments[dept_id].get_sub_depts()[:]
                self._departments[dept_id] = Department.from_CSV_row(self, dept_id, parent_id, name, city)
                for sub_dept_id in existing_sub_depts:
                    self._departments[dept_id].add_subdept(sub_dept_id)


    def load_employees_csv(self, employees_filename):
        with open(employees_filename, encoding='utf-8') as employees_file:
            employees_reader = csv.reader(employees_file, delimiter=';')
            for row in employees_reader:
                if not row:               # skip empty rows
                    continue
                try:
                    employee_id, first_name, surname, dept_id, birth_date = row
                    dept_id = int(dept_id)
                    employee_id = int(employee_id)
                except ValueError:
                    print("Wrong format in %s!" % employees_filename)
                    sys.exit(3)
                # TODO fix encoding
                new_employee = Employee(employee_id, first_name, surname, dept_id, birth_date)
                self._departments[dept_id].add_employee(new_employee)


class Department:
    def __init__(self, organization, dept_id, parent_id, name, city):
        self._organization = organization
        self._dept_id = dept_id
        self._parent_id = parent_id if parent_id != '' else None
        self._name = name
        self._city = city
        self._sub_depts = []
        self._employees = []

    @classmethod
    def from_CSV_row(cls, organization, dept_id, parent_id, name, city):
        assert isinstance(dept_id, int)
        assert isinstance(parent_id, int) or parent_id == ''

        dept = cls(organization, dept_id, parent_id, name, city)
        dept._parent_id = parent_id if parent_id != '' else None
        return dept

    @classmethod
    def from_dept_id(cls, organization, dept_id):
        dept = cls(organization, dept_id, None, None, None)
        return dept

    def __repr__(self):
        representation = "[%d (%s), %s, %s]" % (self._dept_id, str(self._parent_id), self._name, self._city)
        if self._sub_depts:
            representation += " [sub_depts: " + ' '.join([str(sub_dept) for sub_dept in self._sub_depts]) + "]"
        if self._employees:
            representation += " [employees: " +\
                              ' '.join([str(employee._employee_id) + " (age " + str(employee.get_age()) + ")"
                                        for employee in self._employees]) + "]"
        return representation

    def add_subdept(self, sub_dept_id):
        if sub_dept_id not in self._sub_depts:
            self._sub_depts.append(sub_dept_id)

    def get_sub_depts(self):
        return self._sub_depts

    def display_department(self):
        print("%s, %s" % (self._name, self._city))

    def add_employee(self, employee):
        if employee not in self._employees:
            self._employees.append(employee)

    def count_employees(self):
        count = len(self._employees)
        for sub_dept_id in self._sub_depts:
            count += self._organization._departments[sub_dept_id].count_employees()
        return count

    def get_employees(self):
        '''
        :return: a list of employees' names
        '''
        list_of_employees = [employee._first_name + ' ' + employee._surname for employee in self._employees]
        for sub_dept_id in self._sub_depts:
            list_of_employees.extend(self._organization._departments[sub_dept_id].get_employees())
        return list_of_employees

    def sum_age(self):
        sum = 0
        for employee in self._employees:
            sum += employee.get_age()
        for sub_dept in self._sub_depts:
            sum += self._organization._departments[sub_dept].sum_age()
        return sum

    def avg_age(self):
        '''
        :return: the average age of employees in the department and its subdepartments
        '''
        sum_age = self.sum_age()
        count = self.count_employees()
        average = sum_age / count if count != 0 else 0
        return average


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
