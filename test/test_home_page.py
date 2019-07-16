import pytest

def test_example(selenium):
    selenium.get(' http://127.0.0.1:5000/')
    try:
        driver.find_element_by_id('title')
    except NoSuchElementException:
        return False
