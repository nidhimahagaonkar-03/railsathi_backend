# RailSathi Backend — Dockerized Django App with PostgreSQL

This is the backend for RailSathi, a Django REST API application containerized with Docker and PostgreSQL.

## Setup Instructions

1. Clone the repo: `git clone https://github.com/your-username/RailSathiBE.git && cd RailSathiBE`  
2. Create a `.env` file in the root directory with the following content:  
`POSTGRES_DB=railsathi_db`  
`POSTGRES_USER=railsathi_user`  
`POSTGRES_PASSWORD=supersecretpassword`  
`DB_HOST=db`  
`DB_PORT=5432`  
3. Run the application using Docker Compose: `docker-compose up --build`  
This will build the image, start PostgreSQL, run migrations, and serve the app on port 8000.

## Access

- API Endpoint: [http://localhost:8000/items/](http://localhost:8000/items/)  
- Admin Panel: [http://localhost:8000/admin/](http://localhost:8000/admin/)  

To create a superuser for the admin panel, open a terminal inside the running container:  
`docker-compose exec web python manage.py createsuperuser`

## Assumptions & Design Decisions

- PostgreSQL is used as the default DB for production and development.  
- Database migrations are triggered automatically on container startup via the entrypoint script.  
- Static files are collected inside the container (though this is more relevant for production with `whitenoise` or cloud storage).  
- `wait-for-db.sh` ensures Django waits for PostgreSQL to be ready before running commands.  
