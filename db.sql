CREATE TABLE investment(
  id INTEGER PRIMARY KEY,
  title TEXT,
  amount_invested REAL,
  date_start TIMESTAMP,
  confirmation_of_start NUMERIC,
  date_end TIMESTAMP,
  profit REAL,
  confirmation_of_withdrawal NUMERIC,
  FOREIGN KEY (title) REFERENCES title (alias)
);

CREATE TABLE title(
  id INTEGER PRIMARY KEY,
  name VARCHAR(50),
  alias TEXT
)