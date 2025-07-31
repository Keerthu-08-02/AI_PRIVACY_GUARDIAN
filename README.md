# AI Privacy Guardian (Prototype)

The AI Privacy Guardian is a Python-based proof-of-concept that simulates real-time detection of unauthorized content capture—such as screen recordings, screenshots, and file saves. This prototype lays the foundation for a fully-featured mobile application on Android and iOS that leverages AI and system hooks for proactive privacy protection.

## Getting Started

These instructions will help you get a copy of the project up and running on your local Windows machine for development and testing purposes.

### Prerequisites

- Python 3.x installed on your system
  - Download: https://python.org/downloads
  - During installation, ensure Add Python to PATH is checked.
- Git installed for version control and repository management
  - Download: https://git-scm.com/downloads
- VS Code (or any code editor of your choice)
  - Download: https://code.visualstudio.com/

### Installation & Setup

1. Clone the repository (or download the ZIP and extract):
   ```bash
   git clone https://github.com/YOUR_USERNAME/ai-privacy-guardian.git
   cd ai-privacy-guardian
   ```

2. (Optional but recommended) Create a virtual environment:
   ```powershell
   python -m venv venv
   .\venv\Scripts\activate
   ```
   - On PowerShell, you might need to run: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` once.

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python app/main.py
   ```

   You should see console output indicating the prototype is running, followed by simulated detection results and alerts.

## Prototype Features

- Simulated Real-Time Detection: Mimics detection of unauthorized screen recordings or screenshots using random logic.
- Alert System: Prints an alert message to the console when a simulated capture event is detected.
- Modular Codebase: Organized into `detection.py`, `alerts.py`, and utility modules for easy extension.
- Extensible Design: Architecture ready to integrate real media capture detection and AI models.

## Future Work

1. Hardware-Level Detection
   - Integrate with webcam/microphone via `OpenCV`, `pyaudio`, or `MediaPipe` to detect real unauthorized use.
   - Implement background screen monitoring for actual screenshot/screen-record detection using OS hooks or mobile APIs.

2. Cross-Platform Mobile App
   - Develop native Android/iOS apps using Flutter or React Native.
   - Use TensorFlow Lite or ONNX to run ML models on-device.
   - Leverage platform-specific APIs (e.g., Android's MediaProjection).

3. Cloud Integration
   - Backend (e.g., Firebase, Django) for logging detection events, push notifications, and user management.
   - Sync settings across multiple devices.

4. Advanced AI Models
   - Train models to recognize visual cues (e.g., screen flashes, camera icons).
   - Use anomaly detection for unusual media access patterns.

5. Enterprise Solutions
   - Corporate deployments for data loss prevention (DLP).
   - Compliance reporting and audit logs.

6. User Customization
   - User-configurable detection sensitivity levels.
   - Selective protection (text, audio, video).

## Project Structure
ai_privacy_guardian/
├── app/
│   ├── main.py       # Entry point
│   ├── detection.py  # Simulated detection logic
│   ├── alerts.py     # Alerting mechanism
│   └── utils.py      # Helper functions
├── assets/           # Static assets (e.g., logo.png)
├── models/           # Placeholder for ML models (dummy_model.pkl)
├── requirements.txt  # Python dependencies
├── README.md         # Project overview and instructions
└── .gitignore        # Git ignore rules
