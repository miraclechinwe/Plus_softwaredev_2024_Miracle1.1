import rasterio
from rasterio.plot import show
import matplotlib.pyplot as plt
import numpy as np

# Define file paths for Red and NIR bands
red_band_file = r'C:\Users\HP\DATA\landsat\LC08_L1TP_091084_20210309_20210315_01_T1_B4.tif'
nir_band_file = r'C:\Users\HP\DATA\landsat\LC08_L1TP_091084_20210309_20210315_01_T1_B5.tif'

# Open Red band
with rasterio.open(red_band_file) as red_band:
    red_img = red_band.read(1)  # Read band 1

# Open NIR band
with rasterio.open(nir_band_file) as nir_band:
    nir_img = nir_band.read(1)  # Read band 1

# Visualize Red band
plt.figure(figsize=(10, 10))
plt.imshow(red_img, cmap='Reds')
plt.colorbar(label='Pixel Value')
plt.title('Landsat 8 Red Band (Band 4)')
plt.axis('off')
plt.show()

# Visualize NIR band
plt.figure(figsize=(10, 10))
plt.imshow(nir_img, cmap='Greens')
plt.colorbar(label='Pixel Value')
plt.title('Landsat 8 NIR Band (Band 5)')
plt.axis('off')
plt.show()

# Calculate NDVI
red_img = red_img.astype(float)
nir_img = nir_img.astype(float)
ndvi = (nir_img - red_img) / (nir_img + red_img)

# Plot NDVI
plt.figure(figsize=(10, 10))
plt.imshow(ndvi, cmap='viridis', vmin=-1.0, vmax=1.0)  # Set colorbar limits for NDVI range (-1 to 1)
plt.colorbar(label='NDVI')
plt.title('Normalized Difference Vegetation Index (NDVI)')
plt.axis('off')
plt.show()
