from django.test import TestCase
from core.models import Contact, AboutUs

class ContactModelTest(TestCase):
    """Test module for Contact model"""

    def setUp(self):
        self.data1 = Contact.objects.create(
            name_and_surname='John Doe',
            email_address = 'admin@admin.com',
            text = 'This is a test'
        )
        self.data2 = Contact.objects.create(
            name_and_surname='Jane Doe',
            email_address = 'admin2@admin.com',
            text = 'This is a test'
        )


    def test_contact(self):
        self.assertEqual(self.data1.name_and_surname, 'John Doe')
        self.assertEqual(self.data1.email_address, 'admin@admin.com')
        self.assertEqual(self.data1.text, 'This is a test')


    def test_str(self):
        self.assertEqual(str(self.data1), 'John Doe')
        self.assertEqual(str(self.data2), 'Jane Doe')


    def tearDown(self):
        del self.data1
        del self.data2


class AboutUsModelTest(TestCase):
    """Test module for AboutUs model"""

    def setUp(self):
        self.data1 = AboutUs.objects.create(
            title='John Doe',
            text = 'This is a test'
        )
        self.data2 = AboutUs.objects.create(
            title='Jane Doe',
            text = 'This is a test'
        )


    def test_contact(self):
        self.assertEqual(self.data1.title, 'John Doe')
        self.assertEqual(self.data1.text, 'This is a test')


    def test_str(self):
        self.assertEqual(str(self.data1), 'John Doe')
        self.assertEqual(str(self.data2), 'Jane Doe')


    def tearDown(self):
        del self.data1
        del self.data2