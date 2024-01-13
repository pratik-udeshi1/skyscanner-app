# Skyscanner Flight Booking with Django (DRF)

This is the backend of a flight booking system similar to Skyscanner, built using Django Rest Framework. The project
consists of several modules to manage various aspects of flight booking and user management.

## Modules

1. **Airline**: Manages airlines and their details.
2. **Airport**: Handles information about airports and their locations.
3. **Flight**: Manages flight details, schedules, and availability.
4. **Booking**: Handles user flight bookings.
5. **User**: Manages user accounts and authentication.

## Getting Started

Follow these steps to set up and run the project locally.

### Prerequisites

- Python 3.x
- Django (DRF)
- PostgreSQL (or other database of your choice)
- GraphQL
- Swagger (API Documentation)

### Installation

1. Clone the repository:

   ```
   git clone https://github.com/your-username/skyscanner-app.git
   ```

2. Change to the project directory:

   ```
   cd skyscanner-app
   ```

3. Create a virtual environment and activate it:

   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   ```

4. Install the required packages:

   ```
   pip install -r requirements.txt
   ```

5. Configure your database settings in `settings.py`. Make sure to update the database name, username, and password. (or
   create .env for env variables)

6. Apply migrations:

   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

7. Create a superuser to access the Django admin interface:

   ```
   python manage.py createsuperuser
   ```

8. Run the development server:

   ```
   python manage.py runserver
   ```

### Usage

1. Access the Django admin interface by visiting `http://localhost:8000/admin/` and log in with the superuser
   credentials you created.

2. Use the admin interface to manage airline, airport, flight, booking, and user data.

3. To access the API collections, visit `http://localhost:8000/swagger/`. Here's an example format:

   #### Flight API

    - Endpoint: `/api/flight/`
    - Methods: GET, POST, PUT, DELETE

   ##### Basic Usage

    - To create a flight:
      ```
      POST /api/flight/
      {
        "airline": "Delta",
        "departure_airport": "JFK",
        "arrival_airport": "LAX",
        "departure_time": "2024-01-08T12:00:00Z",
        "arrival_time": "2024-01-08T15:00:00Z",
        "price": 300.00
      }
      ```

    - To list flights:
      ```
      GET /api/flight/
      ```

    - To update the flight:
      ```
      PUT /api/flight/{flight_id}/
      {
        "price": 350.00
      }
      ```

    - To cancel the flight:
      ```
      DELETE /api/flight/{flight_id}/
      ```

Repeat the above format for each module's API endpoints.

## Running Test Cases

#### To run test cases for the project, use the following command:

```
python manage.py test
```

## Contributing

If you'd like to fork this project, please feel free to.

## License

This project is licensed under the MIT License - see the [LICENSE](https://opensource.org/licenses/MIT) file for
details.

---

Feel free to customize the README to better suit your project and its specific API endpoints. Make sure to provide more
detailed information about each API, input validation, and any other specifics your project may have.