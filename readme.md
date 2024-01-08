# Django Boilerplate Project

This is a Django boilerplate project with basic user authentication and model setup.

## Features

- User authentication system
- Basic models configured

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

- Python [3.10]
- Django [5.0.1]
- djangorestframework
- django-seed
- simplejwt
- psycopg2

### Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/your-django-boilerplate.git
cd your-django-boilerplate
```

2. Create a virtual environment:

```bash
python -m venv venv
```

3. Activate the virtual environment:

   - For Windows:

   ```bash
   venv\Scripts\activate
   ```

   - For macOS/Linux:

   ```bash
   source venv/bin/activate
   ```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

5. Create .env:

```bash
copy .env.example content for reference
```

6. Apply migrations:

```bash
python manage.py migrate
```

7. Create a superuser:

```bash
python manage.py createsuperuser
```

8. Run the development server:

```bash
python manage.py runserver
```

9. Open your browser and go to [http://localhost:8000](http://localhost:8000)

## Contributing

If you would like to contribute to this project, please feel free to.
