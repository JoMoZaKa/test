import re
from playwright.sync_api import Page, expect
'''
def test_has_title(page: Page):
    page.goto("https://playwright.dev/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Playwright"))

def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/")

    # Click the get started link.
    page.get_by_role("link", name="Get started").click()

    # Expects page to have a heading with the name of Installation.
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()
'''

'''
def test_has_title(page: Page):
    page.goto("https://demo.opencart.com/admin")
    page.get_by_placeholder('Username').fill('demo')
    page.wait_for_timeout(3000)
    page.get_by_placeholder('Password').fill('demo')
    page.wait_for_timeout(3000)
    page.get_by_role('button').click()
    page.wait_for_timeout(3000)
    title = page.get_by_role("heading", name="Dashboard")
    expect(title).to_be_visible()
'''


'''
page.goto("https://demo.opencart.com/admin")
        page.wait_for_timeout(5000)
        page.get_by_placeholder('Username').fill('demo')
        page.wait_for_timeout(5000)
        page.get_by_placeholder('Password').fill('demo')
        page.wait_for_timeout(5000)
        login_button = page.locator('button[type="submit"]')
        login_button.click()
        page.wait_for_timeout(10000)
'''

def test_registration_page(page: Page):
    page.goto('http://users.bugred.ru/')
    page.wait_for_load_state('load')
    page.get_by_text('Войти').click()
    page.wait_for_load_state('domcontentloaded')
    page.locator("input[name=\"name\"]").fill("JoJo")
    page.wait_for_timeout(2000)
    page.locator("input[name=\"email\"]").fill("test@test.test")
    page.wait_for_timeout(2000)
    page.locator("tbody").filter(has_text="Имя Email").locator("input[name=\"password\"]").fill("password")
    page.wait_for_timeout(2000)
    page.get_by_role('button', name='Зарегистрироваться').click()

def test_test_login(page: Page):
    page.goto('http://users.bugred.ru/')
    page.wait_for_load_state('load')

