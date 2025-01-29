# Derived from official my sql image (ourb base image)
FROM mysql
# Add a database of the sql-scripts/ directory to your image
# All scripts in docker-entrypoint-initdb.d/ are automatically
# Executed during container startup
COPY ./sql-scripts /docker-entrypoint-initdb.d/
