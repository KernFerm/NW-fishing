# 🐟 New World Fishing Bot with CUDA Support

Welcome to the New World Fishing Bot repository! This bot automates fishing in the game "New World" using advanced machine learning techniques with CUDA acceleration for improved performance. 🎮🐠🚀

## 🌟 Features

- **Automated Fishing**: Automate your fishing activities in New World with precision.
- **CUDA Acceleration**: Utilizes NVIDIA CUDA technology to enhance object detection and processing speed.
- **Real-time Object Detection**: Powered by YOLO and ONNX models for efficient and accurate detection of fishing spots and actions within the game.
- **User-friendly Configuration**: Easy setup and customization through a simple configuration file.

## Disclaimer

This project, including all associated source code and files, is provided for **educational purposes only** and is not intended for malicious use or to promote cheating in any form. This tool is designed to assist individuals with physical disabilities who may benefit from automation in gaming environments. We strongly discourage the use of this software for any activities that violate terms of service or fair play agreements of any game or software.

By using this software, you agree to use it responsibly and ethically, adhering to the applicable laws and terms of service agreements. The developers and contributors of this project are not responsible for any misuse of this tool or any damages that arise from its use. Please use this tool in a manner that respects the rights and experience of all players.


## 🚀 Quick Start

Follow these steps to get your fishing bot up and running with CUDA acceleration:

### Prerequisites

- NVIDIA GPU with CUDA 11.8 support.
- Python 3.11.9 installed on your system.

### Installation

1. Click the Green Button Upper Right Hand Corner:
- Download `ZipFile` to desktop.
- `Extract Zipfile` to desktop.
- Open up the Folder and make sure to read the `readme.md`
- install `python`
- double click the `python3119.bat` and press `Y` to install.
- once done, `python --version`
- to see if it got installed correctly.

2. Install required Python packages:

```
pip install -r requirements.txt
```

## Configuration

Update the `config.py` to set your model paths, CUDA settings, and key bindings:

```
# config.py

# Basic interaction configurations
casting_base_time = 0.5
casting_random_time = 0.3
line_slack_time = 1.5
animation_sleep_time = 0.1
move_directions = ['a', 'd']
free_cam_key = 'alt'
visuals = False
quit_key = '8'

# Model configurations - now using names instead of full paths
model_name = 'basicv5s'  # This is the name of the model, corresponding to either a .pt or .onnx file
model_confidence_threshold = 0.4
model_classes = {'FishIcon': 0, 'CastIcon': 1, 'FishReelingOrange': 2}

# Define model file extensions and directory path
model_directory = 'input the path to the NW fishing bot directory here (e.g. C:\\Users\\username\\Desktop\\NW_Fishing_Bot\\)'
model_extension = '.pt'  # or '.onnx' based on the model you are using

# Full path construction
model_path = f"{model_directory}{model_name}{model_extension}"

# GPU and other performance settings
cuda_enabled = True  # Set to True if CUDA is available and desired
```

# 🚀 NVIDIA CUDA Installation Guide

---

## DO `EVERY STEP AND FOLLOW EVERY STEP` OF THE NVIDIA INSTALLATION GUIDE OR IT WON'T WORK PROPERLY

- **FOR `AMD USERS` MAKE SURE YOU `FOLLOW` THE GUIDE FOR `AMD GPUS`**

## For `AMD GPU SUPPORT` [click here](https://github.com/FNBUBBLES420-ORG/Assistive-AimGuide/blob/main/main_amd_scripts/dist/readme.md)

</div>

----
### 1. **Download the NVIDIA CUDA Toolkit 11.8**

First, download the CUDA Toolkit 11.8 from the official NVIDIA website:

