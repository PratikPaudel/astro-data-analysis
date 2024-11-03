import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Spectral data analysis
observed_wavelengths = np.array([0.893, 1.03, 1.25, 1.63, 2.2, 3.35, 3.55, 4.49, 4.6, 5.73, 7.87, 11.56])
observed_flux_values = np.array([3.46273, 1.58287, 1.21598, 0.90115, 0.5819, 0.26269, 0.2472, 0.16518, 0.16178, 0.11047, 0.07074, 0.07684])
error_values = np.array([0.1756, 0.10931, 0.11118, 0.06963, 0.02924, 0.00729, 0.00576, 0.00369, 0.00733, 0.00565, 0.00349, 0.02996])

def fit_linear_function(x, m, b):
    return m * x + b

# Perform the curve fitting
params, covariance = curve_fit(
    fit_linear_function,
    np.log10(observed_wavelengths),
    np.log10(observed_flux_values),
    sigma=np.log10(1 + error_values/observed_flux_values),
    p0=[-2, 1.2]
)

# Plot the data and fit
plt.figure(figsize=(10, 6))
plt.errorbar(
    observed_wavelengths[3:11],
    observed_flux_values[3:11],
    yerr=error_values[3:11],
    fmt='o',
    label='Observed Data',
    ecolor='black'
)

plt.yscale("log")
plt.xscale("log")

plt.plot(
    observed_wavelengths,
    10**(fit_linear_function(np.log10(observed_wavelengths), *params)),
    label='Fitted Line',
    color='red'
)

plt.xlabel('Wavelength')
plt.ylabel('Flux')
plt.title('Spectral Data Fitting')
plt.legend()
plt.grid(True)
plt.show()

# Print fit results
slope, intercept = params
print(f"Fitted Slope: {slope:.3f}")
print(f"Fitted Intercept: {intercept:.3f}")