output_file = []
data_path = []
data_energy = []
data = []
lines = []

with open('nebts.final.interp', 'r') as input_file:
    lines = input_file.readlines()[16:] # Skipping the lines
for item in lines:
    item_split = item.split()
    data.append(item_split)
    for path in data:
        path = item_split[0]
        energy = item_split[2]
    data_path.append(float(path))
    data_energy.append(float(energy))
    
import matplotlib.pyplot as plt
plt.plot(data_path,data_energy)
plt.xlabel('ReactionPath')
plt.ylabel('Energy/Eh')