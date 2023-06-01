# Portable API "Medic.Madskill"

![python](https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![django](https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white)
![drf](https://img.shields.io/badge/django_rest_framework-A30000?style=for-the-badge&logo=django&logoColor=white)
![sqlite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

Django application packaged in an .exe file for launch on personal PCs
running Windows

## Description

There was a need to use the following
[![swagger](https://img.shields.io/badge/API-85EA2D?style=for-the-badge&logo=swagger&logoColor=white)](https://app.swaggerhub.com/apis-docs/serk87/APIfood/FRBHWRIOJAFIDSNKJF)
but this caused a strong dependence on a third-party service. Therefore, it
was decided to create our own portable solution to run as a regular
executable file.

## Getting Started

1. Clone the repo

```commandline
git clone https://github.com/Umbreella/medic_madskill.git
```

2. Run the file **API.exe**

```
./pyinstaller/API/API.exe
```

## Installation

1. Clone the repo

```commandline
git clone https://github.com/Umbreella/medic_madskill.git
```

2. Install dependencies

```commandline
pip install -r requirements.txt
```

3. Run file **manage.py**

```commandline
python manage.py
```

## Endpoints

* Django admin

```swagger codegen
[your_ip_address]/admin/
```

* REST docs

```swagger codegen
[your_ip_address]/api/docs/
```

## Login Data

* Administrator

```commandline
email: admin@admin.admin
password: admin
```
