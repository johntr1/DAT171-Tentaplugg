import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("pollutants.txt")
data = data.reshape(26, 11, 30)

years = np.arange(1990, 2020)

pollutants = ['Kväveoxider (t)', 'Flyktiga organiska ämnen, exkl. metan (t)', 'Svaveldioxid (t)',
              'Ammoniak (t)', 'PM2.5 (t)', 'PM10 (t)', 'TSP (t)', 'Sot (BC) (t)', 'Kolmonoxid (CO) (t)',
              'Bly (kg)', 'Kadmium (kg)', 'Kvicksilver (kg)', 'Arsenik (kg)', 'Krom (kg)',
              'Koppar (kg)', 'Nickel (kg)', 'Selen (kg)', 'Zink (kg)', 'Dioxin (g I-Teq)',
              'benso(a)pyren (kg)', 'benso(b)fluoranten (kg)', 'benso(k)fluoranten (kg)', 'Indeno(1,2,3-cd)pyren (kg)',
              'PAH 1-4 (kg)', 'HCB (kg)', 'PCB  (kg)']

sectors = ['Nationell total (exkl. utrikes transporter)', 'Nationell total',
           'Arbetsmaskiner', 'Avfall', 'El och fjärrvärme', 'Industri', 'Utrikes transporter', 'Jordbruk',
           'Lösningsmedel etc.', 'Inrikes transporter', 'Egen uppvärmning']

# Part A, axis 1 since it's over the sectors
pol_sum = np.sum(data, axis=1)
t_items = np.char.find(pollutants, '(t)') != -1 # Char finds indices for the letters. Can use true or false as well
kg_items = np.char.find(pollutants, '(kg)') != -1
o_items = np.logical_not(t_items | kg_items)  # Takes rest

pollutants = np.array(pollutants)

# Part B
fig, ax = plt.subplots(2, 3)
ax[0, 0].plot(years, pol_sum[t_items].T, label=pollutants[t_items])
ax[0, 1].plot(years, pol_sum[kg_items].T, label=pollutants[kg_items])
ax[0, 2].plot(years, pol_sum[o_items].T, label=pollutants[o_items])


# Part C


plt.show()
