CREATE DATABASE Archivos_variados;
USE Archivos_variados;

CREATE TABLE archivos_documentos (id INT, nombre_archivo VARCHAR(255), formato_archivo VARCHAR(255));
CREATE TABLE archivos_audio (id INT, nombre_archivo VARCHAR(255), formato_archivo VARCHAR(255));
CREATE TABLE archivos_video (id INT, nombre_archivo VARCHAR(255), formato_archivo VARCHAR(255));
CREATE TABLE archivos_imagen (id INT, nombre_archivo VARCHAR(255), formato_archivo VARCHAR(255));

INSERT INTO archivos_documentos (nombre_archivo, formato_archivo) VALUES ("texto", "txt");

INSERT INTO archivos_audio (nombre_archivo, formato_archivo) VALUES ("audio1", "mp3"),
("audio2", "flac");

INSERT INTO archivos_video (nombre_archivo, formato_archivo) VALUES ("video", "mp4");

INSERT INTO archivos_imagen (nombre_archivo, formato_archivo) VALUES ("imagen", "jpg");
