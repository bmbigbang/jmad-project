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
        self.assertEqual('JMAD', brand_element.text)

        # He sees the inputs of the search form, including labels and placeholders.
        instrument_input = self.browser.find_element_by_css_selector('input#jmad-instrument')
        self.assertIsNotNone(self.browser.find_element_by_css_selector('label[for="jmad-instrument"]'))
        self.assertEqual(instrument_input.get_attribute('placeholder'), 'i.e. trumpet')

        artist_input = self.browser.find_element_by_css_selector('input#jmad-artist')
        self.assertIsNotNone(self.browser.find_element_by_css_selector('label[for="jmad-artist"]'))
        self.assertEqual(artist_input.get_attribute('placeholder'), 'i.e. Davis')

        # He types in the name of his instrument and submits it.
        instrument_input.send_keys('saxophone')
        self.browser.find_element_by_css_selector('form button').click()

        # He sees too many search results so he adds a particular artist to his search query

        search_results = self.browser.find_elements_by_css_selector('.jmad-search-result')
        self.assertGreater(len(search_results), 2)
        # ...so he adds an artist to his search query and gets a more manageable list.

        # He clicks on a search result.

        # The solo page has the title, artist and album for this particular solo.

        # He also sees the start time and end time of the solo.
        self.fail('Incomplete Test')


