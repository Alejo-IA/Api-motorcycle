Buscador de Motos
Esta aplicación te permite buscar motos usando la API de Ninjas. Puedes filtrar por marca, modelo, año y tipo de moto, y ver los resultados en una tabla. También puedes descargar los resultados en formato Excel.
Características principales

Búsqueda de motos con filtros personalizables
Interfaz gráfica sencilla y fácil de usar
Exportación de resultados a Excel
Visualización de datos en una tabla ordenada

Requisitos
Para ejecutar esta aplicación necesitas:

Python 3.8 o superior
Las librerías especificadas en requirements.txt

Instalación

Clona este repositorio o descarga los archivos
Crea un archivo .env en la raíz del proyecto con tu API key:
CopyAPI_NINJA_KEY=tu_clave_api_aqui

Instala las dependencias:
Copypip install -r requirements.txt


Cómo usar

Ejecuta el programa:
Copypython run.py

En la ventana de la aplicación:

Escribe la marca, modelo, año o selecciona un tipo de moto
Haz clic en "Buscar" para ver los resultados
Usa "Limpiar" para borrar los filtros
Haz clic en "Descargar Excel" para guardar los resultados



Estructura del proyecto
Copyapi_cars/
├── .env                 # Mis credenciales (no incluido en repositorio)
├── requirements.txt     # Librerías necesarias
├── run.py               # Archivo para ejecutar la aplicación
├── src/                 # Código fuente
│   ├── main.py          # Punto de entrada principal
│   ├── config.py        # Configuración
│   ├── ui/              # Interfaz de usuario
│   │   └── app.py       # Código de la interfaz
│   └── api/             # Comunicación con APIs
│       └── motorcycles.py  # Funciones para la API de motos
└── data/                # Carpeta para guardar los Excel
Notas importantes



https://github.com/Alejo-IA
