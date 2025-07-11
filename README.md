Clonación repositorio:
  Primero, debe clonarse el repositorio con el siguiente comando "git clone https://github.com/jphc98/Prueba.git".
Activación entorno virtual:
  Desde un computador con Python (en caso de ser necesario, se puede descargar desde esta url https://www.python.org/downloads/), se debe activar el entorno virtual de la siguiente forma:
    * Se abre una terminal y se ejecutan los siguientes comandos, desde la carpeta raíz clonada del repositorio:
      - python -m venv venv
      - cd venv
      - Scripts\activate
      - pip install -r requirements.txt
Ejecución código:
  Con el entorno virtual activado, se ejecuta "python manage.py runserver" desde la misma carpeta raíz del proyecto. Al ejecutarlo, se desplegará el servidor de desarrollo, y mostrará su dirección para acceder a este en el navegador.
  En la URL, que debe ser "http://127.0.0.1:8000/", accedemos al centro de documentación de las APIs completándola de esta forma "http://127.0.0.1:8000/docs", acá, se mostrarán cada uno de los elementos del proyecto y sus respectivos endpoint.

Cualquier información adicional que sea requerida, será brindada.  
