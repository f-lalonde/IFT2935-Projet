begin transaction;
set search_path to projet_ift_2935;
INSERT INTO entreprise VALUES (833506, 'Hydro-Québec', 'hydro-quebec@communications.hydro.qc.ca', '(514)385-7252', True, 'Énergie');
INSERT INTO adresses VALUES (833506, 'H1B5K8', 75, 'boulevard René-Lévesque Ouest');
INSERT INTO entreprise VALUES (146970, 'Desjardins', 'contactdesjardins@desjardins.com', '(514)281-7101', True, 'Financier');
INSERT INTO adresses VALUES (146970, 'H1C0B2', 5, 'Rue Complexe Desjardins Bureau 226');
INSERT INTO entreprise VALUES (460554, 'Desjardins', 'contactdesjardins2@desjardins.com', '(418)833-5515', True, 'Financier');
INSERT INTO adresses VALUES (460554, 'G6V0M5', 995, 'boulevard Alphonse-Desjardins');
INSERT INTO entreprise VALUES (586929, 'Loto-Québec', 'jeuxenligne@lotoquebec.com', '(866)611-5686', True, 'Jeux et loteries');
INSERT INTO adresses VALUES (586929, 'H1E1A7', 500, 'rue Sherbrooke Ouest');
INSERT INTO entreprise VALUES (483632, 'Matério', 'emplois@materio.ca', '(450)438-9780', True, 'Matériel de construction');
INSERT INTO adresses VALUES (483632, 'J5L0A1', 2159, 'boulevard Curé-Labelle');
INSERT INTO entreprise VALUES (120090, 'Poulet en Folie', 'pouletpoulet@poulet.qc.ca', '(438)444-1919', True, 'Délicieux poulet');
INSERT INTO adresses VALUES (120090, 'G0Y1H0', 2020, 'rue du Finfin');
INSERT INTO entreprise VALUES (3578325, 'Aperture Science', 'dontbeshell@aperture.evil', '(514)555-5555', True, 'Science Expérimentale');
INSERT INTO adresses VALUES (3578325, 'B1G0B4', 666, 'Avenue GLaDOS');
INSERT INTO entreprise VALUES (933852, 'Big Metal Fan', 'pushit@toelev.en', '(819)832-1234', True, 'Acierie et musique');
INSERT INTO adresses VALUES (933852, 'B3L5S8', 420, 'rang Enfumé');
INSERT INTO entreprise VALUES (99261207, 'Pas la Mafia', 'nousommes@legit.ok', '(666)123-0987', True, 'Do not ask');
INSERT INTO adresses VALUES (99261207, 'T0B4N1', 111, 'boulevard Sanglant');
INSERT INTO entreprise VALUES (5222182, 'Twiggs', 'sax@trompette.fwiiit', '(514)802-6969', True, 'Fabriquant instruments à vent');
INSERT INTO adresses VALUES (5222182, 'H2T3E2', 42, 'Place Gillespie');
INSERT INTO entreprise VALUES (2720226, 'Vric à Vrac', 'noixdegrenobles@vrac.com', '(450)889-2776', True, 'Alimentation');
INSERT INTO adresses VALUES (2720226, 'J0P1Y', 10092, 'Rang Profond');
commit;