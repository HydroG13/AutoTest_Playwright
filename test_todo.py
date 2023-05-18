import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def page():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        context = browser.new_context()
        page = context.new_page()
        yield page
        context.close()
        browser.close()

def test_add_todo(page):
    pass

def test_add_todo(page):
    page.goto("https://develop.intelogis.ru/analytics-tender/main")
    page.get_by_label("Логин").click()
    page.get_by_label("Логин").fill("ptr.pert@yandex.ru")
    page.get_by_label("Пароль").click()
    page.get_by_label("Пароль").fill("123zxc123")
    page.get_by_label("Пароль").press("Enter")


