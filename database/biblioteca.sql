DROP DATABASE IF EXISTS biblioteca;
CREATE DATABASE biblioteca;
USE biblioteca;

CREATE TABLE usuarios (
    id_usuario VARCHAR(20) PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    direccion VARCHAR(200),
    tipo_usuario ENUM('bibliotecario','suscriptor') NOT NULL,
    password VARCHAR(255) NOT NULL,
    estado ENUM('activo','inactivo') NOT NULL DEFAULT 'activo',
    ultimo_acceso DATETIME NULL
);

CREATE TABLE autores (
    id_autor INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    nacionalidad VARCHAR(80),
    fecha_nacimiento DATE NULL
);

CREATE TABLE libros (
    id_libro INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(150) NOT NULL,
    isbn VARCHAR(20) UNIQUE,
    anio_publicacion INT,
    stock INT NOT NULL DEFAULT 0,
    id_autor INT NOT NULL,
    FOREIGN KEY (id_autor) REFERENCES autores(id_autor)
);

CREATE TABLE prestamos (
    id_prestamo INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario VARCHAR(20) NOT NULL,
    id_libro INT NOT NULL,
    fecha_prestamo DATE NOT NULL,
    fecha_devolucion DATE NULL,
    estado ENUM('activo','devuelto') NOT NULL DEFAULT 'activo',
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario),
    FOREIGN KEY (id_libro) REFERENCES libros(id_libro)
);

INSERT INTO usuarios(id_usuario,nombre,direccion,tipo_usuario,password,estado,ultimo_acceso) VALUES
('admin1','Ana Bibliotecaria','admin@biblio.cl','bibliotecario','admin123','activo',NULL),
('sus001','Carlos Soto','carlos@correo.cl','suscriptor','sus001123','activo',NULL),
('sus002','María Díaz','maria@correo.cl','suscriptor','sus002123','inactivo',NULL);

INSERT INTO autores(nombre,nacionalidad,fecha_nacimiento) VALUES
('Gabriel García Márquez','Colombiana','1927-03-06'),
('Isabel Allende','Chilena','1942-08-02');

INSERT INTO libros(titulo,isbn,anio_publicacion,stock,id_autor) VALUES
('Cien años de soledad','9780307474728',1967,5,1),
('El amor en los tiempos del cólera','9780307389732',1985,2,1),
('La casa de los espíritus','9788401337208',1982,3,2);

INSERT INTO prestamos(id_usuario,id_libro,fecha_prestamo,estado)
VALUES ('sus001',1,CURDATE(),'activo');

UPDATE libros SET stock = stock - 1 WHERE id_libro = 1;
