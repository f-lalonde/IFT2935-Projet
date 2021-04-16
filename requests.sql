begin transaction;

    with count_prenoms as (select matricule, count(prenom) as nb_prenoms from
        prenoms group by matricule),
    with prenoms_gte_2 as (select matricule from count_prenoms where
        nb_prenoms >= 2),
    with mat_performants as (select matricule from etudiant_1 where
        credits_completes >= 30 and gpa >= 3.7)
    select * from prenoms_gte_2 natural join mat_performants);

    commit;
