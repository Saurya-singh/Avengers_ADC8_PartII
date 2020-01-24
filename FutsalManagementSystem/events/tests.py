from django.test import TestCase
from .models import *
# Create your tests here.
class EventsModelTestCase(TestCase):
    def test_Payment_name_null_check(self):
        Payment1= Payment.objects.create(team_name="SWAT", duration=1, charge=1500, bill="bill number")
        self.assertTrue(Payment1.Payment_name_null_check())


    def test_Staff_name_null_check(self):
        Staff1= Staff.objects.create(contact=9815267681, name="Ronit", address="Thapathali")
        self.assertTrue(Staff1.Staff_name_null_check())

    def test_Staff_name_null_check_f(self):
        Staff4= Staff.objects.create(contact=9815267681, name="", address="Thapathali")
        self.assertFalse(Staff4.Staff_name_null_check_f())

    def test_Staff_name_namecount_check(self):
        Staff2= Staff.objects.create(contact=9815267634, name="Ronita", address="Thapathalika")
        self.assertEqual(Staff2.Staff_name_namecount_check(),1)

    def test_Staff_name_namecount_check_n(self):
        Staff5= Staff.objects.create(contact=9815267634, name="Roni", address="Thapathalika")
        self.assertNotEqual(Staff5.Staff_name_namecount_check_n(),-1)
