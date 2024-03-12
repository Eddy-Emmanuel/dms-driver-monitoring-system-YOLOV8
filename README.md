# DMS Driver Monitoring System (YOLOv8)

![Owner Avatar](owner_avatar_link)

## Overview

This repository contains the implementation of a Driver Monitoring System (DMS) using YOLOv8, a state-of-the-art object detection algorithm. The system is designed to detect and monitor the driver's behavior and alert in case of drowsiness, distraction, or other hazardous driving situations.

## Features

- Utilizes YOLOv8 for real-time object detection.
- Monitors driver behavior including drowsiness and distraction.
- Alerts the driver in case of potential hazards.
- Supports integration with various camera feeds.
- Easy-to-use interface for monitoring and analysis.

## Files

- **app.py**: Main Python script containing the implementation of the DMS.
- **best.pt**: Pre-trained YOLOv8 model weights for object detection.
- **dms-driver-monitoring-system.html**: HTML file for user interface.
- **dms-driver-monitoring-system.ipynb**: Jupyter notebook containing the development process and analysis.
- **dms-driver-monitoring-system.pdf**: PDF documentation for the DMS.

## Getting Started

To get started with the DMS, follow these steps:

1. Clone the repository:

```bash
git clone https://github.com/Eddy-Emmanuel/dms-driver-monitoring-system-YOLOV8.git
```

2. Install the necessary dependencies:

```bash
pip install -r requirements.txt
```

3. Run the `app.py` script:

```bash
python app.py
```

4. Access the DMS interface through a web browser at `http://localhost:5000`.

## Usage

Once the DMS is running, follow these steps to use it:

1. Ensure that the camera feed is properly configured.
2. The DMS will start detecting objects and monitoring the driver's behavior in real-time.
3. In case of any hazardous behavior detected, the system will issue alerts.

## Contributing

Contributions to the DMS project are welcome! Feel free to fork the repository and submit pull requests with your improvements.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- The implementation of YOLOv8 is based on the work by the original authors.
- Special thanks to contributors and supporters of the project.

---

Feel free to customize this README according to your project's specific details and requirements.
