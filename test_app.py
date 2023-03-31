from app import app
from unittest import TestCase

class ConverterTestCase(TestCase):
    def test_home(self):
        with app.test_client() as client:
            resp = client.get('/')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('Welcome to the Currency Converter', html)

    # def test_result(self):
    #     with app.test_client() as client:
    #         resp = client.get('/result')
    #         html = resp.get_data(as_text=True)

    #         self.assertEqual(resp.status_code, 200)
    #         self.assertIn('The result is:', html)

    def test_is_valid_currency(self):
        with app.test_client() as client:
            resp = client.get('/is_valid_currency')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('The result is:', html)

    
