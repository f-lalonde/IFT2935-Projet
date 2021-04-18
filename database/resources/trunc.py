import io

file = io.open("C:\\Users\\Francis\\AppData\\Roaming\\JetBrains\\PyCharmCE2021.1\\scratches\\codequebectronque.csv", 'w', encoding="UTF-8")
file_og = io.open("C:\\Users\\Francis\\AppData\\Roaming\\JetBrains\\PyCharmCE2021.1\\scratches\\codequebecplus2.csv", encoding="UTF-8")
list_ville = []
for line in file_og:
    code, ville = line.split(";")
    if ville in list_ville:
        continue
    else:
        file.write(code+";"+ville)
        list_ville.append(ville)

file.close()
file_og.close()