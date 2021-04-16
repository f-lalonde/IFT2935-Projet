import datetime
import io
import math
import random

boy = ["Jacob", "Michael", "Ethan", "Joshua", "Daniel", "Alexander", "Anthony",
       "William", "Christopher", "Matthew", "Jayden", "Andrew", "Joseph", "David", "Noah", "Aiden", "James", "Ryan",
       "Logan", "John", "Nathan", "Elijah", "Christian", "Gabriel", "Benjamin", "Jonathan", "Tyler", "Samuel",
       "Nicholas", "Gavin", "Dylan", "Jackson", "Brandon", "Caleb", "Mason", "Angel", "Isaac", "Evan", "Jack", "Kevin",
       "Jose", "Isaiah", "Luke", "Landon", "Justin", "Lucas", "Zachary", "Jordan", "Robert", "Aaron", "Brayden",
       "Thomas", "Cameron", "Hunter", "Austin", "Adrian", "Connor", "Owen", "Aidan", "Jason", "Julian", "Wyatt",
       "Charles", "Luis", "Carter", "Juan", "Chase", "Diego", "Jeremiah", "Brody", "Xavier", "Adam", "Carlos",
       "Sebastian", "Liam", "Hayden", "Nathaniel", "Henry", "Jesus", "Ian", "Tristan", "Bryan", "Sean", "Cole", "Alex",
       "Eric", "Brian", "Jaden", "Carson", "Blake", "Ayden", "Cooper", "Dominic", "Brady", "Caden", "Josiah", "Kyle",
       "Colton", "Kaden"]

girl = ["Emma", "Isabella", "Emily", "Madison", "Ava", "Olivia", "Sophia", "Abigail", "Elizabeth", "Chloe", "Samantha",
        "Addison", "Natalie", "Mia", "Alexis", "Alyssa", "Hannah", "Ashley", "Ella", "Sarah", "Grace", "Taylor",
        "Brianna", "Lily", "Hailey", "Anna", "Victoria", "Kayla", "Lillian", "Lauren", "Kaylee", "Allison", "Savannah",
        "Nevaeh", "Gabriella", "Sofia", "Makayla", "Avery", "Riley", "Julia", "Leah", "Aubrey", "Jasmine", "Audrey",
        "Katherine", "Morgan", "Brooklyn", "Destiny", "Sydney", "Alexa", "Kylie", "Brooke", "Kaitlyn", "Evelyn",
        "Layla", "Madeline", "Kimberly", "Zoe", "Jessica", "Peyton", "Alexandra", "Claire", "Madelyn", "Maria",
        "Mackenzie", "Arianna", "Jocelyn", "Amelia", "Angelina", "Trinity", "Andrea", "Maya", "Valeria", "Sophie",
        "Rachel", "Vanessa", "Aaliyah", "Mariah", "Gabrielle", "Katelyn", "Ariana", "Bailey", "Camila", "Jennifer",
        "Melanie", "Gianna", "Charlotte", "Paige", "Autumn", "Payton", "Faith", "Sara", "Isabelle", "Caroline",
        "Genesis", "Isabel", "Mary", "Zoey", "Gracie"]

