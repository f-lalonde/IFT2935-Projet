begin transaction;

create table personne
(
	matricule text primary key,
	code_postal text not null unique,
	nom_personne text not null,
	date_naissance date not null,
	faculte facultes,
	telephone_personne text,
	courriel_personne text not null,
	no_personne int not null,
	constraint age_personne check(date_naissance >= '1900-01-01')
);

create table prenoms
(
	matricule text not null,
	prenom text not null,
	primary key(prenom),
	foreign key (matricule) references personne(matricule)
);

create table etudiant_1
(
	matricule text unique not null,
	programme programmes unique not null,
	credits_completes int,
	gpa float,
	foreign key (matricule) references personne(matricule), 
	constraint gpa_check check(gpa >= 0 and gpa <= 4.3),
	constraint credits_pos check(credits_completes >= 0)
);

create table etudiant_2
(
	programme programmes not null,
	faculte facultes not null,
	foreign key (programme) references etudiant_1(programme)
);

	
create table professeur_1
(
	matricule text not null,
	discipline disciplines unique not null,
	foreign key (matricule) references personne(matricule)
);

create table professeur_2
(
	discipline disciplines not null,
	faculte facultes not null,
	foreign key (discipline) references professeur_1(discipline)
);

create table code_postal
(
	code_postal text not null,
	ville text not null,
	province text not null,
	foreign key (code_postal) references personne(code_postal)
);


create table entreprise
(
	id_entreprise text primary key,
	nom_entreprise text not null,
	courriel_entreprise text not null,
	telephone_entreprise text not null,
	participante bool not null default true,
	domaine text
);


create table adresses
(
	id_entreprise text not null,
	code_postal text not null,
	no_entreprise int not null,
	rue_entreprise text not null,
	primary key(code_postal, no_entreprise, rue_entreprise),
	foreign key (id_entreprise) references entreprise(id_entreprise)
);

create table stage_1
(
	id_entreprise text not null,
	matricule_etudiant text not null,
	matricule_professeur text not null,
	poste text unique not null, 
	date_debut date primary key,
	date_fin date,
	heures_travaillees numeric(4,2),
	foreign key (id_entreprise) references entreprise(id_entreprise),
	foreign key (matricule_etudiant) references personne(matricule),
	foreign key (matricule_professeur) references personne(matricule)
);

create table stage_2
(
	poste text not null,
	salaire_horaire numeric(6,2),
	foreign key (poste) references stage_1(poste)
);


create table visites
(
	id_entreprise text not null,
	matricule_etudiant text not null,
	date_debut date not null,
	date_fin date,
	date_visite date,
	foreign key (id_entreprise) references entreprise(id_entreprise),
	foreign key (matricule_etudiant) references etudiant_1(matricule),
	foreign key (date_debut) references stage_1(date_debut),
	constraint check_date check(date_visite >= date_debut and date_visite <= date_fin)
);

commit;