CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    passwd TEXT NOT NULL
);

/*  Regarding the Flaw 3: Broken authentication: uses plain text passwords (see users.py line 35).
Line 4: Fix by changing column "passwd" to "password". */

CREATE TABLE notes (
  id SERIAL PRIMARY KEY,
  note TEXT
);