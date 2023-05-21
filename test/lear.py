from playwright.sync_api import Playwright, sync_playwright, expect, Page


def run(playwright: Playwright, page: Page) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page.goto("http://10.71.176.123:7008/")
    page.get_by_role("button").filter(has_text="close").click()
    page.get_by_role("button").filter(has_text="translate").click()
    page.get_by_text("中文简体").click()
    page.get_by_role("button", name="登入").click()
    page.get_by_label("管理员").click()
    page.get_by_label("管理员").fill("lear")
    page.get_by_label("管理员").press("Tab")
    page.get_by_role("textbox", name="密码").fill("lear123456")
    page.locator("div").filter(has_text="登入").get_by_role("button", name="登入").click()
    page.get_by_role("link", name="仓库管理").click()
    page.get_by_role("tab", name="容器列表").first.click()
    page.locator("tr:nth-child(22) > td:nth-child(11) > button:nth-child(2)").first.click()
    page.get_by_role("button", name="2").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright, Page)



