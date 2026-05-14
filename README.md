# Sistema Biblioteca (POO + DAO + MySQL)

Proyecto educativo en Python por consola para practicar POO, CRUD y patrón DAO sin frameworks.

## Requisitos
- Python 3.10+
- MySQL Server
- Dependencia: `mysql-connector-python`

## Instalación
```bash
pip install mysql-connector-python
```

## Base de datos
1. Crear la base ejecutando el script:
```bash
mysql -u root -p < database/biblioteca.sql
```
2. Revisar credenciales en `models/Conexion.py` (`user`, `password`, `host`).

## Ejecutar
```bash
python main.py
```

## Datos de prueba
- Bibliotecario: `admin1` / password `admin123`
- Suscriptores: `sus001`, `sus002`
- Passwords suscriptores: `sus001123`, `sus002123`
- 2 autores, 3 libros y 1 préstamo activo ya cargados por SQL.
