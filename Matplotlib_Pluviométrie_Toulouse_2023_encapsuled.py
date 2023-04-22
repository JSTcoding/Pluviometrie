from matplotlib import pyplot as plt


def plot_pluviometry(x, y_dict):
    plt.figure(figsize=(20, 10))
    colors = plt.rcParams['axes.prop_cycle'].by_key()['color']
    for i, (year, y_data) in enumerate(y_dict.items()):
        plt.plot(x, y_data, label=str(year), color=colors[i])
        plt.fill_between(x, y_data, color=colors[i], alpha=0.3)
        plt.text(0, 232 - (year-2018)*7, 'Cumul {} = {}mm'.format(year, sum(y_data)),
                 color=colors[i], fontsize=10)
        
    plt.xticks(x, rotation=90)
    plt.xlabel('Mois')
    plt.ylabel('Cumul (mm)')
    plt.legend(title='Année', loc='upper left')
    plt.title('Cumul annuel de pluviométrie')
    plt.subplots_adjust(bottom=0.15, top=0.93, left=0.06, right=0.95, wspace=0.2, hspace=0.2)
    # Remove call to plt.show()

x = ['Jan', 'Fév', 'Mars', 'Avril', 'Mai', 'Juin', 'Juil', 'Aout', 'Sept', 'Oct', 'Nov', 'Déc']

y_dict = {
    2018: [114, 143, 161, 79, 229, 104, 102, 52, 34, 83, 46, 95],
    2019: [93, 76, 25, 165, 124, 79, 92, 51, 37, 141, 177, 120],
    2020: [54, 15, 75, 110, 89, 86, 31, 47, 70, 137, 14, 154],
    2021: [98, 77, 40, 30, 81, 97, 27, 27, 27, 9, 37, 26],
    2022: [18, 5, 16, 22, 7, 14, 4, 17, 13, 5, 29, 9],
    2023: [25, 6, 18, 0, 0, 0, 0, 0, 0, 0, 0, 0]
}

# Call to function
plot_pluviometry(x, y_dict)

# Add title, axis labels, and legend
plt.title("Evolution de la pluviométrie à Toulouse / France - Période 2018 à 2023 \n Données : https://www.historique-meteo.net/france/midi-toulousain/toulouse/")
plt.xlabel("Mois \n \n Graphe généré avec Python 3.10 \ Matplotlib \n \u00a9 Jérôme Salort - www.intelligence-informatique.fr ")
plt.ylabel("Pluiviométrie en mm")
plt.grid(True)
plt.legend()

# Show the plot
plt.show()