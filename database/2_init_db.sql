begin transaction;
set search_path to projet_ift_2935;

create table personne
(
	matricule int primary key,
	code_postal text not null,
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
	matricule int not null,
	prenom text not null,
	foreign key (matricule) references personne(matricule),
	primary key(matricule, prenom)
);

create table etudiant
(
	matricule int unique not null,
	programme programmes not null,
	credits_completes int,
	gpa float,
	foreign key (matricule) references personne(matricule), 
	constraint gpa_check check(gpa >= 0 and gpa <= 4.3),
	constraint credits_pos check(credits_completes >= 0)
);

	
create table professeur
(
	matricule int not null,
	discipline disciplines not null,
	foreign key (matricule) references personne(matricule)
);

create table programmes_departements
(
	programme programmes primary key,
	faculte facultes not null,
	discipline disciplines not null
);

create table code_postal
(
	code_postal text primary key,
	ville text not null,
	province text not null
);


create table entreprise
(
	id_entreprise int primary key,
	nom_entreprise text not null,
	courriel_entreprise text not null,
	telephone_entreprise text not null,
	participante bool not null default true,
	domaine text
);


create table adresses
(
	id_entreprise int not null,
	code_postal text not null,
	no_entreprise int not null,
	rue_entreprise text not null,
	foreign key (id_entreprise) references entreprise(id_entreprise),
	primary key(id_entreprise, code_postal, no_entreprise, rue_entreprise)
);

create table stage_1
(
	id_entreprise int not null,
	matricule_etudiant int not null,
	matricule_professeur int not null,
	poste text not null, 
	date_debut date primary key,
	date_fin date,
	heures_travaillees numeric(4,2),
	foreign key (id_entreprise) references entreprise(id_entreprise),
	foreign key (matricule_etudiant) references personne(matricule),
	foreign key (matricule_professeur) references personne(matricule)
);

create table stage_2
(
	poste text primary key,
	salaire_horaire numeric(6,2)
);


create table visites
(
	id_entreprise int not null,
	matricule_etudiant int not null,
	date_debut date not null,
	date_fin date,
	date_visite date,
	foreign key (id_entreprise) references entreprise(id_entreprise),
	foreign key (matricule_etudiant) references etudiant(matricule),
	foreign key (date_debut) references stage_1(date_debut),
	primary key (id_entreprise, matricule_etudiant, date_debut, date_visite),
	constraint check_date check(date_visite >= date_debut and date_visite <= date_fin)
);

commit;