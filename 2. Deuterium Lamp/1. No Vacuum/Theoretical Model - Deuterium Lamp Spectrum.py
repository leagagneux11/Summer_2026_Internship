import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks


def actuator_angle_to_wavelength(theta_deg):
    # Equation 20 of Max's report: m * lambda = 2 * d * cos(phi) * sin(gamma * (theta - theta0))

    d = 835.5          # nm (1 / 1200 lines/mm)
    phi = 35           # degrees (half deviation angle)
    gamma = 1.0028     # actuator scaling factor, Max's : 1.0028
    theta0 = 0.35      # degrees (angular offset), Max's : 1.502
    m = 1              # first diffraction order

    theta_rad = np.radians(theta_deg)
    theta0_rad = np.radians(theta0)
    phi_rad = np.radians(phi)

    C = 2 * d * np.cos(phi_rad)  # ≈ 1365 nm

    wavelength = (C * np.sin(gamma * (theta_rad - theta0_rad))) / m

    return wavelength

# Spectrum from Deuterium Lamp Datasheet
deuterium_wavelengths = np.array([114, 120, 122, 124, 126, 130, 132, 136, 140, 144, 148, 150, 156, 158, 161, 165, 170, 180, 200, 220, 240, 400])
deuterium_intensities = np.array([0, 42, 50, 35, 56, 25, 34, 22, 28, 26, 36, 32, 50, 155, 200, 40, 10, 8, 7, 4, 2, 0])

# Air lenght attenuation as a fonction of wavelenght
attenuation_wavelengths = np.array([50, 100, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400])
attenuation_lengths_m = np.array([1e-6, 10e-6, 0.1e-3, 1e-3, 0.01, 0.5, 5, 75, 750, 5000, 20000, 50000, 100000, 200000, 500000, 1000000, 2000000, 5000000, 10000000, 20000000, 50000000, 100000000, 200000000, 300000000, 500000000, 700000000, 1000000000, 1000000000])

def attenuation_length(lambda_nm):
    log_lengths = np.log10(attenuation_lengths_m)
    log_interp = np.interp(lambda_nm, attenuation_wavelengths, log_lengths, left=np.log10(1e-9), right=np.log10(1e12))
    return 10 ** log_interp

def air_transmission(lambda_nm, PATH_LENGTH=0.7):
    L_atten = attenuation_length(lambda_nm)
    L_atten_safe = np.where(L_atten < 1e-15, 1e-15, L_atten)
    return np.exp(-PATH_LENGTH / L_atten_safe)

PDE_CONSTANT = 0.24
PATH_LENGTH = 0.7 # Distance between

def model_spectrum(lambda_nm):
    D = np.interp(lambda_nm, deuterium_wavelengths, deuterium_intensities, left=0, right=0)
    T = air_transmission(lambda_nm, PATH_LENGTH)
    return D * PDE_CONSTANT * T

lambda_range = np.linspace(100, 400, 500)
S_lambda = model_spectrum(lambda_range)
S_lambda_norm = S_lambda / np.max(S_lambda)

# Calibration of the measured data
file_path = r"C:/Users/leaga/OneDrive/Desktop/Internship UoM/VUV Monochromator/Deuterium/deuterium_test2.txt"
data = np.loadtxt(file_path, delimiter=',', usecols=(0, 1))

angle = data[:, 0]
photocurrent = data[:, 1]

wavelength_calibrated = actuator_angle_to_wavelength(angle)

# Normalization only within the 100–400 nm range for calibrated data
mask = (wavelength_calibrated >= 100) & (wavelength_calibrated <= 400)
photocurrent_norm = photocurrent / np.max(photocurrent[mask])

# Plots
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Plot 1 : Raw data
axes[0].plot(angle, photocurrent_norm, 'b-', linewidth=1.5)
axes[0].set_xlabel('Actuator Angle (degrees)', fontsize=12)
axes[0].set_ylabel('Normalised intensity', fontsize=12)
axes[0].set_title('Raw Data S(θ)', fontsize=14)
axes[0].grid(True, alpha=0.3)
axes[0].set_xlim(-15, 15)
axes[0].set_yscale('log')

# Plot 2 : Calibrated data vs theoretical model
axes[1].plot(wavelength_calibrated, photocurrent_norm, 'b-', linewidth=1.5, label='Calibrated spectrum')
axes[1].plot(lambda_range, S_lambda_norm, 'r--', linewidth=2, alpha=0.7, label='Theoretical Model')
axes[1].set_xlabel('Wavelength (nm)', fontsize=12)
axes[1].set_ylabel('Normalised intensity', fontsize=12)
axes[1].set_title('Theoretical Model vs Calibrated Spectrum', fontsize=14)
axes[1].grid(True, alpha=0.3)
axes[1].legend()
axes[1].set_xlim(100, 400)
axes[1].set_ylim(-0.1,1.1)

plt.tight_layout()

save_path = "C:/Users/leaga/OneDrive/Desktop/Internship UoM/VUV Monochromator/Deuterium"
plt.savefig(save_path, dpi=300, bbox_inches='tight')

plt.show()