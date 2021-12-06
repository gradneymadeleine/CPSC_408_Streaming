CREATE TABLE netflix(
show_id VARCHAR(10) NOT NULL PRIMARY KEY,
type ENUM('Movie', 'TV Show'),
title VARCHAR(50),
director VARCHAR(30),
cast VARCHAR(100),
country VARCHAR(20),
date_added VARCHAR(25),
release_year INTEGER,
rating VARCHAR(10),
duration VARCHAR(20)
);

CREATE TABLE hulu(
show_id VARCHAR(10) NOT NULL PRIMARY KEY,
type ENUM('Movie', 'TV Show'),
title VARCHAR(50),
director VARCHAR(30),
cast VARCHAR(100),
country VARCHAR(20),
date_added DATE,
release_year YEAR,
rating VARCHAR(10),
duration VARCHAR(20)
);

CREATE TABLE disney(
show_id VARCHAR(10) NOT NULL PRIMARY KEY,
type ENUM('Movie', 'TV Show'),
title VARCHAR(50),
director VARCHAR(30),
cast VARCHAR(100),
country VARCHAR(20),
date_added DATE,
release_year YEAR,
rating VARCHAR(10),
duration VARCHAR(20)
);

CREATE TABLE amazon(
show_id VARCHAR(10) NOT NULL PRIMARY KEY,
type ENUM('Movie', 'TV Show'),
title VARCHAR(50),
director VARCHAR(30),
cast VARCHAR(100),
country VARCHAR(20),
date_added DATE,
release_year YEAR,
rating VARCHAR(10),
duration VARCHAR(20)
);
