# Tasks API

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-green)
![Tests](https://img.shields.io/badge/tests-pytest-success)
![Status](https://img.shields.io/badge/status-learning_project-informational)

API REST desarrollada con **Python y FastAPI** como proyecto personal para consolidar fundamentos de desarrollo backend.

Proyecto enfocado en estructura clara, validación de datos y tests automatizados, siguiendo buenas prácticas básicas de diseño de APIs.

---

## 🚀 Funcionalidades

- Listado de tareas
- Creación de tareas
- Validación de datos con Pydantic
- Persistencia en memoria (fake database)
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

## ▶️ Ejecución en local

### 1️⃣ Clonar el repositorio
```bash
git clone https://github.com/Marcial-Godes/Tasks_API.git
cd Tasks_API
```

### 2️⃣ Crear y activar entorno virtual
```bash
python -m venv venv

Windows
venv\Scripts\activate

Linux / macOS
source venv/bin/activate
```

### 3️⃣ Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4️⃣ Ejecutar la API
```bash
uvicorn main:app --reload

La API estará disponible en:
http://127.0.0.1:8000

Swagger UI:
http://127.0.0.1:8000/docs
```

---

### 🧪 Tests
```bash
Tests implementados con pytest.
Ejecutar tests:
pytest
```
Casos cubiertos:

API sin tareas iniciales

Creación correcta de una tarea

---

### 🎯 Objetivo del proyecto

Proyecto con fines formativos, orientado a practicar:

Diseño de APIs REST

Organización de un proyecto backend

Validación de datos

Testing automatizado básico

No orientado a producción.
