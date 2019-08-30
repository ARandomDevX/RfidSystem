CREATE TABLE student(

id int NOT NULL,
fname varchar(255) NOT NULL,
lname varchar(255),
klasse varchar(2),

PRIMARY KEY (id)
);

CREATE TABLE notfall(
id int NOT NULL,
erw1 text NOT NULL,
erw2 text NOT NULL,
addr text NOT NULL,
n1 int NOT NULL,
n2 int NOT NULL,
klasse varchar(2) NOT NULL,

PRIMARY KEY (id)

);

CREATE TABLE status(
id int NOT NULL,
ort text NOT NULL,

PRIMARY KEY (id)
);

CREATE TABLE meldung(
ort text NOT NULL,
id int NOT NULL,
zeit text NOT NULL,
incident text NOT NULL,

PRIMARY KEY (id)
);
