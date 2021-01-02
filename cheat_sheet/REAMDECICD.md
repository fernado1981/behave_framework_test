<a name='top'></a>
[Principal](../README.md) 

# configurar virtualenv:
 pip3 install virtualenv 
 
export PATH=$PATH:/usr/local/bin
export PATH=$PATH:/usr/local/bin/python3
export PATH=$PATH:/Library/Frameworks/Python3.framework/Versions/3.7/lib/site-packages

ln -s /Library/Frameworks/Python3.framework/Versions/3.7/bin/virtualenv /usr/local/bin/virtualenv

## Configuración básica jenkins:
**Nota:** Toda esta configuración puede ser ampliada a medida que se requiera en el proyecto

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
        . venv/bin/activate && pip3 install -r requirements.txt && pip3 install webdrivermanager
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
* Recorrerá los ficheros don de están ubicados los .features y ejecutara behave, obteniendo los .json en el directorio reports/allure/results/
* ejecutara el fichero convert2cucumber.py para la generación del reporte cucumber en jenkins
    
        #!/bin/bash
        
        # Delete any previous report files
        rm -f reports/allure/results/*.json
        
        # Run Every feature
        for folder in features/orange_hrm/orange*; do
            behave $folder -f json.pretty -o reports/allure/results/$folder.json || true;
        done
        
        # Convert every report to cucumber format for further jenkins report
        for f in reports/allure/results/* ; do
            python convert2cucumber.py $f
        done

# Creacion del fichero convert2cucumber.py

    import json
    import behave2cucumber
    import sys
    
    fPath = str(sys.argv[1])
    cucumber_json = None
    with open(fPath) as behave_json:
        cucumber_json = behave2cucumber.convert(json.load(behave_json))
    
    with open(fPath, "w") as of:
        json.dump(cucumber_json, of)
        
# Creamos el directorio web/drivers
* En este directorio alojaremos los drivers necesarios (firefox, chrome, ...)

ChromeDriver: https://chromedriver.chromium.org/downloads <br/>
GekoDriver: https://github.com/mozilla/geckodriver/releases/ <br/>

# actulizar fichero factory:
        return Web(webdriver.Chrome('web/drivers/chromedriver'))
        return Web(webdriver.Firefox('web/drivers/geckodriver'))


[Subir](#top)
