from flaskinfo import app
import unittest


class AboutTestCase(unittest.TestCase):

    def test_about_page_loads(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertTrue(b'About me' in response.data)


if __name__ == '__main__':
    unittest.main()
