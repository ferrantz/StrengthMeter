import numpy as np
import matplotlib.pyplot as plt
from math import pi
from vertici import *
import pandas as pd

file_path = 'dati.xlsx'
df = pd.read_excel(file_path)

# Dati per il grafico
labels = ['PETTO', 'GAMBE', 'SPALLE', 'DORSO', 'BICIPITI', 'TRICIPITI']
max_values = [PANCA_PIANA, TOT_GAMBE, MILITARY_PRESS, REMATORE_BILANCIERE, CURL_BILANCIERE, FRENCH_PRESS_BIL_CURVO]

# Numero di variabili
num_vars = len(labels)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

# Completa il cerchio aggiungendo il primo valore alla fine per tutti i set di dati
angles += angles[:1]

# Creazione della figura e dell'asse
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

# Ciclo per aggiungere ogni serie di dati
for i in range(df.shape[0]):
    values = df.iloc[i].tolist()[1:]
    values += values[:1]  # Completa il cerchio
    
    # Normalizzazione dei valori rispetto ai massimi
    normalized_values = [v / max_v for v, max_v in zip(values, max_values)]
    normalized_values += normalized_values[:1]  # Completa il cerchio
    
    # Preparare il label della legenda, assicurandosi che sia solo la data
    date_label = df.iloc[i].tolist()[0]
    if isinstance(date_label, pd.Timestamp):
        date_label = date_label.strftime('%d-%m-%Y')
    
    # Disegno delle linee e riempimento dell'area
    ax.plot(angles, normalized_values, linewidth=2, linestyle='solid', label=date_label)
    ax.fill(angles, normalized_values, alpha=0.25)

# Impostazione delle etichette dei vertici
ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels, ha='center')

# Impostazione dei limiti dell'asse radiale
ax.set_ylim(0, 1)  # Normalizzazione tra 0 e 1  

# Mostrare la griglia radiale con i cerchi concentrici
ax.yaxis.grid(True)  # Mostra le linee della griglia radiali    

# Nascondere le etichette dell'asse radiale
ax.set_yticklabels([])  # Nascondi le etichette radiali 

# Mostra la legenda
# bbox_to_anchor: sposta la legenda fuori dal grafico e si adatta automaticamente
ax.legend(loc='upper left', bbox_to_anchor=(1.1, 1.05), title='Osservazioni')

# Mostra il grafico
plt.show()

