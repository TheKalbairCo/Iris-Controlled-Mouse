
# Iris Controlled Mouse

This project is a Python-based solution that enables hands-free control of the mouse using eye movements. Utilizing advanced machine learning and computer vision libraries, the script detects the position of your iris and translates those movements into mouse actions. It employs `Mediapipe` for iris detection, `OpenCV` (`cv2`) for video processing, and `PyAutoGUI` to simulate mouse movement and clicks.

## Features:
- **Eye-based Cursor Control**: The script tracks your eye movement and moves the cursor accordingly.
- **Click Functionality**: Predefined eye gestures trigger left and right mouse clicks.
- **Real-time Video Capture**: Uses your device's camera to process the real-time position of the iris.
- **Custom Sensitivity**: Adjustable sensitivity settings for smoother and more precise control.
- **Lightweight & Efficient**: Built with efficiency in mind, allowing for a smooth real-time experience with minimal computational load.

## How it Works:
The script captures video from your webcam, processes each frame with `Mediapipe` to detect facial landmarks, specifically focusing on the iris position. Based on the relative movement of your iris, it calculates and maps the motion to the screen, moving the cursor accordingly. Custom eye gestures can be used to simulate left or right mouse clicks.

## Libraries Used:
- **Mediapipe**: For detecting facial landmarks and tracking the iris.
- **cv2 (OpenCV)**: For handling video capture and image processing.
- **PyAutoGUI**: For simulating mouse movements and clicks.

## Project Structure:
- `main.py`: The final rendition of this project, containing the complete code for iris tracking and mouse control. This script integrates all features and settings for seamless interaction.
- `requirements.txt`: List of dependencies needed to run the project.
- `config.py` (optional): You can add a config file for storing sensitivity settings and customizable parameters for fine-tuning the experience.

## How to Use:
1. Clone the repository and install the necessary dependencies from `requirements.txt`.
2. Run `main.py` to start the real-time iris-controlled mouse system.
3. Adjust the sensitivity settings if needed to fit your screen and preferred control style.

---

Let me know if you’d like any further adjustments!
