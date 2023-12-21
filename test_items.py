from conftest import on_form


def test_bucket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)

    assert on_form(browser, '.btn-add-to-basket'), '"Add to chart" button not found'
