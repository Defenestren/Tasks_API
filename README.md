# Tasks API

API REST desarrollada con **Python y FastAPI** como proyecto personal para practicar y consolidar fundamentos de desarrollo backend.

Este proyecto implementa una API sencilla para la gestión de tareas, con estructura clara, validación de datos y tests automatizados.

---

## 🚀 Funcionalidades

- Listar tareas
- Crear tareas
- Validación de datos con Pydantic
- Almacenamiento en memoria (fake database)
- Tests automatizados con pytest
- Documentación automática con Swagger UI

---

## 🗂️ Estructura del proyecto

Tasks_API/
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


---

## 🛠️ Tecnologías utilizadas

- **Python**
- **FastAPI**
- **Pydantic**
- **Pytest**
- **Uvicorn**

---

## ▶️ Cómo ejecutar en local

1. **Clonar el repositorio**
```bash
git clone https://github.com/Marcial-Godes/Tasks_API.git
cd Tasks_API

Crear y activar un entorno virtual

python -m venv venv


Windows

venv\Scripts\activate


Linux/macOS

source venv/bin/activate


Instalar dependencias

pip install -r requirements.txt


Ejecutar la API

uvicorn main:app --reload


La API estará disponible en:

http://127.0.0.1:8000


Documentación interactiva de Swagger UI:

http://127.0.0.1:8000/docs
```


## 🧪 Tests

2. **Los tests están implementados con pytest.**
Para ejecutarlos:

```bash
os tests están implementados con pytest.
Para ejecutarlos:

pytest


Incluyen casos básicos como:

Obtener tareas cuando no hay ninguna

Crear una tarea correctamente
```

---

##🎯 Objetivo del proyecto

Este proyecto es de aprendizaje y práctica, orientado a reforzar:

Diseño de APIs REST

Organización de proyecto backend

Validación de datos

Testing automatizado básico

No está pensado para producción.
