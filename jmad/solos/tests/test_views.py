from django.test import TestCase, RequestFactory

from solos.views import index


class IndexViewTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test_index_view_basic(self):
        """
        Test that index view returns a 200 response and uses the correct template
        """
        request = self.factory.get('/')
        # first check using context manager that solos/index.html template is used
        with self.assertTemplateUsed('solos/index.html'):
            # then check the response and that it returns code 200
            response = index(request)
            self.assertEqual(response.status_code, 200)