last = ["SMITH", "JOHNSON", "WILLIAMS", "BROWN", "JONES", "MILLER", "DAVIS", "GARCIA", "RODRIGUEZ", "WILSON",
        "MARTINEZ", "ANDERSON", "TAYLOR", "THOMAS", "HERNANDEZ", "MOORE", "MARTIN", "JACKSON", "THOMPSON", "WHITE",
        "LOPEZ", "LEE", "GONZALEZ", "HARRIS", "CLARK", "LEWIS", "ROBINSON", "WALKER", "PEREZ", "HALL", "YOUNG", "ALLEN",
        "SANCHEZ", "WRIGHT", "KING", "SCOTT", "GREEN", "BAKER", "ADAMS", "NELSON", "HILL", "RAMIREZ", "CAMPBELL",
        "MITCHELL", "ROBERTS", "CARTER", "PHILLIPS", "EVANS", "TURNER", "TORRES", "PARKER", "COLLINS", "EDWARDS",
        "STEWART", "FLORES", "MORRIS", "NGUYEN", "MURPHY", "RIVERA", "COOK", "ROGERS", "MORGAN", "PETERSON", "COOPER",
        "REED", "BAILEY", "BELL", "GOMEZ", "KELLY", "HOWARD", "WARD", "COX", "DIAZ", "RICHARDSON", "WOOD", "WATSON",
        "BROOKS", "BENNETT", "GRAY", "JAMES", "REYES", "CRUZ", "HUGHES", "PRICE", "MYERS", "LONG", "FOSTER", "SANDERS",
        "ROSS", "MORALES", "POWELL", "SULLIVAN", "RUSSELL", "ORTIZ", "JENKINS", "GUTIERREZ", "PERRY", "BUTLER",
        "BARNES", "FISHER", "HENDERSON", "COLEMAN", "SIMMONS", "PATTERSON", "JORDAN", "REYNOLDS", "HAMILTON", "GRAHAM",
        "KIM", "GONZALES", "ALEXANDER", "RAMOS", "WALLACE", "GRIFFIN", "WEST", "COLE", "HAYES", "CHAVEZ", "GIBSON",
        "BRYANT", "ELLIS", "STEVENS", "MURRAY", "FORD", "MARSHALL", "OWENS", "MCDONALD", "HARRISON", "RUIZ", "KENNEDY",
        "WELLS", "ALVAREZ", "WOODS", "MENDOZA", "CASTILLO", "OLSON", "WEBB", "WASHINGTON", "TUCKER", "FREEMAN", "BURNS",
        "HENRY", "VASQUEZ", "SNYDER", "SIMPSON", "CRAWFORD", "JIMENEZ", "PORTER", "MASON", "SHAW", "GORDON", "WAGNER",
        "HUNTER", "ROMERO", "HICKS", "DIXON", "HUNT", "PALMER", "ROBERTSON", "BLACK", "HOLMES", "STONE", "MEYER",
        "BOYD", "MILLS", "WARREN", "FOX", "ROSE", "RICE", "MORENO", "SCHMIDT", "PATEL", "FERGUSON", "NICHOLS",
        "HERRERA", "MEDINA", "RYAN", "FERNANDEZ", "WEAVER", "DANIELS", "STEPHENS", "GARDNER", "PAYNE", "KELLEY", "DUNN",
        "PIERCE", "ARNOLD", "TRAN", "SPENCER", "PETERS", "HAWKINS", "GRANT", "HANSEN", "CASTRO", "HOFFMAN", "HART",
        "ELLIOTT", "CUNNINGHAM", "KNIGHT", "BRADLEY", "CARROLL", "HUDSON", "DUNCAN", "ARMSTRONG", "BERRY", "ANDREWS",
        "JOHNSTON", "RAY", "LANE", "RILEY", "CARPENTER", "PERKINS", "AGUILAR", "SILVA", "RICHARDS", "WILLIS",
        "MATTHEWS", "CHAPMAN", "LAWRENCE", "GARZA", "VARGAS", "WATKINS", "WHEELER", "LARSON", "CARLSON", "HARPER",
        "GEORGE", "GREENE", "BURKE", "GUZMAN", "MORRISON", "MUNOZ", "JACOBS", "OBRIEN", "LAWSON", "FRANKLIN", "LYNCH",
        "BISHOP", "CARR", "SALAZAR", "AUSTIN", "MENDEZ", "GILBERT", "JENSEN", "WILLIAMSON", "MONTGOMERY", "HARVEY",
        "OLIVER", "HOWELL", "DEAN", "HANSON", "WEBER", "GARRETT", "SIMS", "BURTON", "FULLER", "SOTO", "MCCOY", "WELCH",
        "CHEN", "SCHULTZ", "WALTERS", "REID", "FIELDS", "WALSH", "LITTLE", "FOWLER", "BOWMAN", "DAVIDSON", "MAY", "DAY",
        "SCHNEIDER", "NEWMAN", "BREWER", "LUCAS", "HOLLAND", "WONG", "BANKS", "SANTOS", "CURTIS", "PEARSON", "DELGADO",
        "VALDEZ", "PENA", "RIOS", "DOUGLAS", "SANDOVAL", "BARRETT", "HOPKINS", "KELLER", "GUERRERO", "STANLEY", "BATES",
        "ALVARADO", "BECK", "ORTEGA", "WADE", "ESTRADA", "CONTRERAS", "BARNETT", "CALDWELL", "SANTIAGO", "LAMBERT",
        "POWERS", "CHAMBERS", "NUNEZ", "CRAIG", "LEONARD", "LOWE", "RHODES", "BYRD", "GREGORY", "SHELTON", "FRAZIER",
        "BECKER", "MALDONADO", "FLEMING", "VEGA", "SUTTON", "COHEN", "JENNINGS", "PARKS", "MCDANIEL", "WATTS", "BARKER",
        "NORRIS", "VAUGHN", "VAZQUEZ", "HOLT", "SCHWARTZ", "STEELE", "BENSON", "NEAL", "DOMINGUEZ", "HORTON", "TERRY",
        "WOLFE", "HALE", "LYONS", "GRAVES", "HAYNES", "MILES", "PARK", "WARNER", "PADILLA", "BUSH", "THORNTON",
        "MCCARTHY", "MANN", "ZIMMERMAN", "ERICKSON", "FLETCHER", "MCKINNEY", "PAGE", "DAWSON", "JOSEPH", "MARQUEZ",
        "REEVES", "KLEIN", "ESPINOZA", "BALDWIN", "MORAN", "LOVE", "ROBBINS", "HIGGINS", "BALL", "CORTEZ", "LE",
        "GRIFFITH", "BOWEN", "SHARP", "CUMMINGS", "RAMSEY", "HARDY", "SWANSON", "BARBER", "ACOSTA", "LUNA", "CHANDLER",
        "DANIEL", "BLAIR", "CROSS", "SIMON", "DENNIS", "OCONNOR", "QUINN", "GROSS", "NAVARRO", "MOSS", "FITZGERALD",
        "DOYLE", "MCLAUGHLIN", "ROJAS", "RODGERS", "STEVENSON", "SINGH", "YANG", "FIGUEROA", "HARMON", "NEWTON", "PAUL",
        "MANNING", "GARNER", "MCGEE", "REESE", "FRANCIS", "BURGESS", "ADKINS", "GOODMAN"]


