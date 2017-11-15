CREATE TABLE PROXY(
   ID INTEGER PRIMARY KEY     AUTOINCREMENT,
   IP             CHAR(50)    NOT NULL,
   PORT           CHAR(50)     NOT NULL,
   FP             CHAR(50)     NOT NULL UNIQUE,
   DELAY          DOUBLE
);