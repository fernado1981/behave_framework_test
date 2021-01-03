<a name='top'></a>
[Principal](../README.md) 

# configurar virtualenv:
**DOC:** https://dont-be-afraid-to-commit.readthedocs.io/en/latest/virtualenv.html
 * pip3 install virtualenv
 * virtualenv --version
 * pip3 show virtualenv
 
         cd /usr/local/bin
         virtualenv virtualenv
     
## Configuración básica jenkins:
# Añadir plugins:
* ShiningPanda plugin -> <https://plugins.jenkins.io/shiningpanda/>
* Allure -> <https://plugins.jenkins.io/allure-jenkins-plugin/>

# Crear proyecto Freestyle: 
**Nota:** Toda esta configuración puede ser ampliada a medida que se requiera en el proyecto.

1. New Item
    * Enter a name for de the project
2. Create Freestyle project
    * Description (pequeña descripción sobre le proyecto)
    * check GitHub project and enter the url
3. Source Code Management
    * chech the radiobutton name Git and enter the url repository with the name end in *.git -> url del clone del repo
    * añadir credenciales si tiene
    * Branch Specifier (blank for 'any') -> Ej. */master 
4. Build -> Execvute shell (Command)

        #!/bin/bash 
        . [ruta al bin/activate] && pip3 install -r requirements.txt && pip3 install allure-behave && pip3 install webdrivermanager
        . /eject.sh
5. Post-build Actions
    * Allure Report
    * **nota:** No activar Disabled
    * Results -> Path Ej. reports/allure/results (sera el directorio donde se van a ir alojando los .json generados de reporte)
6. Cucumber reports
    * Report title: -> nombre que desemos Ej. behave report
    * JSON Report Location 
        * JSON Reports Path -> donde estan alojados los json para el reporte. Ej. reports/allure/results/
        * File Include Pattern -> **/*.json
        * **NOTA:** dejar todo lo demas por defecto
        
# Configuración file eject.sh:
* Eliminará los reportes existentes cada vez que se ejecutan las pruebas.
* Ejecutará las pruebas con behave, obteniendo los .json en formato para allure-behave
    
        #!/bin/bash
        
        # Delete any previous report files
        rm -f reports/allure/results/*.json
        
        behave -f allure_behave.formatter:AllureFormatter -o reports/allure-results ./features
        
# Creamos el directorio web/drivers
* En este directorio alojaremos los drivers necesarios (firefox, chrome, ...)

ChromeDriver: https://chromedriver.chromium.org/downloads <br/>
GekoDriver: https://github.com/mozilla/geckodriver/releases/ <br/>

# actulizar fichero factory:
        return Web(webdriver.Chrome('web/drivers/chromedriver'))
        return Web(webdriver.Firefox('web/drivers/geckodriver'))


[Subir](#top)
