import numpy as np
import matplotlib.pyplot as plt

# MUV and H-alpha data analysis
MUV_data = [19.5, 18.94, 19.2, 17.82, 21.66, 16.71, 19.5, 21.23, 21.49, 19.61]
H_alpha_data = [7.7, 1.2, 8.2, 6.8, 6.8, 1.8, 7.6, 2.6, 1.2, 4.8]

MUV_upper_errors = [0.18, 0.08, 0.10, 0.33, 0.07, 0.31, 0.12, 0.17, 0.12, 0.27]
MUV_lower_errors = [0.18, 0.09, 1.08, 0.61, 0.07, 1.16, 0.00, 0.24, 0.12, 0.23]

H_alpha_lower_errors = [0.2, 0.1, 0.5, 0.4, 0.6, 0.2, 0.7, 0.4, 0.2, 0.8]
H_alpha_upper_errors = [0.2, 0.1, 0.7, 0.4, 0.9, 0.2, 0.8, 0.8, 0.3, 1.1]

# Create the error plot
plt.figure(figsize=(10, 6))
plt.errorbar(MUV_data, H_alpha_data,
             yerr=[H_alpha_lower_errors, H_alpha_upper_errors],
             xerr=[MUV_lower_errors, MUV_upper_errors],
             fmt='o', color="#0000FF", ecolor='red', capsize=2)

plt.xlabel('MUV')
plt.ylabel('H-alpha')
plt.title('MUV and H-alpha Data Plot with Error Bars')
plt.grid(True)
plt.show()