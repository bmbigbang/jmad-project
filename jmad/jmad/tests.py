from selenium import webdriver
from django.test import LiveServerTestCase


class StudentTestCase(LiveServerTestCase):

    def setUp(self):
        # run on each startup
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(2)

    def tearDown(self):
        # run on each shut down
        self.browser.quit()

    def test_student_find_solos(self):
        """
        Test that a user can search for solos
        """

        # vising the home page of JMAD and check the site heading
        home_page = self.browser.get(self.live_server_url + '/')
        brand_element = self.browser.find_element_by_css_selector('.navbar-brand')
        self.asserEqual('JMAD', brand_element.text)

        # He sees the inputs of the search form, including labels and placeholders.

        # He types in the name of his instrument and submits it.

        # He sees too many search results...

        # ...so he adds an artist to his search query and gets a more manageable list.

        # He clicks on a search result.

        # The solo page has the title, artist and album for this particular solo.

        # He also sees the start time and end time of the solo.
        self.fail('Incomplete Test')


