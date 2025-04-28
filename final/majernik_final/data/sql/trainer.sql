CREATE TABLE IF NOT EXISTS TRAINER
                    (ID         INTEGER      PRIMARY KEY,
                     Name       TEXT         NOT NULL UNIQUE,
                     Email      TEXT,
                     Phone      INTEGER,
                     Team       INTEGER)STRICT
                                                