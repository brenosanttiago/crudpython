create database db_voluntario;

use db_voluntario;

create table tb_voluntario(
	id int not null auto_increment primary key,
    nome varchar(30),
    idade int,
    telefone varchar(20)
);

select * from tb_voluntario;