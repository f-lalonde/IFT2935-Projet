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




    commit;
