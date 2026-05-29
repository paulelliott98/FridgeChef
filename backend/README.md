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
│   │           ├── inventory.py
│   │           ├── recipes.py
│   │           └── groceries.py
│   ├── db/
│   │   ├── session.py
│   │   ├── base.py
│   │   └── init_db.py
│   ├── models/
│   │   ├── user.py
│   │   ├── inventory.py
│   │   ├── recipe.py
│   │   ├── ingredient.py
│   │   ├── grocery_list.py
│   │   └── __init__.py
│   ├── schemas/
│   │   ├── user.py
│   │   ├── inventory.py
│   │   ├── recipe.py
│   │   └── ...
│   ├── services/
│   │   ├── inventory_service.py
│   │   ├── recipe_service.py
│   │   └── grocery_service.py
│   └── dependencies.py
├── alembic/
├── tests/
├── pyproject.toml
└── .env.example
```

# Python Package Manager

Link:  
https://docs.astral.sh/uv/getting-started/installation/

To install on macOS:

```
brew install uv
```

# Local Postgres DB Setup

Download Docker Desktop, which should also install docker compose. Inside /backend which contains docker-compose.yml, run:

```
docker compose up -d
```

to start the postgres db container.

Not needed now, but we can start session to DB server using:

```
docker exec -it fridgechef-db psql -U fridgechef -d fridgechef
```

Install required packages (alembic, psycopg[binary], etc.) using:

```
uv sync
```

Make sure you don't have a local postgres server running (e.g. postgres installed using brew), or the following command might use the wrong postgres server and fail. We want to use the docker db server. 

To create a migration file, run:
```
uv run alembic revision --autogenerate -m "MESSAGE"
```
Note: We only need to create migration file when we change the db schema. If someone created a new migration file, we just skip to the below command to change our db tables.

To create the tables, run:
```
uv run alembic upgrade head
```

To check existing tables:
```
docker exec -it fridgechef-db psql -U fridgechef -d fridgechef
\dt
```