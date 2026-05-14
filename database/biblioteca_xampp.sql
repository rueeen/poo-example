-- Script de base de datos para importar en XAMPP (MySQL/MariaDB)
-- Recomendado: importar desde phpMyAdmin

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

DROP DATABASE IF EXISTS `biblioteca`;
CREATE DATABASE IF NOT EXISTS `biblioteca` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE `biblioteca`;

CREATE TABLE `usuarios` (
  `id_usuario` varchar(20) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `direccion` varchar(200) DEFAULT NULL,
  `tipo_usuario` enum('bibliotecario','suscriptor') NOT NULL,
  `password` varchar(255) NOT NULL,
  `estado` enum('activo','inactivo') NOT NULL DEFAULT 'activo',
  `ultimo_acceso` datetime DEFAULT NULL,
  PRIMARY KEY (`id_usuario`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `autores` (
  `id_autor` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `nacionalidad` varchar(80) DEFAULT NULL,
  `fecha_nacimiento` date DEFAULT NULL,
  PRIMARY KEY (`id_autor`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `libros` (
  `id_libro` int(11) NOT NULL AUTO_INCREMENT,
  `titulo` varchar(150) NOT NULL,
  `isbn` varchar(20) DEFAULT NULL,
  `anio_publicacion` int(11) DEFAULT NULL,
  `stock` int(11) NOT NULL DEFAULT 0,
  `id_autor` int(11) NOT NULL,
  PRIMARY KEY (`id_libro`),
  UNIQUE KEY `isbn` (`isbn`),
  KEY `id_autor` (`id_autor`),
  CONSTRAINT `libros_ibfk_1` FOREIGN KEY (`id_autor`) REFERENCES `autores` (`id_autor`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `prestamos` (
  `id_prestamo` int(11) NOT NULL AUTO_INCREMENT,
  `id_usuario` varchar(20) NOT NULL,
  `id_libro` int(11) NOT NULL,
  `fecha_prestamo` date NOT NULL,
  `fecha_devolucion` date DEFAULT NULL,
  `estado` enum('activo','devuelto') NOT NULL DEFAULT 'activo',
  PRIMARY KEY (`id_prestamo`),
  KEY `id_usuario` (`id_usuario`),
  KEY `id_libro` (`id_libro`),
  CONSTRAINT `prestamos_ibfk_1` FOREIGN KEY (`id_usuario`) REFERENCES `usuarios` (`id_usuario`),
  CONSTRAINT `prestamos_ibfk_2` FOREIGN KEY (`id_libro`) REFERENCES `libros` (`id_libro`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

INSERT INTO `usuarios` (`id_usuario`, `nombre`, `direccion`, `tipo_usuario`, `password`, `estado`, `ultimo_acceso`) VALUES
('admin1','Ana Bibliotecaria','admin@biblio.cl','bibliotecario','admin123','activo',NULL),
('sus001','Carlos Soto','carlos@correo.cl','suscriptor','sus001123','activo',NULL),
('sus002','María Díaz','maria@correo.cl','suscriptor','sus002123','inactivo',NULL);

INSERT INTO `autores` (`nombre`,`nacionalidad`,`fecha_nacimiento`) VALUES
('Gabriel García Márquez','Colombiana','1927-03-06'),
('Isabel Allende','Chilena','1942-08-02');

INSERT INTO `libros` (`titulo`,`isbn`,`anio_publicacion`,`stock`,`id_autor`) VALUES
('Cien años de soledad','9780307474728',1967,5,1),
('El amor en los tiempos del cólera','9780307389732',1985,2,1),
('La casa de los espíritus','9788401337208',1982,3,2);

INSERT INTO `prestamos` (`id_usuario`,`id_libro`,`fecha_prestamo`,`estado`)
VALUES ('sus001',1,CURDATE(),'activo');

UPDATE `libros` SET `stock` = `stock` - 1 WHERE `id_libro` = 1;

COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
