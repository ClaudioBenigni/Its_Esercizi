create domain stringa as varchar;

create domain Anno as Integer check (value>0 and value <=2026);

create domain IntGZ as integer check (value >0);

create table Volo (
    codice stringa primary key,
    durata_min IntGZ not null,
);

create table Aereoporto (
    codice stringa primary key,
    nome stringa non null,
);

create table Compagnia(
    nome stringa primary key,
    anno Anno not null
);

create table Città(
    nome stringa primary key,
    abitanti IntGZ not null,
);

create table Nazione(
    nome stringa primary key,
);