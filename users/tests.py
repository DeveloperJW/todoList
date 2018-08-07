from django.test import TestCase, SimpleTestCase

# Create your tests here.


class SimpleUserTest(SimpleTestCase):
    # Test if proper url directs to the correct login and registeration page
    def test_login_page_status_code(self):
        response = self.client.get('/users/login/')
        self.assertEqual(response.status_code, 200)

    def test_register_page_status_code(self):
        response = self.client.get('/users/register/')
        self.assertEqual(response.status_code, 200)

