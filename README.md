# nota-keeper-backend

## Project Description

This project aims to create a versioned note-taking web application:

**Features:**

1. View the list of notes
2. Create a new note
3. Edit an existing note
4. Delete a note
5. Browse the history of note modifications
    - Optional: ability to see lines added, modified, and deleted (like a simplified git diff) compared to the previous version
6. Revert to a previous version

## Requirements

To run this project, you will need:

- Python 3
- FastAPI
- Pydantic
- SQLAlchemy
- Postgres
- Docker

These technologies were chosen for their efficiency and ease of use in building modern web applications. FastAPI provides a robust framework for building APIs with Python 3, Pydantic is used for data validation and settings management, SQLAlchemy serves as the ORM for interacting with Postgres, and Docker simplifies deployment and environment management.

## How to Launch the Project with Docker

To launch the project using Docker, follow these steps:

1. Ensure Docker is installed and running on your machine.
2. Clone the repository to your local machine.
3. Navigate to the project directory in a terminal.
4. Build and run the Docker image:

```
docker compose -f docker-compose.local.yml up --build
```

6. The application should now be running and accessible through `http://localhost:8000`.

This will set up the entire application stack, including the FastAPI application and the Postgres database, in Docker containers. You can then interact with the API through the specified port.

Moreover the project documentation can be found in the `http://localhost:8000/docs` endpoint.

> To see the detailed docs, check : https://nota-keeper-backend-qsq8y.ondigitalocean.app/docs

## Things to Improve

- Add authentication and authorization to secure the application.
