create table tbl_movie_category(
    category_id int unsigned auto_increment,
    category_name varchar(100) not null,
    category_desc varchar(100) default "Sin descripción",
    primary key(category_id),
    unique u_category(category_name)
);CREATE DATABASE `moviesdb` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;


