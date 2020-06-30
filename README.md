Comparte Ride
=============

Group-bounded, invite-only, carpooling platform

# Crear entorno
Una vez ya instalado [docker](https://www.docker.com/) y [docker-compose](https://docs.docker.com/compose/install/)

corremos el siguiente comando para crear las imagenes de nuestros contenedores:

``` shell
docker-compose -f local.yml build
```

Esto puede tarda un rato, ten paciencia.

# Ejecutar nuestro stack
`docker-compose -f local.yml up`

# Interactuar con el manage.py de Django
`docker-compose -f local.yml run --rm django [CMD]`

# Ejecutar Django en otra terminal para poder interactuar con el Debugger
``` shell
docker-compose -f local.yml up
docker-compose -f local.yml ps
docker-compose -f local.yml rm -f <ID>
docker-compose -r local.yml run --rm --service-ports django
```

# Protip
Para no ejecutar siempre **docker-compose** con `-f local.yml`. Podemos seteamos la siguiente variable de entorno `export COMPOSE_FILE=local.yml`. De esta manera podremos ejecutar solo `docker-compose`.

