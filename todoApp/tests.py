from django.test import TestCase, SimpleTestCase
from django.urls import reverse
from .models import List

# Create your tests here.


class SimpleTest(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        # since we require login before accessing home page
        # redirect is expected, therefore, check if response.status_code == 302
        self.assertEqual(response.status_code, 302)

    def test_about_page_status_code(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

    # def test_view_url_by_name(self):
    #     resp = self.client.get(reverse('home'))
    #     self.assertEqual(resp.status_code, 200)


class ListModelTest(TestCase):
    # test for adding new task item to the List
    def setUp(self):
        List.objects.create(item='Using TestCase to test List Model')

    def test_item_content(self):
        post = List.objects.get(id=1)
        expected_object_name = f'{post.item}'
        self.assertEqual(expected_object_name, 'Using TestCase to test List Model')