👉 [Nvidia CUDA Toolkit 11.8 - DOWNLOAD HERE](https://developer.nvidia.com/cuda-11-8-0-download-archive)

### 2. **Install the CUDA Toolkit**

- After downloading, open the installer (`.exe`) and follow the instructions provided by the installer.
- Make sure to select the following components during installation:
  - CUDA Toolkit
  - CUDA Samples
  - CUDA Documentation (optional)

### 3. **Verify the Installation**

- After the installation completes, open the `cmd.exe` terminal and run the following command to ensure that CUDA has been installed correctly:
```
nvcc --version
```
This will display the installed CUDA version.

### **4. Install Cupy**
Run the following command in your terminal to install Cupy:
```
pip install cupy-cuda11x
```

## 5. CUDNN Installation 🧩
Download cuDNN (CUDA Deep Neural Network library) from the NVIDIA website:

👉 [Download CUDNN](https://developer.nvidia.com/downloads/compute/cudnn/secure/8.9.6/local_installers/11.x/cudnn-windows-x86_64-8.9.6.50_cuda11-archive.zip/). (Requires an NVIDIA account – it's free).

## 6. Unzip and Relocate 📁➡️
Open the `.zip` cuDNN file and move all the folders/files to the location where the CUDA Toolkit is installed on your machine, typically:

```
C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.8
```


## 7. Get TensorRT 8.6 GA 🔽
Download [TensorRT 8.6 GA](https://developer.nvidia.com/downloads/compute/machine-learning/tensorrt/secure/8.6.1/zip/TensorRT-8.6.1.6.Windows10.x86_64.cuda-11.8.zip).

## 8. Unzip and Relocate 📁➡️
Open the `.zip` TensorRT file and move all the folders/files to the CUDA Toolkit folder, typically located at:

```
C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.8
```


## 9. Python TensorRT Installation 🎡
Once all the files are copied, run the following command to install TensorRT for Python:

```
pip install "C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.8\python\tensorrt-8.6.1-cp311-none-win_amd64.whl"
```

🚨 **Note:** If this step doesn’t work, double-check that the `.whl` file matches your Python version (e.g., `cp311` is for Python 3.11). Just locate the correct `.whl` file in the `python` folder and replace the path accordingly.

## 10. Set Your Environment Variables 🌎
Add the following paths to your environment variables:
- `system path`
```
C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.8\lib
C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.8\libnvvp
C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.8\bin
```

# Setting Up CUDA 11.8 with cuDNN on Windows

Once you have CUDA 11.8 installed and cuDNN properly configured, you need to set up your environment via `cmd.exe` to ensure that the system uses the correct version of CUDA (especially if multiple CUDA versions are installed).

## Steps to Set Up CUDA 11.8 Using `cmd.exe`

### 1. Set the CUDA Path in `cmd.exe`

You need to add the CUDA 11.8 binaries to the environment variables in the current `cmd.exe` session.

Open `cmd.exe` and run the following commands:
- DO each one `Separately`
```
set PATH=C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.8\bin;%PATH%
set PATH=C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.8\libnvvp;%PATH%
set PATH=C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.8\extras\CUPTI\lib64;%PATH%
```
These commands add the CUDA 11.8 binary, lib, and CUPTI paths to your system's current session. Adjust the paths as necessary depending on your installation directory.

2. Verify the CUDA Version
After setting the paths, you can verify that your system is using CUDA 11.8 by running:
```
nvcc --version
```
This should display the details of CUDA 11.8. If it shows a different version, check the paths and ensure the proper version is set.

3. **Set the Environment Variables for a Persistent Session**
If you want to ensure CUDA 11.8 is used every time you open `cmd.exe`, you can add these paths to your system environment variables permanently:

1. Open `Control Panel` -> `System` -> `Advanced System Settings`.
Click on `Environment Variables`.
Under `System variables`, select `Path` and click `Edit`.
Add the following entries at the top of the list:
```
C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.8\bin
C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.8\libnvvp
C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.8\extras\CUPTI\lib64
```
This ensures that CUDA 11.8 is prioritized when running CUDA applications, even on systems with multiple CUDA versions.

4. **Set CUDA Environment Variables for cuDNN**
If you're using cuDNN, ensure the `cudnn64_8.dll` is also in your system path:
```
set PATH=C:\tools\cuda\bin;%PATH%
```
This should properly set up CUDA 11.8 to be used for your projects via `cmd.exe`.

#### Additional Information
- Ensure that your GPU drivers are up to date.
- You can check CUDA compatibility with other software (e.g., PyTorch or TensorFlow) by referring to their documentation for specific versions supported by CUDA 11.8.

## 🖥️ How to Use

To start the fishing bot, execute the following command in your project directory:

```
python main.py
```

- Ensure the game is running and the game window is visible. The bot will automatically handle the fishing process, utilizing GPU acceleration for processing.

## 📈 Visualization
If `config.visuals` is set to True, you can see real-time detection and actions performed by the bot through an OpenCV window.

## 📜 License

This project is licensed under the `MIT License`.


## 💖 Acknowledgements

- [NumPy](https://numpy.org/)
- [OpenCV](https://opencv.org/)
- [PyTorch](https://pytorch.org/)
- [Ultralytics YOLOv5](https://github.com/ultralytics/yolov5)
- [ONNX Runtime](https://github.com/microsoft/onnxruntime)
- [RootkitOrg](https://github.com/rootkitorg) / i made the repo better hopefully. lol

