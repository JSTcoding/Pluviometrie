#########################################
#           MatPlotLib                  #
#########################################

from matplotlib import pyplot as plt

x = ['Jan', 'Fév', 'Mars', 'Avril', 'Mai', 'Juin', 'Juil', 'Aout', 'Sept', 'Oct', 'Nov', 'Déc']

y_2018 = [114, 143, 161, 79, 229, 104, 102, 52, 34, 83, 46, 95]

y_2019 = [93, 76, 25, 165, 124, 79, 92, 51, 37, 141, 177, 120]

y_2020 = [54, 15, 75, 110, 89, 86, 31, 47, 70, 137, 14, 154]

y_2021 = [98, 77, 40, 30, 81, 97, 27, 27, 27, 9, 37, 26]

y_2022 = [18, 5, 16, 22, 7, 14, 4, 17, 13, 5, 29, 9]

y_2023 = [25, 6, 18, 0, 0, 0, 0, 0, 0, 0, 0, 0]

plt.plot(x, y_2018, label="2018", color="grey", linewidth=2)

plt.text(0, 232, 'Cumul 2018 = ' + (str(sum(y_2018))) + 'mm', color="grey")

plt.plot(x, y_2019, label="2019", color="green", linewidth=2)

plt.text(0, 225, 'Cumul 2019 = ' + (str(sum(y_2019))) + 'mm', color="green")

plt.plot(x, y_2020, label="2020", color="orange", linewidth=2)

plt.text(0, 218, 'Cumul 2020 = ' + (str(sum(y_2020))) + 'mm', color="orange")

plt.plot(x, y_2021, label="2021", color="blue", linewidth=2)

plt.text(0, 211, 'Cumul 2021 = ' + (str(sum(y_2021))) + 'mm', color="blue")

plt.plot(x, y_2022, label="2022", color="red", linewidth=3)

plt.text(0, 204, 'Cumul 2022 = ' + (str(sum(y_2022))) + 'mm', color="red")

plt.plot(x, y_2023, label="2023", color="purple", linewidth=2)

plt.text(0, 197, 'Cumul 2023 = ' + (str(sum(y_2023))) + 'mm', color="purple")

plt.title("Evolution de la pluviométrie à Toulouse / France - Période 2018 à 2023 \n Données : https://www.historique-meteo.net/france/midi-toulousain/toulouse/")
plt.xlabel("Mois \n \n Graphe généré avec Python 3.10 \ Matplotlib \n \u00a9 Jérôme Salort - www.intelligence-informatique.fr ")
plt.ylabel("Pluiviométrie en mm")
plt.grid(True)

plt.legend()

plt.show()
