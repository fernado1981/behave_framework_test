class homeorangeHrm:
    locators = {
        "id_username": "txtUsername",
        "id_password": "txtPassword",
        "xpath_message_error": "//span[@id='spanMessage']",
        "xpath_logo": "//div[@id='divLogo']//img",
        "id_btn_login": "btnLogin",
        "credential_error": "Invalid credentials"
    }

    locators_dashboard = {
        "xpath_dashboard_header": "//h1[contains(text(),'Dashboard')]",
        "Dashboard_header_name": "Dashboard"
    }
