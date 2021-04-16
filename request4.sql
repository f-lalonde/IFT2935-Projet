    with id_mat_stages as (select id_entreprise, matricule_etudiant,
        matricule_professeur from stage_1),
    id_mat_visites as (select id_entreprise, matricule_etudiant, date_visite
    from visites),
    stages_visites as (select matricule_prof, date_visite
        from id_mat_stages natural join id_mat_visites),
    count_visites as (select matricule_prof, count(date_visite) as
        nb_visites from stages_visites group by matricule_prof),
    visits_gt_3 as (select matricule_prof from count_visites
        where nb_visites > 3),
    etudiants_visites as (select matricule_etudiant from visits_gt_3
        natural join stage_1),
    etudiants_programmes as (select etudiant_1.matricule, programme from
        etudiant_1 natural join etudiants_visites),
    select programme, count(matricule) as nb_etudiants from etudiants_programmes
    group by programme;
