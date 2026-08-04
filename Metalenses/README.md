# Two SiPM Metalens Holder & Windows

## Project Overview

This repository contains the CAD designs and technical documentation for a customized **dual-SiPM holder system** featuring a **metalens slot**. 

The primary scientific goal of this project is to compare the light collection performance between two configurations:
* **Side A:** A **$3\times3\text{ mm}^2$ SiPM + Metalens** ($f \approx 10\text{ mm}$).
* **Side B:** A standalone **$6\times6\text{ mm}^2$ SiPM**.

Since the effective collection area of the metalens combined with the $3\times3\text{ mm}^2$ SiPM should match the active area of the standalone $6\times6\text{ mm}^2$ SiPM, this experimental setup allows us to evaluate if focusing light onto a smaller sensor using a metalens yields comparable signal response while preserving optical symmetry.


## Design Description

This design is adapted from the original 3D model created by **Mathias** for the **Graphene Project** (dual $6\times6\text{ mm}^2$ SiPM holder with circular windows for graphene).

### 1. Main Holder  (`TwoSiPM_Metalens_Holder`)
* **Geometry:** Designed to interface directly with the PCB designed to go inside the **flash lamp**.
* **Sensor Accommodation:** Features custom mounting pockets to hold one $3\times3\text{ mm}^2$ SiPM on one side and one $6\times6\text{ mm}^2$ SiPM on the opposite side.
* **Central wall:** Includes a central wall designed to make sure that what is happening on one side of the holder is not visible by the other side.

### 2. Windows (`LeftWindow` & `RightWindow`)
* **Attachment Mechanism:** The windows mount to the top and bottom of the main holder body using vertical pass-through screws through holes, secured with nuts.
* **Optical Symmetry:** Both windows share identical geometries to ensure identical light entrance conditions and optical paths for both SiPM channels.
* **Metalens Slot:** Includes a slot designed to slide in a metalens, positioned at a focal distance of approximately **$10\text{ mm}$** from the $3\times3\text{ mm}^2$ SiPM face.


## echnical Considerations & Alignment Warning

> * **Current Design Assumption:** The current CAD models align the geometric center of the window opening directly with the center of the SiPM active area.
> * **Metalens Substrate Offset:** Many fabricated metalenses are **not perfectly centered** on their square substrate. 
> * **Adjustment Requirement:** Depending on the exact position of the metalens pattern on its physical substrate, it may be necessary to adjust the lateral placement of the $3\times3\text{ mm}^2$ SiPM pocket. 
> * **Symmetry Constraint:** When adjusting the $3\times3\text{ mm}^2$ side, ensure maximum overall symmetry is maintained relative to the $6\times6\text{ mm}^2$ side so that ambient/incident light distribution remains identical for both channels.
