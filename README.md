# Blogging Platform API

This is a RESTful API for a Blogging Platform where users can create, read, update, and delete blog posts. The API also supports user authentication and authorization.

## Getting Started

These instructions will help you set up and run the Blogging Platform API on your local machine.

### Prerequisites

- Python 3.x
- Flask
- Flask SQLAlchemy
- Flask Bcrypt
- Flask JWT Extended

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/blogging-platform-api.git
    cd blogging-platform-api
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up environment variables:

    Copy the `.env.example` file to `.env` and update the configuration values, including the database URI and secret key.

4. Run the application:

    ```bash
    python app.py
    ```

The API should now be running at `http://localhost:5000`.

## API Endpoints

### User Authentication

- **POST /register**: Register a new user.

  ```bash
  curl -X POST -H "Content-Type: application/json" -d '{"username":"yourusername", "password":"yourpassword"}' http://localhost:5000/register

