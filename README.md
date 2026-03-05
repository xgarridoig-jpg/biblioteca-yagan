# Biblioteca Yagán — Sistema de Gestión Bibliográfica

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square\&logo=python\&logoColor=white)
![Django](https://img.shields.io/badge/Django-4.x-092E20?style=flat-square\&logo=django\&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-4169E1?style=flat-square\&logo=postgresql\&logoColor=white)

---

## Descripción

**Biblioteca Yagán** es una aplicación web desarrollada con **Django** orientada a la gestión de registros bibliográficos.

El proyecto implementa un modelo relacional para organizar información sobre libros y sus atributos utilizando **PostgreSQL** como base de datos y el **ORM de Django** para la interacción con los datos.

La aplicación está construida siguiendo la arquitectura **MTV (Model–Template–View)** del framework y permite realizar operaciones básicas de administración y gestión de catálogo.

---

## Características

* Registro y administración de libros
* Edición y eliminación de registros
* Gestión de datos mediante **Django Admin**
* Persistencia de datos utilizando **PostgreSQL**
* Consultas y relaciones gestionadas mediante **Django ORM**
* Organización del proyecto siguiendo las convenciones de Django

---

## Stack tecnológico

* **Python**
* **Django**
* **PostgreSQL**
* **Django ORM**
* **Git**

---

## Arquitectura del proyecto

```
biblioteca-yagan/
│
├── biblioteca/
│   ├── biblioteca/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── ...
│   │
│   ├── catalogo/
│   │   ├── migrations/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── admin.py
│   │   ├── templates/
│   │   └── static/
│   │
│   └── manage.py
│
└── evidencias/
```

La aplicación principal es **catalogo**, donde se definen los modelos y la lógica de negocio relacionada con la gestión del catálogo bibliográfico.

---

## Instalación y ejecución

### Requisitos

* Python 3
* PostgreSQL

---

### 1. Clonar repositorio

```bash
git clone https://github.com/xgarridoig-jpg/biblioteca-yagan.git
cd biblioteca-yagan
```

---

### 2. Crear entorno virtual

```bash
python -m venv venv
source venv/bin/activate

# Windows
venv\Scripts\activate
```

---

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

### 4. Configurar base de datos

Crear una base de datos en PostgreSQL y ajustar las credenciales en:

```
settings.py
```

---

### 5. Ejecutar migraciones

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 6. Ejecutar servidor

```bash
python manage.py runserver
```

Aplicación disponible en:

```
http://127.0.0.1:8000/
```

Panel administrativo:

```
http://127.0.0.1:8000/admin/
```

---

## Proyección del proyecto

La estructura actual permite extender el sistema hacia funcionalidades como:

* gestión de autores y editoriales
* control de préstamos
* búsqueda avanzada de catálogo
* generación de reportes de inventario

---

## Autora

**Ximena Garrido**
Backend Developer

Portafolio
[https://xgarridoig-jpg.github.io/](https://xgarridoig-jpg.github.io/)

LinkedIn
[https://www.linkedin.com/in/xpgarrido/](https://www.linkedin.com/in/xpgarrido/)

