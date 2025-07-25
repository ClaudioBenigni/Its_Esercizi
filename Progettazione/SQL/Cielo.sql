create domain PosInteger as integer
check (value >= 0);

create domain StringaM as varchar (100);

create domain CodIATA as char (3);

create table Compagnia (
    nome StringaM not null,
    annoFondaz PosInteger,
    primary key (nome)
);

create table Aeroporto (
    codice CodIATA not null,
    nome StringaM not null,
    primary key (codice)
);

create table LuogoAeroporto (
    aeroporto CodIATA not null,
    citta StringaM not null,
    nazione StringaM not null,
    primary key (aeroporto),
    foreign key (aeroporto) references Aeroporto(codice)
);

create table Volo (
    codice PosInteger not null,
    comp StringaM not null,
    durataMinuti PosInteger,
    primary key (codice, comp),
    foreign key (comp) references Compagnia(nome)
);

create table ArrPart (
    codice PosInteger,
    comp StringaM not null,
    arrivo CodIATA not null,
    partenza CodIATA not null,
    primary key (codice, comp),
    foreign key (codice, comp) references Volo(codice, comp),
    foreign key (arrivo) references Aeroporto(codice),
    foreign key (partenza) references Aeroporto(codice)
);




