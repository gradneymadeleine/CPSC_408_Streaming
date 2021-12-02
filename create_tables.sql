CREATE TABLE netflix(
show_id VARCHAR(10) NOT NULL PRIMARY KEY,
show_movie VARCHAR(10),
title VARCHAR(50),
director VARCHAR(30),
actors VARCHAR(1000),
country VARCHAR(20),
date_added VARCHAR(20),
release_year INTEGER,
rating VARCHAR(10),
duration VARCHAR(20),
listed_in VARCHAR(20),
summary VARCHAR(1000)
);

CREATE TABLE hulu(
show_id VARCHAR(10) NOT NULL PRIMARY KEY,
type ENUM('Movie', 'TV Show'),
title VARCHAR(50),
director VARCHAR(30),
cast LONGTEXT,
country VARCHAR(20),
date_added DATE,
release_year YEAR,
rating VARCHAR(10),
duration VARCHAR(20),
listed_in VARCHAR(20),
description LONGTEXT
);

CREATE TABLE disney(
show_id VARCHAR(10) NOT NULL PRIMARY KEY,
type ENUM('Movie', 'TV Show'),
title VARCHAR(50),
director VARCHAR(30),
cast LONGTEXT,
country VARCHAR(20),
date_added DATE,
release_year YEAR,
rating VARCHAR(10),
duration VARCHAR(20),
listed_in VARCHAR(20),
description LONGTEXT
);
