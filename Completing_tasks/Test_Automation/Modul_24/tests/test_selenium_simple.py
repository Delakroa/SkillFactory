

def test_search_example(selenium):
    """Search some phrase in google and make a screenshot of the page."""

    # Open google search page:
    selenium.get('http://google.com')

    # Find the field for search text input
    search_input = selenium.find_element_by_id('lst-ib')

    # Enter the text for search:
    search_input.clear()
    search_input.send_keys('my first selenium test for Web UI!')

    # Click Search:
    search_button = selenium.find_element_by_name('btnK')
    search_button.click()

    # Make the screenshot of browser windows:
    selenium.save_screenshot('result.png')

