create table tbl_movie_category(
    category_id int unsigned auto_increment,
    category_name varchar(100) not null,
    category_desc varchar(100) default "Sin descripción",
    primary key(category_id),
    unique u_category(category_name)
);CREATE DATABASE `moviesdb` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

alter table tbl_movie_category modify category_desc varchar(250);

create table tbl_classification(
    classification_id int unsigned auto_increment,
    classification_name varchar(3) not null,
    classification_desc varchar(100) default "Sin descripción",
    primary key(classification_id),
    unique u_category(classification_desc )
);CREATE DATABASE `moviesdb` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;


create table tbl_movies(
    movie_id int unsigned auto_increment,
    name_movie varchar(100) not null,
    lauch_year varchar(4) not null,
    sinopsis varchar(255) not null,
    duration varchar(20) not null,
    category_id int(3) unsigned not null,
    classification_id int(3) unsigned not null,
    primary key(movie_id),
    CONSTRAINT FK_category_id FOREIGN KEY (category_id) REFERENCES tbl_movie_category(category_id),
    CONSTRAINT FK_classification_id FOREIGN KEY (classification_id) REFERENCES tbl_classification(classification_id)
);CREATE DATABASE `moviesdb` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
