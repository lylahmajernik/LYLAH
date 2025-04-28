CREATE TABLE IF NOT EXISTS TEAM
                    (ID         INTEGER      PRIMARY KEY,
                     Name       TEXT         NOT NULL    UNIQUE,
                     Manager    INTEGER      NOT NULL,
                     Wins       INTEGER      DEFAULT 0,
                     Losses     INTEGER      DEFAULT 0,
                     FOREIGN KEY(Manager) REFERENCES TRAINER(ID))STRICT