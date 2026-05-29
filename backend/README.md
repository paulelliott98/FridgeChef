# FridgeChef Backend Directory Structure
Exact files will vary, but we should follow this folder organization:
```
backend/
├── app/
│   ├── main.py
│   ├── api/
│   │   └── v1/
│   │       └── routes/
│   │           ├── auth.py
│   │           ├── pantry.py
│   │           ├── recipes.py
│   │           └── groceries.py
│   ├── db/
│   │   ├── session.py
│   │   ├── base.py
│   │   └── init_db.py
│   ├── models/
│   │   ├── user.py
│   │   ├── pantry_item.py
│   │   ├── recipe.py
│   │   ├── ingredient.py
│   │   ├── grocery_list.py
│   │   └── __init__.py
│   ├── schemas/
│   │   ├── user.py
│   │   ├── pantry_item.py
│   │   ├── recipe.py
│   │   └── ...
│   ├── services/
│   │   ├── pantry_service.py
│   │   ├── recipe_service.py
│   │   └── grocery_service.py
│   └── dependencies.py
├── alembic/
├── tests/
├── pyproject.toml
└── .env.example
```