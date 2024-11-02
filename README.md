https://roadmap.sh/projects/todo-list-api

# Todo List API
A simple Django-based API that provides Authentication, Create, Read, Update, Delete (CRUD) operations, along with search functionality for title,contact and category.



## Prerequisites

- Python 3.x
- PostgreSQL (or any database you use)


## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/mbnahmadi/Todo_list_API.git

2. Navigate to the project directory
3. Create and activate a virtual environment
4. Install dependencies:
- pip install -r requirements.txt
5. Setup the database:
- python manage.py makemigrations
- python manage.py migrate
6. Run the development server:
- python manage.py runserver


## Endpoints

### Athentication

- `POST /auth/register/` - Create a new user
- `POST /api/token/` - Get token to login
- `POST /api/token/refresh` - Get refresh token

### Todo

- `POST /todo/create/` - Create your new todo
- `PUT /todo/update/<id>/` - Update your specific todo by ID
- `DELETE /todo/delete/<id>/` - Delete your specific todo
- `GET /todo/get/` - Get all of your todos


## Example: Creating a resource

Request:

{
    "title": "string",
    "description": "string",
}

## Search Functionality

You can get all your todos by specific page and limit item.
    ```bash
    GET /todo/get/?page=1&limit=10


## API Documentation

The API documentation is available at `/swagger/` for Swagger UI and `/redoc/` for ReDoc.

Simply navigate to:
http://localhost:8000/swagger/