def generer_matricule():
    n = random.randint(5, 7)
    return random.randint(int(math.pow(10, n)), int(math.pow(10, n) * 9.999))


matricules = []

for _ in range(400):
    temp = generer_matricule()
    if temp not in matricules:
        matricules.append(temp)

duplicates = any(matricules.count(elements) > 1 for elements in matricules)

if duplicates:
    print("oh ho duplicates!\n")

file = io.open("C:\\Users\\Francis\\AppData\\Roaming\\JetBrains\\PyCharmCE2021.1\\scratches\\codequebectronque.csv",
               encoding='UTF-8')

codepostaux = {}
for line in file:
    temp = line.split(";")
    if temp[1][-1] == '\n':
        temp[1] = temp[1][0:-1]
    if temp[1] != "":
        codepostaux[temp[0]] = temp[1]

codekeys = list(codepostaux.keys())


def findprovince(codepostal):
    if codepostal[0] == "H" or codepostal[0] == "J" or codepostal[0] == "G":
        return "Québec"
    elif codepostal[0] == "A":
        return "Terre-Neuve"
    elif codepostal[0] == "B":
        return "Nouvelle-Écosse"
    elif codepostal[0] == "C":
        return "Ile-du-Prince-Édouard"
    elif codepostal[0] == "E":
        return "Nouveau-Brunswick"
    elif codepostal[0] == "K" or codepostal[0] == "L" or codepostal[0] == "M" or codepostal[0] == "N" or \
            codepostal[0] == "O" or codepostal[0] == "P":
        return "Ontario"
    elif codepostal[0] == "R":
        return "Manitoba"
    elif codepostal[0] == "S":
        return "Saskatchewan"
    elif codepostal[0] == "T":
        return "Alberta"
    elif codepostal[0] == "V":
        return "Colombie-Britannique"
    elif codepostal[0] == "X":
        return "Territoires-du-Nord-Ouest"
    elif codepostal[0] == "Y":
        return "Yukon"


def generer_naissance():
    an = random.randint(1965, 2002)
    mois = random.randint(1, 12)
    if mois in [1, 3, 5, 7, 8, 10, 12]:
        jour = random.randint(1, 31)
    elif mois == 2:
        jour = random.randint(1, 28)
    else:
        jour = random.randint(1, 30)

    date = datetime.date(an, mois, jour)
    return "\'" + str(date) + "\'"


def generer_email(prenom, nom):
    prenom = prenom[1:-1]
    nom = nom[1:-1]
    return "\'" + prenom + "." + nom + str(random.randint(1, 9)) + "@umontreal.ca" + "\'"


def generer_tel():
    indicatifs = [450, 438, 514, 819]
    ind = str(indicatifs[random.randint(0, 3)])
    tel1 = str(random.randint(350, 978))
    tel2 = str(random.randint(0, 9999)).zfill(4)
    return "\'(" + ind + ") " + tel1 + "-" + tel2 + "\'"


file_rue = io.open("C:\\Users\\Francis\\AppData\\Roaming\\JetBrains\\PyCharmCE2021.1\\scratches\\vdq-voiepublique.csv",
                   encoding='utf-8')
rues = []
exclusion = ["Bretelle", "Trottoir", "Piste", "cyclable", "Bande", "Lien", "Passerelle", "Stationnement", "Accès",
             "Projetée", "TOPOGRAPHIE", "Column"]
