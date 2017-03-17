# OrgChart
Python demo for manipulating database of departments and employees

Requirements
------------

Install requirements by
```
pip3 install -r requirements.txt
```

Input arguments
---------------

The program will take two input arguments = two files.
- First file contains company orgchart data
- Second file contains employees data

```
$ python3 orgchart.py orgchart-data.csv employees-data.csv
```
It will load the data from two files into a memory, wait in a loop for user input commands and display corresponding
results.

Commands
--------

Command 1 – Display the department name and the city for given department ID

- User command: Department 5
- Output example: Testing, Praha


Command 2 – Number of all employees for department INCLUDING all employees for department
INCLUDING all its sub-departments (all levels, for example for Delivery it includes also Development,
Python, Java) - for given department ID

- User command: Count 1
- Output example: 25

Command 3 – List of names of all employees for department INCLUDING all its sub-departments (all
levels, for example for Delivery it includes also Development, Python, Java) - for given department ID

- User command: People 1
- Output example: Jan Hora, Jiří Vereš

Command 4 – Average age of all employees for department INCLUDING all its sub-departments (all
levels, for example for Delivery it includes also Development, Python, Java) - for given department ID

- User command: Avgage 1
- Output example: 28 years


License
-------
OrgChart is **licensed** under the **[MIT License]**. The terms of the license are as follows:

    MIT License

    Copyright (c) 2017 Karel Ha

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.

[MIT License]: https://github.com/mathemage/OrgChart/raw/master/License.md