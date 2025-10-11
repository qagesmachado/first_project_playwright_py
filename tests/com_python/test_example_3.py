from playwright.sync_api import sync_playwright

def network_events():
    with sync_playwright() as p:
        # Lança o navegador WebKit (simula Safari / iPhone)
        browser = p.webkit.launch(headless=False)
        
        # Emula iPhone 13
        iphone = p.devices["iPhone 13"]
        context = browser.new_context(**iphone)
        
        # Nova aba
        page = context.new_page()
        
        # Acessa o site
        page.goto("https://coderbyte.com")
        
        # Tenta clicar no botão com id #mainButton
        # try:
        #     page.locator("#mainButton").click()
        #     print("Botão clicado com sucesso!")
        # except:
        #     print("Elemento #mainButton não encontrado.")
        
        # Fecha o navegador
        browser.close()

# Executa a função
network_events()
