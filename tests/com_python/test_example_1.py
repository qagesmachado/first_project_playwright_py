from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Escolhe o navegador (chromium, firefox ou webkit)
    browser = p.chromium.launch(headless=False)  # False = abre a janela real
    page = browser.new_page()

    # Abre uma página web
    page.goto("https://www.google.com")
    print(page.title())

    # Espera um pouco para você ver a página
    page.wait_for_timeout(3000)

    # Fecha o navegador
    browser.close()
