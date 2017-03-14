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


def main():
    if len(sys.argv) < 3:
        print("Not enough arguments!")
        return 1
    orgchart_filename = sys.argv[1]
    employees_filename = sys.argv[2]
    load_csv(orgchart_filename, employees_filename)


if __name__ == "__main__":
    main()