# 📏 NowYourSize – Real-World Object Measurement with ArUco Markers

**NowYourSize** is an open-source computer vision tool that allows you to **measure the real-world dimensions of objects (in cm)** using a webcam and an **ArUco marker** as a scale reference.

With a simple **mouse click**, you can measure object dimensions live and see results directly on your screen.

---

## ✨ Features

* 📏 Accurate **cm-based measurements** using ArUco markers.
* 🖱️ Interactive **click-to-measure** workflow.
* 🖼️ Real-time **bounding box visualization** with size overlay.
* 🔧 Configurable marker size for flexible usage.
* 💻 Works with any standard webcam.

---

## 🛠️ Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/NowYourSize.git
   cd NowYourSize
   ```

2. Install dependencies:

   ```bash
   pip install opencv-python opencv-contrib-python
   ```

---

## ▶️ Usage

Run the application:

```bash
python measure.py
```

### Controls:

* **Left Mouse Click** → Select object to measure.
* **ESC** → Exit program.

---

## 📂 Project Structure

```
NowYourSize/
│── measure.py        # Main application
│── README.md         # Documentation
│── aruco_marker.png  # Example ArUco marker (5 cm × 5 cm)
```

---

## 📸 Workflow

1. Print or display an **ArUco marker (default: 5 × 5 cm)**.
2. Place the marker in the camera frame with the object.
3. Run the program.
4. Click on the object → bounding box & size displayed live.

**Example Output on Screen:**

```
W: 3.45 cm, H: 7.12 cm
```

---

## 🖼️ Generate Your Own ArUco Marker

Use OpenCV to generate:

```python
import cv2
aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)
marker = cv2.aruco.generateImageMarker(aruco_dict, 0, 200)
cv2.imwrite("aruco_marker.png", marker)
```

Print the marker with a **known size** (default = 5 cm). Update `ref_length_cm` in the code if using another size.

---

## 🔮 Roadmap

* 📍 Distance measurement between **two clicked points**.
* 📑 Exporting results to **CSV/Excel**.
* 🎯 Multi-marker calibration for **greater accuracy**.
* 📱 Mobile/Android version (future idea).

---

## ⚠️ Notes

* Accuracy depends on:

  * Camera resolution & calibration
  * Proper placement of the ArUco marker
  * Lighting conditions

---

## 📜 License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

Python itself is released under the **Python Software Foundation (PSF) License**.
For more details, visit the [official license page](https://docs.python.org/3/license.html).

---

## 👨‍💻 Author

**NowYourSize** is developed by **Amit Kasbe** 🚀
Feel free to contribute, open issues, or suggest improvements!

---
