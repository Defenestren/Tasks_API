Tasks API – FastAPI Backend Project

Proyecto personal desarrollado con Python y FastAPI para practicar y consolidar fundamentos de desarrollo backend.

Se trata de una API REST sencilla para la gestión de tareas, orientada al aprendizaje práctico: estructura de proyecto, validación de datos y tests automatizados.

🚀 Características

API REST para gestión de tareas

Operaciones básicas:

Listar tareas

Crear tareas

Validación de datos con Pydantic

Almacenamiento temporal con fake database (en memoria)

Tests básicos automatizados con pytest

Documentación automática con Swagger UI

🗂️ Estructura del proyecto
Tasks_API/
├── main.py
├── routers/
│   └── tasks.py
├── models/
│   └── task.py
├── db/
│   └── fake_db.py
├── tests/
│   └── test_tasks.py
├── requirements.txt
└── README.md


Estructura mínima, clara y pensada para aprendizaje backend.

🛠️ Tecnologías utilizadas

Python

FastAPI

Pydantic

Pytest

Uvicorn

▶️ Ejecución en local

Clonar el repositorio:

git clone https://github.com/TU_USUARIO/Tasks_API.git
cd Tasks_API


Crear y activar entorno virtual:

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate


Instalar dependencias:

pip install -r requirements.txt


Ejecutar la aplicación:

uvicorn main:app --reload


La API estará disponible en:

http://127.0.0.1:8000


Documentación interactiva:

http://127.0.0.1:8000/docs

🧪 Tests

Ejecutar los tests con:

pytest


Incluye tests básicos para comprobar:

Listado de tareas vacío

Creación correcta de tareas

🎯 Objetivo del proyecto

Proyecto enfocado exclusivamente al aprendizaje y a reforzar buenas prácticas en:

Diseño de APIs REST

Organización de proyectos backend

Validación de datos

Testing básico

No pretende ser un producto final ni usar base de datos real.

📌 Estado del proyecto

✅ Finalizado
🧩 Proyecto de aprendizaje backend
