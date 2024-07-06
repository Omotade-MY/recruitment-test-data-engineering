DROP TABLE IF EXISTS places;

CREATE TABLE places (
    id INT AUTO_INCREMENT PRIMARY KEY,
    city VARCHAR(255) NOT NULL,
    county VARCHAR(255),
    country VARCHAR(255),
    UNIQUE (city)
);

DROP TABLE IF EXISTS people;

CREATE TABLE people (
    id INT AUTO_INCREMENT PRIMARY KEY,
    given_name VARCHAR(255) NOT NULL,
    family_name VARCHAR(255) NOT NULL,
    date_of_birth DATE NOT NULL,
    place_of_birth VARCHAR(255),
    FOREIGN KEY (place_of_birth) REFERENCES places(city)
);
