create table estudiantes
(
    id      int auto_increment
        primary key,
    usuario varchar(200) null,
    sueldo  double       null
);

INSERT INTO paises.estudiantes (id, usuario, sueldo) VALUES (1, 'reroes', 2000.1);
INSERT INTO paises.estudiantes (id, usuario, sueldo) VALUES (2, 'usuario002', 200.2);