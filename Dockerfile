# Ce fichier définit le docker container qui va contenir le Crawler app . 
# L'image de python
FROM python:3.6-slim
# ILe maintainer de l'image
LABEL maintainer="diallomouhawa97@"
# Le répertoire de travail dans le conteneur
WORKDIR /app/
COPY  crawler.py requirements.txt /app/
RUN pip install -r requirements.txt
# La commande à éxécuter lorsque le conteneur démarre
ENTRYPOINT [ "python","./crawler.py" ]