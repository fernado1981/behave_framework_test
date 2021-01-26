class locator:
    data_locator_google_telefonica={
        "Google_bing":"https://www.bing.es",
        "logo": "//img[@alt='Telefonica.com']",
        "first":"//a[@href='https://www.telefonica.com/es/' and contains(text(),'Telefonica.com')]",
        "cookies": "//button[@id='bnp_btn_accept']//*[contains(text(),'Aceptar')]",
        "microsoft_Edge":"//*[contains(text(),'Quizás más tarde')]",
    }

    data_locator_telefonica_home={
        "title":"Telefónica",
        "accept_cookies": "//button[contains(text(),'Aceptar todas y continuar')]",
        "Accionistas": "//nav[@id='navigation']//li[4]//a",
    }

    data_locator_telefonica_accionistas={
        "url":"https://www.telefonica.com/es/web/shareholders-investors",
        "iframe_euroland_class": "EurolandTool",
        "Nyse": "//a[contains(text(),'NYSE')]",
        "valNy": ".Tab_Active .last",
    }