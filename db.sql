CREATE TABLE investment(
  id INTEGER PRIMARY KEY,
  title TEXT,
  amount REAL,
  date_start TIMESTAMP,
  confirmation_of_start NUMERIC,
  date_end TIMESTAMP,
  profit REAL,
  confirmation_of_withdrawal NUMERIC,
  population_id INTEGER,
  FOREIGN KEY (population_id) REFERENCES population (id),
  FOREIGN KEY (title) REFERENCES title (alias)
);

CREATE TABLE population(
  id INTEGER PRIMARY KEY,
  title TEXT,
  date_start TIMESTAMP,
  date_end TIMESTAMP

);

CREATE TABLE title(
  id INTEGER PRIMARY KEY,
  name VARCHAR(50),
  alias TEXT
);

CREATE INDEX timestart on investment (date_start);
