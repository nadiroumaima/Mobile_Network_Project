import matplotlib.pyplot as plt

# Data points for NewReno Loss Ratio
newreno_loss_ratios = [4.842795, 16.058394, 6.225681, 7.462687, 0.000000, 3.428571, 1.565996, 2.059925,
                       2.409639, 3.132530, 0.853789, 2.222222, 1.367781, 4.781421, 9.936709, 8.904511,
                       9.027027, 12.121212, 12.023177, 11.325080, 10.642040, 10.203235, 9.937402,
                       9.722736, 9.573361, 9.470569, 8.748019, 8.628659, 8.439068, 8.177702, 7.944308,
                       7.716702, 7.267663, 7.392147, 6.890875, 6.558501, 6.426678, 6.509636, 6.133557,
                       6.262708, 5.844930, 5.909798, 5.929304, 5.925098, 5.859873, 5.804843, 5.644599,
                       5.637131, 5.395624, 5.104670, 5.219997, 5.027847, 5.037285, 4.917300, 4.842795]

# Data points for NewVegas Loss Ratio
vegas_loss_ratios = [31.120923, 8.928571, 6.701031, 4.150943, 0.000000, 2.887139, 33.453888, 23.447402,
                        19.626168, 17.847025, 15.378356, 14.840715, 14.794733, 14.285714, 12.605042,
                        11.712772, 11.025782, 9.905426, 9.239873, 11.920243, 11.023311, 12.843691,
                        22.912836, 32.829917, 41.319073, 39.665186, 37.601035, 37.541528, 36.002321,
                        35.107873, 34.030571, 32.442846, 35.977625, 35.170017, 34.052241, 32.809249,
                        31.876549, 30.851295, 30.460374, 29.481180, 28.613569, 30.150276, 33.666482,
                        36.342468, 35.735422, 34.616034, 33.661902, 33.365838, 32.820759, 32.121022,
                        32.182679, 31.403849, 30.977552, 31.149409, 31.120923]
# Time points
time_points = range(50, 600, 10)

# Create the plot
plt.figure(figsize=(10, 6))

# Plot NewReno Loss Ratio
plt.plot(time_points, newreno_loss_ratios, label='NewReno Loss Ratio', marker='o', linestyle='-')

# Plot NewVegas Loss Ratio
plt.plot(time_points, vegas_loss_ratios, label='Vegas Loss Ratio', marker='s', linestyle='-')

# Set labels and title
plt.xlabel('Time Point')
plt.ylabel('Loss Ratio')
plt.title('NewReno and Vegas Loss Ratio over Time')

# Add legend
plt.legend()

# Grid
plt.grid(False)


# Ajuster le pas de graduation de l'axe des abscisses
plt.xticks(time_points[::3])

# Show the plot
plt.show()