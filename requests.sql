begin transaction;

    with count_prenoms as (select matricule, count(prenom) as nb_prenoms from
        prenoms group by matricule),
    prenoms_gte_2 as (select matricule from count_prenoms where
        nb_prenoms >= 2),
    mat_performants as (select matricule from etudiant where
        credits_completes >= 30 and gpa >= 3.7)
    select * from prenoms_gte_2 natural join mat_performants;


    with curr_stages as (select matricule_professeur, matricule_etudiant,
        id_entreprise from stage_1 where date_debut > '2021-01-01'),
    students_entreprises_gte_2 as (select matricule_professeur,
        count(matricule_etudiant) as nb_students,
        count(id_entreprise) as nb_entreprises
        from curr_stages group by matricule_professeur),
    busy_profs as (select matricule_professeur
        from students_entreprises_gte_2),
    busy_profs_discipline as (select matricule, discipline from
        busy_profs join professeur
        on busy_profs.matricule_professeur = professeur.matricule),
    busy_profs_faculte as (select matricule, faculte from
        busy_profs_discipline natural join programmes_departements),
    infos as (select nom_personne, courriel_personne, matricule from personne)
    select matricule, nom_personne, courriel_personne, faculte
    from busy_profs_faculte natural join infos;

    with stages_5ans as (select id_entreprise, matricule_etudiant from stage_1
        where date_debut > '2016-01-01'),
    etudiants_chimie as (select matricule from etudiant
        where programme = 'Chimie'),
    stages_etudiants_chimie as (select id_entreprise, matricule_etudiant
        from stages_5ans natural join etudiants_chimie),
    nb_stagiaires as (select id_entreprise,
        count(matricule_etudiant) as nb_etudiants from stages_etudiants_chimie
        group by id_entreprise),
    id_entreprises as (select id_entreprise from nb_stagiaires
        where nb_etudiants >= 2),
    infos_entreprise as (select id_entreprise, nom_entreprise,
        courriel_entreprise from entreprise),
    codes_id as (select id_entreprise, code_postal from adresses),
    codes_quebec as (select code_postal from code_postal where
        province = 'Québec'),
    id_quebec as (select id_entreprise from entreprise natural
        join codes_quebec),
    infos_quebec as (select id_entreprise, nom_entreprise,
        courriel_entreprise from infos_entreprise natural join id_quebec)
    select id_entreprise, nom_entreprise, courriel_entreprise from infos_quebec
    natural join id_entreprises;

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

    commit;
