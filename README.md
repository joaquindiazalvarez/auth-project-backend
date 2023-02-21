# ⚡Django API - Birthday countdown
## Sobre este proyecto...
  Este es un proyecto el cual está dividido en frontend y backend  
  Este repositorio pertenece a la parte del backend (API REST)  
  [pincha aquí para ir al repositorio del frontend](https://github.com/joaquindiazalvarez/auth-project-frontend)
## Descripción...
  Básicammente lo que hace esta app es generar una aplicación de Django con una base de datos postgres  
  dentro de un docker-compose. Este conjunto de contenedores se encarga de almacenar los datos del registro, que se ingresan  
  desde la aplicación del frontend y entregan diferentes requerimientos del usuario.  
# Empezando...
__(ejecución para un entorno Linux)__
Luego de clonar el repositorio, creamos un archivo .env dentro de el que debe llevar lo siguiente:  


```$ 
POSTGRES_USER=tu_usuario
POSTGRES_PASSWORD=tu_contraseña
PGADMIN_DEFAULT_EMAIL=tu_email
PGADMIN_DEFAULT_PASSWORD=tu_contraseña
```  

aquí se reemplazan los valores asignados por los que deseemos para nuestro proyecto  
y guardamos  
    
luego dentro de la terminal accedemos a la carpeta del repositorio  

```$ cd auth-project_backend```    

Luego levantamos el compose con

```$ docker compose -f docker-compose-dev.yml --env-file .env up```    
    
cuando la terminal muestre que django está corriendo, entraremos a Docker-desktop, iremos a:
Containers->Django->Terminal  
Estaremos dentro de la terminal que corre nuestra aplicación de Django  
vamos a hacer las migraciones con el siguiente comando:

```$ python3 api/manage.py migrate```    
    
Y estaremos listos para hacer request a la api.
    
# ⚡La API
## Descripción...
  Para construir la API se utilizó:
  - Django
  - Django Rest Framework
  - pyjwt 
  - django-cors-headers 
  - psycopg2 
   
  La API posee 4 endpoints.
## Views
### register -> método POST
toma los datos del registro y los guarda en la base de datos  
recibe un JSON con las claves: name, email, password y bithdate con sus respectivos values.  
devuelve un mensaje de confirmación de la recepción de datos  
### login -> método POST  
toma los datos del login y devuelve un token, si es que son válido
recibe un JSON con las claves: email y password con sus respectivos values.  
devuelve un token si el logueo es satisfactorio.  
### validate_email -> método POST
toma un email y verifica si existe o no.  
recibe un JSON con la clave email
devuelve un JSON con un booleano, que es True si ya existe el email. de lo contrario False
### get_user_information -> método GET con autenticación requerida
toma un token, lo decodifica, busca el usuario cuya id decodificamos, y devuelve el name y birthdate  
recibe un token, previamente generado en el login  
devuelve un JSON con el name y el birthdate del usuario encontrado

