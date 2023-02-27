from django.test import TestCase
from core.forms import ContactForm, SubscriberForm
from core.models import Contact, AboutUs, Subscriber

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


class ContactFormTest(TestCase):

    def setUp(self):
        self.valid_form = ContactForm(
            data = {
                'name_and_surname': 'Nathan Ake',
                'email_address': 'nathanake@gmail.com',
                'text': 'lorem ipsum Manchester City',
            }
        )

        self.invalid_form = ContactForm(
            data={
                'name_and_surname': 123,
                'email_address': 'nathanakegmail.com',
                'text': 1,
            }
        )

    def test_valid_form(self):
        self.assertTrue(self.valid_form.is_valid())
    
    def test_invalid_form(self):
        self.assertFalse(self.invalid_form.is_valid())
    
    def tearDown(self):
        del self.valid_form
        del self.invalid_form


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


class SubscriberModelTest(TestCase):
    """Test module for Subscriber model"""

    def setUp(self):
        self.data1 = Subscriber.objects.create(
            email='nurlan@gmail.com',
        )
        self.data2 = Subscriber.objects.create(
            email='Jane Doe',
        )


    def test_subscriber(self):
        self.assertEqual(self.data1.email, 'nurlan@gmail.com')


    def test_str(self):
        self.assertEqual(str(self.data1), 'nurlan@gmail.com')


    def tearDown(self):
        del self.data1


class SubscriberFormTest(TestCase):

    def setUp(self):
        self.valid_form = SubscriberForm(
            data = {
                'email': 'nathanake@gmail.com',
            }
        )

        self.invalid_form = SubscriberForm(
            data={
                'email': 'nathanakegmail.com',
            }
        )

    def test_valid_form(self):
        self.assertTrue(self.valid_form.is_valid())
    
    def test_invalid_form(self):
        self.assertFalse(self.invalid_form.is_valid())
    
    def tearDown(self):
        del self.valid_form
        del self.invalid_form

