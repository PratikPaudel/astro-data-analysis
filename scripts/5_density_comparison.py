import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde

# Data from Maiolino et al. 2023
z1 = np.array([4.64820, 5.59510, 4.40935, 4.68123, 5.22943, 5.87461, 6.76026, 5.91900, 4.13320, 4.44800])
log_L_Ha1 = np.array([41.91761, 41.85963, 41.86622, 41.99880, 42.09537, 42.14658, 42.98032, 42.09984, 42.68253, 42.20340])
f_Edd1 = np.array([0.16000, 0.20000, 0.20000, 0.18000, 0.38000, 0.32000, 0.42000, 0.25200, 0.63000, 0.16700])
E_B_V1 = np.array([0.64, 0.99, 0.68, 0.67, 0.39, 0.69, 0.64, 0.27, 0.45, 0.36])

# Data from Harikane et al. 2023
z2 = np.array([4.478, 4.015, 4.583, 5.624, 4.483, 5.666, 5.241, 6.000])
log_L_Ha2 = np.array([43.89, 43.08, 42.91, 44.83, 43.83, 44.26, 43.88, 43.41])
f_Edd2 = np.array([0.46, 3.68, 1.89, 1.47, 1.93, 0.65, 0.51, 2.02])
E_B_V2 = np.array([0.00, 0.16, 0.17, 1.38, 0.42, 0.80, 0.28, 0.19])

# Compute logarithms, handling E(B-V) = 0
log_f_Edd1 = np.log10(f_Edd1)
log_E_B_V1 = np.log10(E_B_V1)
log_f_Edd2 = np.log10(f_Edd2)
log_E_B_V2 = np.where(E_B_V2 > 0, np.log10(E_B_V2), np.nan)  # Handle log(0) by replacing with NaN

# Remove NaNs for plotting
valid_indices_2023_Harikane = ~np.isnan(log_E_B_V2)
log_f_Edd2_valid = log_f_Edd2[valid_indices_2023_Harikane]
log_E_B_V2_valid = log_E_B_V2[valid_indices_2023_Harikane]

def create_contour_grid(x, y):
    """Create grid for contour plotting"""
    xmin, xmax = x.min() - 0.5, x.max() + 0.5
    ymin, ymax = y.min() - 0.5, y.max() + 0.5
    xx, yy = np.meshgrid(np.linspace(xmin, xmax, 100), np.linspace(ymin, ymax, 100))
    return xx, yy, xmin, xmax, ymin, ymax

def compute_density(x, y, xx, yy):
    """Compute KDE density for contour plotting"""
    kde = gaussian_kde([x, y])
    zz = kde(np.vstack([xx.ravel(), yy.ravel()])).reshape(xx.shape)
    return zz

def read_data(file_path):
    """Read comma-separated data from file"""
    with open(file_path, 'r') as file:
        data = file.readline().strip().split(',')
    return np.array(data, dtype=float)

# Create grids for contour plotting
xx1, yy1, xmin1, xmax1, ymin1, ymax1 = create_contour_grid(log_f_Edd1, log_E_B_V1)
xx2, yy2, xmin2, xmax2, ymin2, ymax2 = create_contour_grid(log_f_Edd2_valid, log_E_B_V2_valid)

# Compute density for contours
zz1 = compute_density(log_f_Edd1, log_E_B_V1, xx1, yy1)
zz2 = compute_density(log_f_Edd2_valid, log_E_B_V2_valid, xx2, yy2)

# Create the plot
plt.figure(figsize=(12, 7))

# Read and plot additional data
try:
    eddington_ratios = read_data('eddington_ratios.txt')
    extinctions = read_data('extinctions.txt')
    log_eddington_ratios = np.log10(eddington_ratios)
    ebv_extinctions = (extinctions - 22.8)
    plt.plot(log_eddington_ratios, ebv_extinctions, 'k--', label='Read Data')
except FileNotFoundError:
    print("Warning: Additional data files not found. Skipping this plot.")

# Plot contours
plt.contourf(xx1, yy1, zz1, levels=20, cmap='Blues', alpha=0.3)
plt.contourf(xx2, yy2, zz2, levels=20, cmap='Reds', alpha=0.3)

# Plot scatter points
plt.scatter(log_f_Edd1, log_E_B_V1,
            color='blue', marker='o', edgecolor='black',
            label='2023_Maiolino')
plt.scatter(log_f_Edd2_valid, log_E_B_V2_valid,
            color='red', marker='s', edgecolor='black',
            label='2023_Harikane')

# Customize plot
plt.xlabel('log f_Edd')
plt.ylabel('log E(B-V)')
plt.xlim(-3, 1)
plt.ylim(-3, 1)
plt.grid(True)
plt.legend()

if __name__ == "__main__":
    plt.show()