# PocketSense: Expense Tracking API
PocketSense is a Django-based API that helps college students track and split their daily expenses with friends. It allows users to create groups, manage expenses, and calculate balances.

## Prerequisites
Before setting up the project, ensure you have the following installed:

1. Python (Version 3.9 or higher)
2. PostgreSQL (Version 12 or higher)
3. Git
4. pip (Python package manager)
5. Virtualenv (Recommended)

## Installation Guide

1. Clone the Repository
    ```bash
    git clone <repository_name>
    cd PocketSense
    ```

2. Set Up a Virtual Environment
    ```bash
    # Create a virtual environment  
    python -m venv env

    # Activate the virtual environment
    # On Windows:
    source env\Scripts\activate
    #OR on powershell
    .\env\Scripts\activate.bat

    # On macOS/Linux:
    source env/bin/activate
    ```

3.  Install Dependencies

Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Set Up the PostgreSQL Database
Create a Database

- Open your PostgreSQL shell or admin tool (e.g., pgAdmin).
- Run the following SQL commands to create a database:
```bash
CREATE DATABASE pocketsense;
CREATE USER pocketsense_user WITH PASSWORD 'your_secure_password';
ALTER ROLE pocketsense_user SET client_encoding TO 'utf8';
ALTER ROLE pocketsense_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE pocketsense_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE pocketsense TO pocketsense_user;
```

5. Create `.env` for the secure credentials
```bash
DB_NAME=pocketsense
USER_NAME=your_username
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432
```
6. Update the database in `settings.py` file
```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER': config('USER_NAME'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST', default='localhost'), 
        'PORT': config('DB_PORT', default='5432'), 
    }
}
```

7. Apply Database Migrations
Run the following commands to apply the database migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

8. Create a Superuser

Create an admin account to access the Django admin panel:
```bash
python manage.py createsuperuser
```

9. Run the Development Server

Start the Django development server:

```bash
python manage.py runserver
# run on specific server like 5000
# python manage.py runserver 5000
```
The API will be available at `http://127.0.0.1:8000/`.

## API Endpoints Overview

1. Register Endpoint: `POST /register/` User registration.

2. Login Endpoint: `POST /login/` User authentication.

3. Groups Endpoint: 
   1. `GET /groups/` List all groups.
   2. `POST /groups/` Create a new group.
   3. `GET /groups/{id}/` Retrieve a specific group.
   4. `PUT /groups/{id}/` Update a specific group.
   5. `DELETE /groups/{id}/` Delete a specific group.

4. Expenses Endpoint:
   1. `GET /expenses/` List all expenses.
   2. `POST /expenses/` Create a new expense.
   3. `GET /expenses/{id}/` Retrieve a specific expense.
   4. `PUT /expenses/{id}/` Update a specific expense.
   5. `DELETE /expenses/{id}/` Delete a specific expense.



## Testing Each Endpoint in Postman

# A. Testing the Register Endpoint
1. Method: `POST`
2. URL: `http://127.0.0.1:8000/register/`
3. Headers: 
  `Content-Type: application/json`
4. Body (JSON):

   ```json
   {
       "username": "testuser",
       "email": "testuser@example.com",
       "password": "test1"
   }
   ```

5. Response: A successful registration returns user details or a success message.


# B. Testing the Login Endpoint

1. Method: `POST`
2. URL: `http://127.0.0.1:8000/login/`
3. Headers:
  `Content-Type: application/json`
4. Body (JSON):

   ```json
   {
       "username": "testuser",
       "password": "test1"
   }
   ```

5. Response: A successful login returns a token or authentication details.


# C. Testing the Groups Endpoint

1. List All Groups
  Method: `GET`
  URL: `http://127.0.0.1:8000/groups/`
  Headers: Include `Authorization: Bearer <token>` if authentication is required.

2. Create a Group
  Method: `POST`
  URL: `http://127.0.0.1:8000/groups/`
  Headers: 
    `Authorization: Bearer <token>`
    `Content-Type: application/json`
  Body (JSON):

     ```json
     {
         "name": "Group A",
         "description": "This is a sample group."
     }
     ```

3. Retrieve a Specific Group
  Method: `GET`
  URL: `http://127.0.0.1:8000/groups/1/`
  Headers: Include `Authorization: Bearer <token>`.

4. Update a Specific Group
  Method: `PUT`
  URL: `http://127.0.0.1:8000/groups/1/`
  Headers: 
    `Authorization: Bearer <token>`
    `Content-Type: application/json`
  Body (JSON):

     ```json
     {
         "name": "Updated Group A",
         "description": "Updated description."
     }
     ```

5. Delete a Specific Group
  Method: `DELETE`
  URL: `http://127.0.0.1:8000/groups/1/`
  Headers: Include `Authorization: Bearer <token>`.

# D. Testing the Expenses Endpoint

1. List All Expenses
  Method: `GET`
  URL: `http://127.0.0.1:8000/expenses/`
  Headers: Include `Authorization: Bearer <token>`.

2. Create an Expense
  Method: `POST`
  URL: `http://127.0.0.1:8000/expenses/`
  Headers: 
    `Authorization: Bearer <token>`
    `Content-Type: application/json`
  Body (JSON):
     ```json
     {
        "description": "Lunch",
        "amount": 105,
        "date": "07/01/2025",
        "group": 1,
    	"payer":1
     }
     ```

3. Retrieve a Specific Expense
  Method: `GET`
  URL: `http://127.0.0.1:8000/expenses/1/`
  Headers: Include `Authorization: Bearer <token>`.

4. Update a Specific Expense
  Method: `PUT`
  URL: `http://127.0.0.1:8000/expenses/1/`
  Headers: 
    `Authorization: Bearer <token>`
    `Content-Type: application/json`
  Body (JSON):
     ```json
     {
        "description": "Updated Lunch",
        "amount": 150.00,
        "date": "07/01/2025",
        "group": 1,
	    "payer":1,
     }
     ```

5. Delete a Specific Expense
  Method: `DELETE`
  URL: `http://127.0.0.1:8000/expenses/1/`
  Headers: Include `Authorization: Bearer <token>`.


## Contributing

Feel free to submit issues or pull requests to improve the project.

## License

This project is licensed under the MIT License.





