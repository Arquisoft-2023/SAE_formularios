# SAE_formularios_ms

Aplicación en Python con FastAPI, Uvicorn y PyMongo
Esta aplicación ha sido desarrollada en Python utilizando el framework FastAPI y los servidores Uvicorn. Además, se ha empleado PyMongo para interactuar con una base de datos MongoDB, la cual también ha sido dockerizada.

La utilización de Docker ha permitido la creación de un Dockerfile que facilita la dockerización de la aplicación, permitiendo su fácil despliegue en diferentes entornos.

La arquitectura de la aplicación está diseñada para ser eficiente y escalable, y la combinación de las tecnologías mencionadas garantiza un alto rendimiento y una gran flexibilidad.

# instrucciones para correr la api

en consola utilizar los siguientes comando de manera ordenada 


docker network create mi-red

en la carpeta de la base de datos:

docker build -t mongo .

docker run --name mi-mongo --network mi-red -p 27018:27017 -d mongo

en la carpeta de la api:

docker build -t mi-aplicacion .

docker run --name mi-aplicacion --network mi-red -p 8000:8000 mi-aplicacion

¡Gracias por utilizar esta aplicación! Si tienes alguna duda o sugerencia, no dudes en ponerte en contacto con nosotros.
