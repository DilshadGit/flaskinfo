from flaskinfo import app
import unittest


class RunTestCase(unittest.TestCase):
    def test_home(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)


    def test_about_page_loads(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertTrue(b'About me' in response.data)


if __name__ == '__main__':
    unittest.main()
