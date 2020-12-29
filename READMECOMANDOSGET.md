## Comandos Get:
Ayudan a buscar informacion importante sobre la página/elemento. estos son algunos de los más importantes:  
- **getTitle**, no necesita parámetros, este obtiene el título de la página.

    driver.title

- **getPageSource**, no necesita parámetros, devuelve el código de la página como valor de cadena.
    
    driver.page_source

- **getCurrentUrl**, No necesita parámetros, obtiene la url actual del navegador

    driver.current_url
    
- **getText()**, recupera el texto interior del elemento que se especifique

## Comandos navigate:
permiten navegar entre las diferentes páginas Web.
- **get()**, abre una nueva ventana del exploradory busca la página que se especifique dentro de los parentesis, el parámetro debe ser un objeto string.

    driver.get("https://selenium.dev")
    
- **Retroceder**

    driver.back()

- **Avanzar**

    driver.forward()

- **Actualizar**

    driver.refresh()
    
## Cerrar y salir del navegador:
- close

    driver.close()

- quit()

    driver.quit()
