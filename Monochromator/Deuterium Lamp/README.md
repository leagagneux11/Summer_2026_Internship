# Deuterium Lamp Spectrum, Calibration, Stability and Resolution Studies

This repository contains the analysis code, as well as the data files and result plots for the **VUV (vacuum ultraviolet) monochromator system** equipped with a **deuterium lamp** and **SiPM (silicon photomultiplier)** photodetectors.

The primary goal of this project phase was to reproduce the theoretical spectrum of the lamp, calibrate the angular actuator to physical wavelengths, and characterize the technical boundaries of the system (slit angular resolution and temporal stability).

---

## Table of Contents
1. [Part 1: Air-Filled Measurements – Theoretical Model Validation](#part-1-air-filled-measurements--theoretical-model-validation)
2. [Part 2: Vacuum Measurements – Calibration, Resolution, and Stability](#part-2-vacuum-measurements--calibration-resolution-and-stability)
3. [Conclusions and Best Practices](#conclusions-and-best-practices)

---

## Part 1: Air-Filled Measurements – Theoretical Model Validation

### Rationale
Before pulling a vacuum, the initial objective was to ensure the general functionality of the optical bench (lamp, grating, SiPM) and verify that the signal observed at ambient air matched atmospheric attenuation physics and manufacturer specifications.

### Methodology
* **Acquisition:** A short run (angular scan from -15° to 15°) was performed at atmospheric pressure.
* **Theoretical Modeling:** A Python script was developed to combine:
  1. The raw emission spectrum from the lamp's datasheet.
  2. The Photon Detection Efficiency (PDE) of the SiPM (simplified to a constant value of `0.24`).
  3. Atmospheric absorption along the optical path ($L \approx 0.7\text{ m}$) using the transmission equation:
     $$T(\lambda) = \exp\left(-\frac{\text{PATH\_LENGTH}}{L_{\text{atten}}(\lambda)}\right)$$
* **Angle-to-Wavelength ($\lambda$) Conversion Formula:**
  $$\lambda = \frac{2d \cdot \cos(\phi) \cdot \sin(\gamma \cdot (\theta - \theta_0))}{m}$$
  *(With optimized fit parameters: $d = 835.5\text{ nm}$, $\phi = 35^\circ$, $\gamma = 1.0028$, and $\theta_0 = 0.35^\circ$)*.

### Results and Insights
* **Excellent Agreement:** The calibrated experimental spectrum and the theoretical model overlaid very well.
* **Low-Wavelength Cutoff:** The complete absence of signal below 175 nm confirmed the intense absorption of air, validating the absolute necessity of vacuum conditions to explore the VUV range.

---

## Part 2: Vacuum Measurements – Calibration, Resolution, and Stability

Once the chamber was successfully pumped down to vacuum, a systematic series of runs was executed.

### 1. VUV Spectrum Reproduction and Wavelength Calibration
* **Objective:** Obtain the deuterium lamp spectrum and map the actuator steps precisely to physical wavelengths.
* **Method:** A *long run* with a fine step size of 0.01° was recorded from -15° to 15°. A minimization procedure (Chi² or fitting on the primary peak at ~160 nm) was implemented.
* **Uncertainty:** Comparing a global calibration (across all peaks) against a targeted calibration (focused on the 160 nm peak with manual overrides) yielded a wavelength discrepancy under **0.5 nm** ($\Delta\lambda = -0.36\text{ nm}$ and $-0.50\text{ nm}$ at the 128 nm and 178 nm targets respectively).
* **Hardware Warning:** Mechanical actuator faults ("position not reached") occurred consistently between 1° and 2.6°. Data within this specific window should be treated with caution.

### 2. Angular Resolution (Slit Width Optimization)
* **Objective:** Find the optimal balance between signal intensity and peak sharpness by adjusting the entrance and exit slits.
* **Method:** Fine scans (0.01° steps) were run over restricted peak zones.
  * **Test 1:** Fixed exit slit (0.01 mm), varying entrance slit (0.01 mm to 2 mm).
  * **Test 2:** Fixed entrance slit (0.01 mm), varying exit slit (0.01 mm to 0.5 mm).
* **Results:** Large slit configurations ($\ge 1\text{ mm}$) severely degraded spectral resolution. Double-Gaussian fitting proved that a **0.05 mm** opening yields the optimal trade-off. As a rule of thumb, spectral resolution is preserved as long as one slit remains narrow and the other does not exceed 1 mm.

### 3. Signal Stability over Time
* **Objective:** Evaluate if the light flux or the overall system response varies throughout the day.
* **Initial Issues:** Continuous wide scans (moving the grating from -2° to 15° every hour) led to actuator overheating, causing consecutive software crashes.
* **Miguel's Static Test:** To bypass motor stress, a static script recorded measurements every 5 minutes at a fixed angle ($5.65^\circ$) over 6 hours.
  * **Lamp Warm-up:** This data clearly demonstrated that the **deuterium lamp requires approximately 20 minutes** after power-on to reach thermal and optical stability.
* **SiPM Stabilization Study:** 
  * Short-duration baseline tests were conducted using the same script. 
  * **Power Cycling Effect:** Between each of these short runs, the SiPM was completely powered off and then powered back. The resulting data showed a distinct downward curvature at the start of each measurement.
  * **Conclusion:** This artifact indicates that the **SiPM itself requires a dedicated stabilization period** upon power-up. Once a slightly longer run was recorded without cycling the power, the curve flattened out and mirrored the stable long-term trend observed the previous day.

---

## Conclusions and Best Practices

Based on these testing phases, the following guidelines are established for upcoming runs:

1. **Warm-up Protocol:** Always turn on the system (computer, actuator, lamp, and SiPM) **at least 20 minutes before** starting data acquisition.
2. **Actuator Management:** Avoid repeated wide-range angular scans over short intervals to prevent motor overheating. Prioritize targeted scans around specific peaks of interest.
3. **Optimal Optical Setup:** Set both slits to **0.05 mm** to maximize resolution without severely sacrificing photocurrent intensity.
