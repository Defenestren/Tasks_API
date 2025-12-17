# Tasks API

API REST desarrollada con **Python y FastAPI** como proyecto personal para practicar y consolidar fundamentos de desarrollo backend.

El proyecto implementa una gestión básica de tareas, con una estructura clara, endpoints simples y tests automatizados.

---

## Funcionalidades

- Listado de tareas
- Creación de tareas
- Validación de datos mediante modelos
- Almacenamiento en memoria (fake DB)
- Tests automatizados con pytest

---

## Estructura del proyecto

<pre>
asks_API/
├── main.py
├── routers/
│ └── tasks.py
├── models/
│ └── task.py
├── db/
│ └── fake_db.py
├── tests/
│ └── test_tasks.py
├── requirements.txt
└── README.md
</pre>


---

## Tecnologías utilizadas

- Python
- FastAPI
- Pytest
- Uvicorn

---

## Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/Defenestren/Tasks_API.git
cd Tasks_API


Crear y activar entorno virtual
python -m venv venv
# Windows
venv\Scripts\activate


Instalar dependencias
pip install -r requirements.txt


Ejecutar la aplicación
uvicorn main:app --reload


Documentación interactiva (Swagger):

http://127.0.0.1:8000/docs


```

```bash
Tests

Los tests están implementados con pytest.

Para ejecutarlos:

pytest

```

---

Notas

Proyecto realizado con fines formativos, enfocado en aprender buenas prácticas básicas de estructura, testing y desarrollo de APIs backend con Python.



