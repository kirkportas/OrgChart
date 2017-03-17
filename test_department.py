import datetime
import unittest

from dateutil.relativedelta import relativedelta

import organization


class TestDepartmentSampleFromThreatMark(unittest.TestCase):
    def setUp(self):
        org = self._sample_organization = organization.Organization()
        org.load_csv("orgchart-data.csv", "employees-data.csv")

    def test_display_department(self):
        org = self._sample_organization
        self.assertEqual(org.get_departments()[1].get_department_name_location(), "Delivery, Brno")
        self.assertEqual(org.get_departments()[2].get_department_name_location(), "Support, Brno")
        self.assertEqual(org.get_departments()[3].get_department_name_location(), "Marketing, Praha")
        self.assertEqual(org.get_departments()[4].get_department_name_location(), "Backoffice, Praha")
        self.assertEqual(org.get_departments()[5].get_department_name_location(), "Testing, Praha")
        self.assertEqual(org.get_departments()[6].get_department_name_location(), "Development, Brno")
        self.assertEqual(org.get_departments()[7].get_department_name_location(), "Python, Brno")
        self.assertEqual(org.get_departments()[8].get_department_name_location(), "Java, Brno")

    def test_count_employees(self):
        org = self._sample_organization
        self.assertEqual(org.get_departments()[1].count_employees(), 2)
        self.assertEqual(org.get_departments()[2].count_employees(), 0)
        self.assertEqual(org.get_departments()[3].count_employees(), 0)
        self.assertEqual(org.get_departments()[4].count_employees(), 0)
        self.assertEqual(org.get_departments()[5].count_employees(), 1)
        self.assertEqual(org.get_departments()[6].count_employees(), 1)
        self.assertEqual(org.get_departments()[7].count_employees(), 1)
        self.assertEqual(org.get_departments()[8].count_employees(), 0)

    def test_get_employees_names(self):
        org = self._sample_organization
        self.assertListEqual(org.get_departments()[1].get_employees_names(), ["Jiří Vereš", "Jan Hora"])
        self.assertListEqual(org.get_departments()[2].get_employees_names(), [])
        self.assertListEqual(org.get_departments()[3].get_employees_names(), [])
        self.assertListEqual(org.get_departments()[4].get_employees_names(), [])
        self.assertListEqual(org.get_departments()[5].get_employees_names(), ["Jiří Vereš"])
        self.assertListEqual(org.get_departments()[6].get_employees_names(), ["Jan Hora"])
        self.assertListEqual(org.get_departments()[7].get_employees_names(), ["Jan Hora"])
        self.assertListEqual(org.get_departments()[8].get_employees_names(), [])

    def test_avg_age(self):
        org = self._sample_organization
        today = datetime.date.today()
        birthday_jiri = datetime.date(1986, 8, 20)
        birthday_jan = datetime.date(1994, 3, 12)
        age_jiri = relativedelta(today, birthday_jiri).years
        age_jan = relativedelta(today, birthday_jan).years
        self.assertEqual(org.get_departments()[5].avg_age(), age_jiri)
        self.assertEqual(org.get_departments()[6].avg_age(), age_jan)
        self.assertAlmostEqual(org.get_departments()[1].avg_age(), (age_jan + age_jiri) / 2.0, delta=0.5)

if __name__ == "__main__":
    unittest.main()
