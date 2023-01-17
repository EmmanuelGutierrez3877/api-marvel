# prueba-tecnica

filtros de busqueda
1=personaje
2=comic

no encontre el valor "apperance" en personaje

user alex
pass 1234

docker commands
docker version
docker images
docker pull mongo //bajar una imagen
docker create mongo //crear container
docker start id_container //iniciar container
docker ps //ver containers corriendo
docker stop id_container //detener container
docker ps -a //mostrar containers incluyendo apagados

docker create --name nombre mongo //crear container con nombre
docker create -pPuertoLocal:PuertoDocker --name nombre mongo //-p27017:27017
docker logs name //logs del container
docker logs --follow name //escuchar logs

docker run -d mongo //descarga imagen, crea contenedor y lo inicia

docker create -p27018:27017 --name DB_Comics --network redComics -e MONGO_INITDB_ROOT_USERNAME=alex -e MONGO_INITDB_ROOT_PASSWORD=1234 mongo:4.4.18

docker network ls
docker network create redcomics

//subir docker python
pip freeze > requirements.txt
docker build -t flask1 .

docker create -p8001:8000 --name Busqueda --network redComics flask1

docker create -p8002:8000 --name Usuarios --network redComics flask2

docker create -p8003:8000 --name Apartados --network redComics flask3