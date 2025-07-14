#!/bin/sh

# Wait for PostgreSQL
echo "Waiting for postgres..."

while ! nc -z db 5432; do
  sleep 0.1
done

echo "PostgreSQL started"

# Run migrations and server
exec "$@"