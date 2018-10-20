CREATE TABLE Patient
(
    Pid INT NOT NULL ,
    Pname VARCHAR COLLATE utf8_bin NOT NULL,
    Pgender VARCHAR COLLATE utf8_bin NOT NULL,
    Ptel INT NOT NULL,
    Paddress VARCHAR COLLATE utf8_bin NOT NULL,
    Did INT NOT NULL,
    Dname VARCHAR COLLATE utf8_bin NOT NULL,
    PRIMARY KEY (Pid),
    FOREIGN KEY (Did) REFERENCES Disease(Did),
)

CREATE TABLE Disease
(
    Did INT NOT NULL ,
    Dname VARCHAR COLLATE utf8_bin NOT NULL,
    Dinfect BOOLEAN NOT NULL,
    PRIMARY KEY (Did),
)

CREATE TABLE Doctor
(
    DOid INT NOT NULL ,
    DOname VARCHAR COLLATE utf8_bin NOT NULL,
    DOgender VARCHAR COLLATE utf8_bin NOT NULL,
    DOtel INT NOT NULL,
    DOposition VARCHAR COLLATE utf8_bin NOT NULL,
    PRIMARY KEY (DOid),
)