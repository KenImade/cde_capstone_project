#!/usr/bin/env bash
# entrypoint.sh

# Exit script on any error
set -e

# Default values for admin user creation
: "${AIRFLOW_ADMIN_USERNAME:=admin}"
: "${AIRFLOW_ADMIN_PASSWORD:=admin}"
: "${AIRFLOW_ADMIN_EMAIL:=admin@example.com}"
: "${AIRFLOW_ADMIN_FIRSTNAME:=Admin}"
: "${AIRFLOW_ADMIN_LASTNAME:=User}"

# Wait for the metadata database to be ready
echo "Waiting for the database to be ready..."
while ! nc -z "${AIRFLOW__CORE__SQL_ALCHEMY_CONN_HOST}" 5432; do
  sleep 1
done
echo "Database is ready."

# Initialize the Airflow metadata database
echo "Initializing the Airflow metadata database..."
airflow db upgrade

# Create the default user (if not already created)
if [ "$AIRFLOW__CORE__EXECUTOR" == "LocalExecutor" ] || [ "$AIRFLOW__CORE__EXECUTOR" == "CeleryExecutor" ]; then
  echo "Creating admin user..."
  airflow users create \
    --username "$AIRFLOW_ADMIN_USERNAME" \
    --password "$AIRFLOW_ADMIN_PASSWORD" \
    --firstname "$AIRFLOW_ADMIN_FIRSTNAME" \
    --lastname "$AIRFLOW_ADMIN_LASTNAME" \
    --role Admin \
    --email "$AIRFLOW_ADMIN_EMAIL" || echo "User already exists."
fi

# Run the command provided to the container (e.g., webserver, scheduler)
exec airflow "$@"
