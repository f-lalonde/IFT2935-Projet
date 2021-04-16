begin transaction;

    with count_prenoms as (select matricule, count(prenom) as nb_prenoms from
        prenoms group by matricule),
    with prenoms_gte_2 as (select matricule from count_prenoms where
        nb_prenoms >= 2),
    with mat_performants as (select matricule from etudiant_1 where
        credits_completes >= 30 and gpa >= 3.7)
    select * from prenoms_gte_2 natural join mat_performants);

    with curr_stages as (select matricule_professeur, matricule_etudiant,
        id_entreprise from stage_1 where date_debut > 2021-01-01),
    with students_entreprises_gte_2 as (select matricule_professeur,
        count(matricule_etudiant)as nb_students,
        count(nb_entreprises) as nb_entreprises
        from curr_stages group by matricule_professeur where nb_students >= 2
        and nb_entreprises >= 2),
    with busy_profs as (select matricule_professeur
        from students_entreprises_gte2),
    with busy_profs_discipline as (select matricule_professeur, discipline from
        busy_profs join professeur_1
        on busy_profs.matricule_professeur = professeur_1.matricule),
    with busy_profs_faculte as (select matricule, facultes from
        busy_profs_discipline natural join professeur_2),
    with infos as (select nom_personne, courriel_personne, matricule from personne),
    select matricule, nom_personne, courriel_personne, faculte
    from busy_profs_faculte natural join infos;

    with stages_5ans as (select id_entreprise, matricule_etudiant from stage_1
        where date_debut > 2016-01-01),
    with etudiants_chimie as (select matricule from etudiant_1
        where programme = "Chimie"),
    with stages_etudiants_chimie as (select id_entreprise, matricule_etudiant
        from stages_5ans natural join etudiants_chimie),
    with nb_stagiaires as (select id_entreprise,
        count(matricule_etudiant) as nb_etudiants from stages_etudiants_chimie
        group by id_entreprise),
    with id_entreprises as (select id_entreprise from nb_stagiaires
        where nb_etudiants >= 2),
    with infos_entreprise as (select id_entreprise, nom_entreprise,
        courriel_entreprise from entreprise),
    with codes_id as (select id_entreprise, code_postal from adresses),
    with codes_quebec as (select code_postal from code_postal where
        province = "QC"),
    with id_quebec as (select id_entreprise from codes natural
        join codes_quebec),
    with infos_quebec as (select id_entreprise, nom_entreprise,
        courriel_entreprise from infos_entreprise natural join id_quebec),
    select id_entreprise, nom_entreprise, courriel_entreprise from infos_quebec
    natural join id_entreprises);


    commit;
