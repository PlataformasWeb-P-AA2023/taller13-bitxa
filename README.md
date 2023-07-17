# taller13.2
## Joel Romero y Jhoel Ordoñez

## Creación de Servicio Web y Consumo vía Flask

## Usar un rama/branch llamada v2 y trabajar en dicha versión

### Problemática

Dadas dos entidades:

* Edificio:
	* nombre
	* dirección
	* ciudad
	* tipo [residencial, comercial]

* Departamento
	* Propietario (tipo Propietario - nombre, apellido, cédula)
	* costo del departamento
	* número de cuartos
	* edificio

Nota: Un departamento pertenece a un edificio

### Tecnologías y herramientas:

- Base de datos Sqlite
- Lenguaje Python
- Framework Django
- Django-Rest
- Flask


### Tarea a realizar:

- Crear un proyecto de Django.
- Crear una aplicación en el proyecto den Django.
- Generar el modelo de la aplicación usando las entidades descritas.
- Activar la interfaz de administración de la aplicación de Django.
- Agregar servicios web que permitan lista; crear; actualizar y eleminar entidades (todas deben tener acceso con autentificación)
- Crear una aplicación en Flask que permita listar Edificios y Departamentos, Propietarios, haciendo uso de los servicios web creados en el proyecto de Django. Atención, al momento de listar los propietarios se deben visualizar el total de los departamentos del propietarios, y la lista de edificios de los departamentos.