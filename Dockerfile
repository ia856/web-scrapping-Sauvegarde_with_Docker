# This files define the docker container that will contain the Crawler app . 
# From the source python image
FROM python:3.6-slim
# Identify maintainer
LABEL maintainer="diallomouhawa97@gmail.com"
# Set the default working directory
WORKDIR /app/
COPY  crawler.py requirements.txt /app/
RUN pip install -r requirements.txt
CMD [ "python","./crawler.py" ]
# When the container starts, run this
ENTRYPOINT [ "python","./crawler.py" ]