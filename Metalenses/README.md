# TwoSiPM Metalens Holder & Windows Integration

## Project Overview

This repository contains the CAD designs and technical documentation for a customized **dual-SiPM holder system** featuring a **metalens slot**. 

The primary scientific goal of this project is to compare the light collection performance between two configurations:
* **Side A:** A **$3\times3\text{ mm}^2$ SiPM + Metalens** ($f \approx 10\text{ mm}$).
* **Side B:** A standalone **$6\times6\text{ mm}^2$ SiPM** (without metalens).

Since the effective collection area of the metalens combined with the $3\times3\text{ mm}^2$ SiPM should match the active area of the standalone $6\times6\text{ mm}^2$ SiPM, this experimental setup allows us to evaluate if focusing light onto a smaller sensor using a metalens yields comparable signal response while preserving optical symmetry.


## Design Evolution & Key Modifications

This design is adapted from the original 3D model created by **Mathias** for the **Graphene Project** (dual $6\times6\text{ mm}^2$ SiPM holder with circular windows for graphene).



## Technical Considerations & Alignment Warning

> **IMPORTANT ALIGNMENT NOTE FOR FABRICATION:**
> 
> * **Current Design Assumption:** The current CAD models align the geometric center of the window opening directly with the center of the SiPM active area.
> * **Metalens Substrate Offset:** Many fabricated metalenses are **not perfectly centered** on their square substrate. 
> * **Adjustment Requirement:** Depending on the exact position of the metalens pattern on its physical substrate, it may be necessary to adjust the lateral placement of the $3\times3\text{ mm}^2$ SiPM pocket. 
> * **Symmetry Constraint:** When adjusting the $3\times3\text{ mm}^2$ side, ensure maximum overall symmetry is maintained relative to the $6\times6\text{ mm}^2$ side so that ambient/incident light distribution remains identical for both channels.
