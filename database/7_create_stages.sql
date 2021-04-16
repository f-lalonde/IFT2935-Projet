begin transaction;
set search_path to projet_ift_2935;

INSERT INTO stage_1 values (120090, 6267377, 4767982, 'Développeur full stack', '2021-06-02', '2021-09-03', 37.5);
INSERT INTO stage_2 values ('Développeur full stack', 18.5);

INSERT INTO stage_1 values (460554, 15708823, 168372, 'Assassin de fraudeurs', '2019-01-12', '2019-01-13', 37.5);
INSERT INTO stage_2 values ('Assassin de fraudeurs', 128.5);

INSERT INTO stage_1 values (933852, 901542, 4767982, 'Guitariste en salle d opération', '2021-02-09', '2021-10-30', 18);
INSERT INTO stage_2 values ('Guitariste en salle d opération', 27.25);

INSERT INTO stage_1 values (933852, 901542, 4767982, 'Bassiste en profondeur', '2019-12-12', '2020-04-17', 22);
INSERT INTO stage_2 values ('Bassiste en profondeur', 32);

INSERT INTO stage_1 values (3578325, 42929910, 378852, 'Testeur de portails', '2002-01-27', '2222-01-27', 99);
INSERT INTO stage_2 values ('Testeur de portails', 0.01);

INSERT INTO stage_1 values (586929, 8785998, 41019719, 'Nettoyeur de boules 6/49', '2021-05-12', '2021-08-31', 12.25);
INSERT INTO stage_2 values ('Nettoyeur de boules 6/49', 18.5);

INSERT INTO stage_1 values (2720226, 99105013, 4767982, 'Décorticeur de noix de grenobles', '2018-11-04', '2019-04-17', 35);
INSERT INTO stage_2 values ('Décorticeur de noix de grenobles', 12);

INSERT INTO stage_1 values (99261207, 738210, 2233107, 'Définitivement pas un nettoyeur de monnaie sale', '2021-03-21', '2021-09-13', 51.2);
INSERT INTO stage_2 values ('Définitivement pas un nettoyeur de monnaie sale', 175);

INSERT INTO stage_1 values (833506, 172756, 2233107, 'Agent au lichage de batteries 9V', '2021-03-10', '2021-07-11', 24.5);
INSERT INTO stage_2 values ('Agent au lichage de batteries 9V', 42.15);

INSERT INTO stage_1 values (833506, 3199042, 4767982, 'Recocombulateur de lignes diazéphanicothriptyches', '2021-09-01', '2022-04-28', 32);
INSERT INTO stage_2 values ('Recocombulateur de lignes diazéphanicothriptyches', 55);

INSERT INTO stage_1 values (146970, 32452731, 36040903, 'Biochimiste en récupération de cartes bancaires', '1997-01-01', '2002-05-17', 3);
INSERT INTO stage_2 values ('Biochimiste en récupération de cartes bancaires', 17.25);

INSERT INTO stage_1 values (5222182, 788460, 2901329, 'Gosseur d anches doubles, spécialisation roseau', '2021-01-12', '2021-07-18', 29.75);
INSERT INTO stage_2 values ('Gosseur d anches doubles, spécialisation roseau', 33.3);


INSERT INTO visites values (5222182, 788460, '2021-01-12', '2021-07-18', '2021-02-02');
INSERT INTO visites values (5222182, 788460, '2021-01-12', '2021-07-18', '2021-03-05');
INSERT INTO visites values (5222182, 788460, '2021-01-12', '2021-07-18', '2021-06-18');

INSERT INTO visites values (99261207, 738210, '2021-03-10', '2021-07-11', '2021-03-12');
INSERT INTO visites values (99261207, 738210, '2021-03-10', '2021-07-11', '2021-05-15');

INSERT INTO visites values (833506, 3199042, '2021-09-01', '2022-04-28', '2021-10-12');
INSERT INTO visites values (833506, 3199042, '2021-09-01', '2022-04-28', '2022-02-24');

INSERT INTO visites values (833506, 172756, '2021-03-10', '2021-07-11', '2021-03-17');
INSERT INTO visites values (833506, 172756, '2021-03-10', '2021-07-11', '2021-06-29');

INSERT INTO visites values (2720226, 99105013, '2018-11-04', '2019-04-17', '2019-03-17');
INSERT INTO visites values (2720226, 99105013, '2018-11-04', '2019-04-17', '2018-12-14');

INSERT INTO visites values (3578325, 42929910, '2002-01-27', '2222-01-27', '2121-03-17');

INSERT INTO visites values (120090, 6267377, '2021-06-02', '2021-09-03', '2021-07-17');
INSERT INTO visites values (120090, 6267377, '2021-06-02', '2021-09-03', '2021-08-09');

INSERT INTO visites values (146970, 32452731, '1997-01-01', '2002-05-17', '1997-01-01');
INSERT INTO visites values (146970, 32452731, '1997-01-01', '2002-05-17', '1999-12-31');

commit;