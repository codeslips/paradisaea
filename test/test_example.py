from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://demo.playwright.dev/todomvc/#/")
    page.get_by_placeholder("What needs to be done?").click()
    page.get_by_placeholder("What needs to be done?").fill("my first test")
    page.get_by_placeholder("What needs to be done?").press("ArrowLeft")
    page.get_by_placeholder("What needs to be done?").press("ArrowLeft")
    page.get_by_placeholder("What needs to be done?").press("ArrowLeft")
    page.get_by_placeholder("What needs to be done?").press("ArrowLeft")
    page.get_by_placeholder("What needs to be done?").fill("my first  test")
    page.get_by_placeholder("What needs to be done?").press("Enter")