for line in file_rue:
    if line[-1] == "\n":
        line = line[0:-1]
    if any(excluded in line for excluded in exclusion):
        continue
    else:
        rues.append(line)


def generer_adresse():
    no = random.randint(1, 12890)
    rue = "\'" + rues[random.randint(0, len(rues))] + "\'"

    codep = codekeys[random.randint(0, len(codekeys) - 1)]
    ville = "\'" + codepostaux[codep] + "\'"
    prov = "\'" + findprovince(codep) + "\'"
    codep = "\'" + codep + "\'"

    return no, rue, ville, prov, codep


def generer_credit():
    return random.randint(30, 120)


def generer_gpa():
    return random.randint(26, 43) / 10


def generer_nom():
    if random.random() < 0.5:
        prenom = "\'" + boy[random.randint(0, len(boy) - 1)] + "\'"
    else:
        prenom = "\'" + girl[random.randint(0, len(girl) - 1)] + "\'"

    nom = "\'" + last[random.randint(0, len(last) - 1)] + "\'"

    return prenom, nom


def generer_multi_prenoms(n):
    prenoms = []
    for _ in range(n):
        prenoms.append(generer_nom()[0])

    return prenoms


prog_file = io.open("C:\\Users\\Francis\\AppData\\Roaming\\JetBrains\\PyCharmCE2021.1\\scratches\\resultats.csv",
                    encoding='utf-8')
prog_faculte_depart = {}
faculte = {}
depart = {}
for line in prog_file:
    temp = line.split(";")
    temp[2] = temp[2][0:-1]
    if len(temp[0]) > 63:
        temp[0] = temp[0][0:63]
    if len(temp[1]) > 63:
        temp[1] = temp[1][0:63]
    if len(temp[2]) > 63:
        temp[2] = temp[2][0:63]
    if temp[2]:
        faculte[temp[1]] = temp[1]
        depart[temp[2]] = temp[2]
        prog_faculte_depart[temp[0]] = [temp[1], temp[2]]


programmes = list(prog_faculte_depart.keys())
faculte = list(faculte)
depart = list(depart)

file_fac = io.open("C:\\Users\\Francis\\AppData\\Roaming\\JetBrains\\PyCharmCE2021.1\\scratches\\facultes.txt", 'w+',
                    encoding='utf-8')
file_fac.seek(0)
for fac in faculte:
    if len(fac) > 63:
        fac = fac[0:63]
    file_fac.write("\'"+fac+"\',\n")
file_fac.truncate()
file_fac.close()

file_dep = io.open("C:\\Users\\Francis\\AppData\\Roaming\\JetBrains\\PyCharmCE2021.1\\scratches\\departements.txt", 'w+',
                    encoding='utf-8')
file_dep.seek(0)
for dep in depart:
    if len(dep) > 63:
        dep = dep[0:63]
    file_dep.write("\'"+dep+"\',\n")
file_dep.truncate()
file_dep.close()

file_prog = io.open("C:\\Users\\Francis\\AppData\\Roaming\\JetBrains\\PyCharmCE2021.1\\scratches\\programmes.txt", 'w+',
                    encoding='utf-8')

file_prog.seek(0)
for prog in programmes:
    if len(prog) > 63:
        prog = prog[0:60]
    file_prog.write("\'"+prog+"\',\n")
file_prog.truncate()
file_prog.close()


def generer_programme():
    prog = programmes[random.randint(0, len(programmes) - 1)]
    tup = prog_faculte_depart[prog]
    prog = "\'" + prog + "\'"
    faculte = "\'" + tup[0] + "\'"
    depart = "\'" + tup[1] + "\'"
    return prog, faculte, depart


file_ent = io.open("C:\\Users\\Francis\\AppData\\Roaming\\JetBrains\\PyCharmCE2021.1\\scratches\\entreprises.csv",
                   encoding='utf-8')

entreprises = []

for line in file_ent:
    temp = line.split(";")
    temp[-1] = temp[-1][0:-1]
    entreprises.append([temp[0], temp[1], temp[2], temp[3], temp[4], temp[5], temp[6], temp[7]])

matricules_generes = []


