# Flask CRUD Application with MongoDB

This project is a Flask application that performs CRUD (Create, Read, Update, Delete) operations on a MongoDB database for a `User` resource. It provides a REST API with endpoints accessible via HTTP requests.

## Getting Started

### Steps to Run the Project

1. **Clone the Repository**
   ```bash
   git clone https://github.com/sameerchauhan1/flask-crud-application.git
   ```
2. **Change into the Project Directory**
   ```shell
   cd flask-crud-application
   ```
3. **Start MongoDB with Docker**
   ```shell
   docker run -d --name mongodb -p 27017:27017 mongo
   ```
4. **Create a python environment and activate it**
   ```shell
   python -m venv venv
   .\venv\Scripts\activate
   ```
5. **Install Dependencies**
   ```shell
   pip install -r requirements.txt
   ```
6. **Run the Flask Application**
   ```shell
   flask --app app run
   ```

## API Endpoints(Test these endpoints in Postman)
The application provides the following REST API endpoints to interact with the User resource:

- GET /users - Retrieve a list of all users.
- GET /users/<id> - Retrieve a single user by their ID.
- POST /users - Create a new user.
- PUT /users/<id> - Update an existing user by ID.
- DELETE /users/<id> - Delete a user by their ID.


## User JSON Example

Here’s an example of the JSON body used when creating a user:

![Screenshot 2024-11-07 165337](https://github.com/user-attachments/assets/d9cce3b9-0a80-4788-a244-b913f0d8e3d6)

Here's an example of getting all the users present in Database:

![Screenshot 2024-11-07 170643](https://github.com/user-attachments/assets/d3dedb9e-8919-4704-851e-1a586aaecf07)



