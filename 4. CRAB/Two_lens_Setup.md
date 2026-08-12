# Experimental Bench: Hybrid Metalens + Lens Setup

**Author:** Léa Gagneux
**Date:** August 12, 2026  
**Object:** Characterization of the hybrid optical system (10 mm Metalens + 75 mm Lens) with Image Intensifiers.

---

## 1. Experimental Configuration

This setup combines a 10 mm metalens in series with a 75 mm lens to focus light onto the input window of the image intensifier.

<img width="640" height="480" alt="image" src="https://github.com/user-attachments/assets/1ae01309-3b20-4fe4-a71e-794e21de1004" />


### Close-up View & Schematic
<img width="480" height="640" alt="image" src="https://github.com/user-attachments/assets/6dca766d-d5d1-4bcd-a9aa-3fc89a181839" />
<img width="600" height="256" alt="image" src="https://github.com/user-attachments/assets/4e03ab82-19f9-41b7-90ab-bad989e62b24" />

---

## 2. Experimental Observations & Data Captures

* **Illumination & Baseline:** LED voltage fixed at **5.0 V**. Default gain set to **0.5 V** (unless specified otherwise).

<img width="480" height="640" alt="image" src="https://github.com/user-attachments/assets/9953ca6c-e742-49af-bda7-ec22dfda27c4" />


### Image Capture Log

| Capture # | Position / Condition | Observations & Resolution | Image Reference |
| :---: | :--- | :--- | :---: |
| **Capture 1** | Rail distance: **345 mm** (Ian's theoretical calculation) | Image out of focus. | <img width="600" height="450" alt="frame_20260812_141615_019028" src="https://github.com/user-attachments/assets/6b80bc9c-5f89-438a-b25e-34a59911c78a" />
 |
| **Capture 2** | Metalens adjusted to **360 mm** on rail | **Optimal focal point / Best resolution achieved.** | <img width="600" height="450" alt="frame_20260812_142114_374977" src="https://github.com/user-attachments/assets/aadfae5c-a982-474c-a7b4-52b577b00cb4" />
 |
| **Capture 3** | **Flipped Metalens** (360 mm on rail) | Same focal distance and resolution. No orientation bias observed. | <img width="600" height="450" alt="frame_20260812_142503_494820" src="https://github.com/user-attachments/assets/f3bf8cbc-dff7-41a9-a727-7ff7c3b4d3e9" />
|

* **75 mm Lens Adjustment Test:** Moving the 75 mm lens away from its position degraded the focal plane and caused defocusing.
* **Gain Sweep (at 360 mm rail position):**
  * **Capture 4:** Gain = 1.0 V
    <img width="600" height="450" alt="frame_20260812_142646_008290_1V" src="https://github.com/user-attachments/assets/b1bb0070-9148-4591-af1b-4d5c4cdbb340" />

  * **Capture 5:** Gain = 1.5 V
    <img width="600" height="450" alt="frame_20260812_142710_172736_1 5V" src="https://github.com/user-attachments/assets/9823071d-a4cc-4cbf-8dbd-f46984bae978" />

  * **Capture 6:** Gain = 2.0 V
    <img width="600" height="450" alt="frame_20260812_142721_199736_2V" src="https://github.com/user-attachments/assets/96cbbbb5-a46b-41e4-afe7-f44d8ab2494d" />


---

## 3. Mechanical Discrepancy & Calculation Analysis

⚠️ **Important Note on the Holder Geometry:**
1. **Current State:** Tests were conducted with the original holder. The new holder (shorter by **10 mm**) has not been installed yet.
2. **Offset Breakdown:**
   * **Theoretical Position (Calculated by Ian):** `345 mm`
   * **Experimental Rail Position:** `360 mm`
   * **Adjusted Position (with new -10 mm holder):** `350 mm`
3. **Residual Gap:** An actual discrepancy of **~5 mm** remains between the theoretical calculations and experimental focal distance.

---

## 4. Next Steps

1. **Holder Swap:** Replace the current holder with the **10 mm shorter** version.
2. **Validation:** Re-run a focal sweep around **345-350 mm on the rail** with the new holder to confirm or refute the ~5 mm residual difference from Ian's model.
