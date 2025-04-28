CREATE TABLE IF NOT EXISTS MEMBERSHIP
                    (PokemonID    INTEGER,
                     TeamID       INTEGER,
                     FOREIGN KEY(PokemonID) REFRENCES POKEMON(ID),
                     FOREIGN KEY(TeamID) REFRENCES TEAM(ID))STRICT
