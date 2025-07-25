create type strutturato as enum ('ricercatore', 'professore associato', 'professore ordinario');
create type lavoroprogetto as enum ('ricerca e sviluppo', 'dimostrazione', 'management', 'altro');
create type lavorononprogettuale as enum ('didattica', 'ricerca', 'missione', 'incontro dipartimentale', 'incontro accademico', 'altro');
create type causaassenza as enum ('chiusura universitaria', 'maternita', 'malattia');

create domain posinteger as integer check (value >= 0);
create domain stringam as varchar(100);
create domain numeroore as integer check (value >= 0 and value <= 8);
create domain denaro as real check (value >= 0);

create table persona (
    id posinteger primary key,
    nome stringam not null,
    cognome stringam not null,
    posizione strutturato not null, 
    stipendio denaro not null
);

create table progetto (
    id posinteger primary key, 
    nome stringam not null unique, 
    inizio date, 
    fine date,
    budget denaro not null,
    check (fine > inizio)
);

create table wp (
    progetto posinteger,
    id posinteger,
    nome stringam not null,
    inizio date,
    fine date,
    check (fine > inizio),
    unique (nome),
    primary key (progetto, id),
    foreign key (progetto) references progetto(id)
);

create table attivitaprogetto (
    id posinteger,
    persona posinteger,
    progetto posinteger,
    wp posinteger,
    giorno date,
    tipo lavoroprogetto not null,
     oreDurata numeroore not null,
    primary key (id),
    foreign key (persona) references persona(id),
    foreign key (progetto, wp) references wp(progetto, id)
);

create table attivitanonprogettuale (
    id posinteger primary key,
    persona posinteger,
    tipo lavorononprogettuale not null,
    giorno date,
    oreDurata numeroore not null,
    foreign key (persona) references persona(id)
);

create table assenza (
    id posinteger primary key,
    persona posinteger,
    tipo causaassenza not null,
    giorno date,
    unique (persona, giorno),
    foreign key (persona) references persona(id)
);
