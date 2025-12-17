# Tasks API

Simple REST API developed with Python and FastAPI as a learning project.

The goal of this project is to practice backend fundamentals such as API design, data validation, routing and basic automated testing.

## Features

- Retrieve task list
- Create new tasks
- Input validation using Pydantic models
- In-memory fake database
- Basic automated tests with pytest

## Tech stack

- Python
- FastAPI
- Pytest

## Project structure

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


## Run locally

Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate


Install dependencies:

pip install -r requirements.txt


Run the API:

uvicorn main:app --reload


Run tests:

pytest