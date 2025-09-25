create domain stringa as varchar;

create domain partitaiva as char(11)
	check (value ~ '[0-9]{11}');

create domain partitaiva as char(11)
	check (value ~ '[A-Z]{6}[0-9]{2}[A-Z][0-9]{2}[A-Z][0-9]{3}[A-Z]');

create domain CAP as char(5)
	check (value ~ '[0-9]{5}');

create type indirizzo as (
	via stringa,
	civico stringa,
	cap CAP
);

create domain Telefono as varchar(15);

create domain email as varchar
	check (value ~ '^[A-Z0-9._%+-]++@(?:[A-Z0-9-]++\.)++[A-Z]{2,}+$');

create type StatoOrdineEnum as enum (
	'In Preparazione', 'Inviato', 'Da Saldare' ,'Saldato'
);

create domain IntGEZ as integer
	check (value >= 0);


create domain RealGEZ as real
	check (value >= 0);


create domain Real_0_1 as RealGEZ
	check (value <= 1);





create table statoordine (
	id serial primary key,
	nome stringa not null,
	unique(nome)
);

create table nazione (
	nome stringa primary key
);

create table regione (
	nome stringa not null,
	nazione stringa not null,
	primary key (nome, nazione),

	foreign key (nazione)
		references nazione(nome)
);

create table citta (
	id serial primary key,
	nome stringa not null,
	regione stringa not null,
	nazione stringa not null,
	unique(nome, regione, nazione)
);


create table direttore (
	cf codicefiscale primary key,
	nome stringa not null,
	cognome stringa not null,
	anni_servizio intgez not null,
	data_nascita date not null,
	cit_nasc integer not null,
	foreign key (cit_nasc)
		references citta(id)
);

create table dipartimento (
	nome stringa primary key,
	indirizzo indirizzo not null,
	dip_dir codicefiscale not null,
	foreign key (dip_dir)
		references direttore(cf),
	dip_cit integer not null,
	foreign key (dip_cit)
		references citta(id)
);

create table fornitore (
	partita_iva partitaiva primary key,
	ragione_sociale stringa not null,
	indirizzo indirizzo not null,
	telefono telefono not null,
	email email not null,
	cit_forn integer not null,
	foreign key (cit_forn)
		references citta(id)
);

create table ordine (
	codice serial primary key,
	data_stipula date not null,
	imponibile realgez not null,
	aliquota real_0_1 not null,
	descrizione stringa not null,
	dip_ord stringa not null,
	foreign key (dip_ord)
		references dipartimento(nome),
	stat_ord stringa not null,
	foreign key (stat_ord)
		references statoordine(nome),

	fornitore partitaiva not null,
	foreign key (fornitore)
		references fornitore(partitaiva)
);
