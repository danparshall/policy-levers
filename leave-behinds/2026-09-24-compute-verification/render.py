from playwright.sync_api import sync_playwright
import sys
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page()
    pg.goto("file://"+__import__("os").path.abspath("leave-behind.html")); pg.wait_for_timeout(300)
    # report overflow per page
    ov = pg.evaluate("""() => [...document.querySelectorAll('.page')].map(e=>({sh:e.scrollHeight, ch:e.clientHeight}))""")
    print(ov)
    pg.pdf(path="leave-behind.pdf", format="Letter", print_background=True, prefer_css_page_size=True)
    b.close()
