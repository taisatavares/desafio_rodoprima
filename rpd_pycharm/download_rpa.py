import time
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(accept_downloads=True)

    page = context.new_page()


    sheet_url = "https://docs.google.com/spreadsheets/d/1AhbsIqh6mQ8J4cKRgEkHokNo2uNmsxkYZL0hxbzxZtc/edit?gid=0#gid=0"
    page.goto(sheet_url)


    page.wait_for_timeout(5000)


    page.locator('role=menuitem[name="Arquivo"]').click()


    page.locator("text=Baixar").click()


    page.locator("text=Microsoft Excel (.xlsx)").click()


    download = page.wait_for_event("download", timeout=60000)
    download_path = download.path()
    download.save_as("planilha.xlsx")

    print("Download concluído!")

    browser.close()