def generer_insert_etudiant():
    prenoms_mult = []

    if random.random() < 0.15:
        prenoms_mult = generer_multi_prenoms(random.randint(2, 5))
        nom = generer_nom()[1]
    else:
        prenom, nom = generer_nom()
        prenoms_mult.append(prenom)

    passed_check = False
    matricule = 'ERR'
    while not passed_check:
        matricule = generer_matricule()
        if matricule not in matricules_generes:
            passed_check = True

    matricules_generes.append(matricule)

    no, rue, ville, prov, codep = generer_adresse()

    tel = generer_tel()

    courriel = generer_email(prenoms_mult[0], nom)

    credit = generer_credit()

    gpa = generer_gpa()

    prog, faculte, _ = generer_programme()

    birth = generer_naissance()

    personne = "INSERT INTO personne VALUES (" + str(matricule) + ", " + codep + ", " + nom + ", " + birth + ", " + \
               faculte + ", " + tel + ", " + courriel + ", " + str(no) + ");\n"

    n = len(prenoms_mult)

    prenoms = []
    for i in range(n):
        prenoms.append("INSERT INTO prenoms VALUES (" + str(matricule) + ", " + prenoms_mult[i] + ");\n")

    etudiant = "INSERT INTO etudiant VALUES (" + str(matricule) + ", " + prog + ", " + str(credit) + ", " + \
               str(gpa) + ");\n"

    return personne, prenoms, etudiant


def generer_insert_professeur():
    prenoms_mult = []

    if random.random() < 0.15:
        prenoms_mult = generer_multi_prenoms(random.randint(2, 5))
        nom = generer_nom()[1]
    else:
        prenom, nom = generer_nom()
        prenoms_mult.append(prenom)

    passed_check = False
    matricule = 'ERR'
    while not passed_check:
        matricule = generer_matricule()
        if matricule not in matricules_generes:
            passed_check = True

    matricules_generes.append(matricule)

    no, rue, ville, prov, codep = generer_adresse()

    tel = generer_tel()

    courriel = generer_email(prenoms_mult[0], nom)

    _, faculte, depart = generer_programme()

    birth = generer_naissance()

    personne = "INSERT INTO personne VALUES (" + str(matricule) + ", " + codep + ", " + nom + ", " + birth + ", " + \
               faculte + ", " + tel + ", " + courriel + ", " + str(no) + ");\n"

    n = len(prenoms_mult)

    prenoms = []
    for i in range(n):
        prenoms.append("INSERT INTO prenoms VALUES (" + str(matricule) + ", " + prenoms_mult[i] + ");\n")

    professeur = "INSERT INTO professeur VALUES (" + str(matricule) + ", " + depart + ");\n"

    return personne, prenoms, professeur


def create_insert_files():
    file_forced = io.open(
        "C:\\Users\\Francis\\AppData\\Roaming\\JetBrains\\PyCharmCE2021.1\\scratches\\3_populate_forced.sql",
        'w', encoding='utf-8')

    file_forced.write("begin transaction;\nset search_path to projet_ift_2935;\n")

    for prog in programmes:
        fac, depart = prog_faculte_depart[prog]
        prog = "\'" + prog + "\'"
        fac = "\'" + fac + "\'"
        depart = "\'" + depart + "\'"
        file_forced.write("INSERT INTO programmes_departements VALUES (" + prog + ", " + fac + ", " + depart + ");\n")

    for codep in list(codepostaux.keys()):
        ville = "\'" + codepostaux[codep] + "\'"
        province = "\'" + findprovince(codep) + "\'"
        codep = "\'" + codep + "\'"

        file_forced.write("INSERT INTO code_postal VALUES (" + codep + ", " + ville + ", " + province + ");\n")

    file_forced.write("commit;")
    file_forced.truncate()
    file_forced.close()

    file_etudiant = io.open(
        "C:\\Users\\Francis\\AppData\\Roaming\\JetBrains\\PyCharmCE2021.1\\scratches\\4_populate_etudiant.sql",
        'w', encoding='utf-8')

    file_etudiant.write("begin transaction;\nset search_path to projet_ift_2935;\n")

    for _ in range(50):
        personne, prenoms, etudiant = generer_insert_etudiant()

        file_etudiant.write(personne)
        for entry in prenoms:
            file_etudiant.write(entry)

        file_etudiant.write(etudiant)

    file_etudiant.write("commit;")
    file_etudiant.truncate()
    file_etudiant.close()

    file_prof = io.open(
        "C:\\Users\\Francis\\AppData\\Roaming\\JetBrains\\PyCharmCE2021.1\\scratches\\5_populate_professeur.sql",
        'w', encoding='utf-8')

    file_prof.write("begin transaction;\nset search_path to projet_ift_2935;\n")

    for _ in range(10):
        personne, prenoms, professeur = generer_insert_professeur()

        file_prof.write(personne)
        for entry in prenoms:
            file_prof.write(entry)

        file_prof.write(professeur)

    file_prof.write("commit;")
    file_prof.truncate()
    file_prof.close()


file.close()
file_ent.close()
file_rue.close()
prog_file.close()

create_insert_files()
