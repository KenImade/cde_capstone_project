FROM apache/airflow:slim-2.10.3-python3.9

LABEL "Name"="Kenneth IMade"
LABEL email="kenimade91@gmail.com"
LABEL version="1.0"
LABEL description="Custom Airflow Image to build data pipelines \
for the CDE Capstone Project."

# Set the working directory for Airflow
WORKDIR /opt/airflow

USER root
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy entrypoint script and run
COPY airflow/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

USER airflow

# Copy and install Python dependencies
COPY airflow/requirements.txt /opt/airflow/requirements.txt
RUN pip install --no-cache-dir -r /opt/airflow/requirements.txt

# Copy DAGs
COPY airflow/dags /opt/airflow/dags

# Set entrypoint
ENTRYPOINT ["/entrypoint.sh"]

# Default command
CMD ["webserver"]

EXPOSE 8080
