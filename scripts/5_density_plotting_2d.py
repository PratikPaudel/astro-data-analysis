"""
2D Density Plot Generator

This script creates a 2D density plot from normally distributed random data.
It uses Kernel Density Estimation (KDE) to visualize the concentration of data points.

Required Libraries:
- numpy: For numerical operations and random number generation
- matplotlib: For plotting
- scipy.stats: For kernel density estimation
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde

# Configuration Parameters
PLOT_CONFIG = {
    'n_points': 200,    # Number of random points to generate
    'spread': 0.3,      # Standard deviation of the normal distribution
    'center': 3,        # Mean of the normal distribution
    'bins': 40,         # Number of grid bins for density calculation
    'padding': 0.2,     # Padding around the data limits
    'bandwidth': 0.15,  # Bandwidth parameter for KDE
    'xlim': (2, 4),     # x-axis limits for the plot
    'ylim': (2, 4)      # y-axis limits for the plot
}

def generate_random_data(n_points: int, center: float, spread: float) -> tuple[np.ndarray, np.ndarray]:
    """
    Generate random normally distributed data points.
    
    Args:
        n_points (int): Number of points to generate
        center (float): Mean of the distribution
        spread (float): Standard deviation of the distribution
    
    Returns:
        tuple: x and y coordinates of the random points
    """
    np.random.seed(42)  # Set seed for reproducibility
    x = np.random.normal(loc=center, scale=spread, size=n_points)
    y = np.random.normal(loc=center, scale=spread, size=n_points)
    return x, y

def create_grid(x: np.ndarray, y: np.ndarray, bins: int, padding: float) -> tuple[np.ndarray, np.ndarray]:
    """
    Create a grid for density calculation.
    
    Args:
        x, y (array): Data point coordinates
        bins (int): Number of bins for the grid
        padding (float): Extra space around the data limits
    
    Returns:
        tuple: Meshgrid arrays for x and y coordinates
    """
    xmin, xmax = x.min() - padding, x.max() + padding
    ymin, ymax = y.min() - padding, y.max() + padding
    xx, yy = np.meshgrid(np.linspace(xmin, xmax, bins),
                        np.linspace(ymin, ymax, bins))
    return xx, yy

def calculate_density(x: np.ndarray, y: np.ndarray, xx: np.ndarray, yy: np.ndarray, bandwidth: float) -> np.ndarray:
    """
    Calculate the density using Gaussian KDE.
    
    Args:
        x, y (array): Data point coordinates
        xx, yy (array): Meshgrid arrays
        bandwidth (float): Bandwidth parameter for KDE
    
    Returns:
        array: Density values on the grid
    """
    positions = np.vstack([xx.ravel(), yy.ravel()])
    values = np.vstack([x, y])
    kernel = gaussian_kde(values, bw_method=bandwidth)
    return kernel(positions).reshape(xx.shape)

def create_density_plot():
    """
    Create and display the density plot.
    """
    # Generate random data
    x, y = generate_random_data(
        PLOT_CONFIG['n_points'],
        PLOT_CONFIG['center'],
        PLOT_CONFIG['spread']
    )
    
    # Set up the plot
    plt.figure(figsize=(10, 8))
    
    # Create grid and calculate density
    xx, yy = create_grid(x, y, PLOT_CONFIG['bins'], PLOT_CONFIG['padding'])
    zz = calculate_density(x, y, xx, yy, PLOT_CONFIG['bandwidth'])
    
    # Create the density plot
    density_plot = plt.pcolormesh(xx, yy, zz, cmap='Blues', shading='auto')
    
    # Add plot elements
    plt.colorbar(density_plot, label='Point Density')
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.title('2D Density Distribution of Random Points')
    plt.grid(True, alpha=0.3)
    
    # Set axis limits to focus on the data
    plt.xlim(PLOT_CONFIG['xlim'])
    plt.ylim(PLOT_CONFIG['ylim'])
    
    plt.show()

# Execute the plot creation if script is run directly
if __name__ == "__main__":
    create_density_plot()
