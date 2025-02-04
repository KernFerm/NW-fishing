# 🎣 New World Fishing Bot Auto Setup

Welcome to the **New World Fishing Bot Auto Setup**! This script automates the installation of **Python 3.11.9**, detects your **GPU type (NVIDIA or AMD)**, and installs all necessary dependencies to get you started with automated fishing in "New World". 🚀🐟

## 📜 Features
- ✅ **Automatically installs Python 3.11.9** if it's not already installed on your system.
- ✅ **Detects NVIDIA and AMD GPU setups** to install the appropriate dependencies.
- ✅ **Guides NVIDIA users through CUDA & cuDNN setup**.
- ✅ **Ensures necessary software like Visual Studio 2022 is installed** for building dependencies.
- ✅ **Automatic dependency installation** based on the detected GPU.
- ✅ **Supports systems without admin privileges** for most operations.

---

## 🔧 Installation Guide

### 1️⃣ Run the Script
- **Double-click** `New-World-Fishing-Bot-Auto-Setup.bat`.
- **Type `Y` and press Enter** to begin the installation.

### 2️⃣ Python Installation 🐍
If Python **is not installed**, the script will:
- **Download and Install Python 3.11.9**.
- **Automatically add Python to PATH**.

If Python **is already installed**, it will **skip this step**. ✅

### 3️⃣ GPU Detection 🎮
- The script will detect if you have an **NVIDIA or AMD GPU**, or if it's a **CPU-only system**.
- It will then install the correct **Python dependencies** based on your GPU type.

---

## 🔹 NVIDIA Users (⚠️ Manual Steps Required)
### 4️⃣ Install CUDA & cuDNN
- You **must** create a **free NVIDIA Developer account**.
- Manually download and install:
  - **CUDA 11.8**: [Download Here](https://developer.nvidia.com/cuda-11-8-0-download-archive)
  - **cuDNN**: [Download Here](https://developer.nvidia.com/rdp/cudnn-download)
- **Extract cuDNN** to your CUDA directory.

### 5️⃣ Install Visual Studio 2022 🛠️
- **Download and install Visual Studio 2022 Community Edition** from [here](https://visualstudio.microsoft.com/vs/community/).
- **Select** the `Desktop development with C++` workload during installation.

## 🔹 NVIDIA Users (⚠️ Manual Steps Required)
### 6️⃣ Install NVIDIA Libraries 📦
Ensure you have Visual Studio 2022 and CUDA Toolkit 11.8 installed with the appropriate environment variables set.
- Run the following commands to install NVIDIA-specific Python libraries:

```
python -m pip install torch==2.6.0+cu118 torchvision==0.21.0+cu118 torchaudio==2.6.0+cu118 --index-url https://download.pytorch.org/whl/cu118
python -m pip install "https://github.com/cupy/cupy/releases/download/v13.3.0/cupy_cuda11x-13.3.0-cp311-cp311-win_amd64.whl"
python -m pip install "C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.8\python\tensorrt-8.6.1-cp311-none-win_amd64.whl"
python -m pip install nvidia-ml-py3 nvidia-pyindex tensorrt torch==2.6.0+cu118 torchvision==0.21.0+cu118 torchaudio==2.6.0+cu118 numpy opencv-python comtypes pandas cupy-cuda11x bettercam psutil colorama ultralytics PyAutoGUI PyGetWindow pywin32 pyyaml tqdm matplotlib seaborn requests ipython dxcam onnx==1.17.0 onnxruntime-gpu==1.20.1 onnx-simplifier onnxruntime==1.20.1
```

## 🔸 AMD Users 🎮

4️⃣ Install AMD Libraries 📦
Ensure your system has Visual Studio 2022 installed with the C++ workload.
Run the following commands to install AMD compatible Python libraries:

```
python -m pip install torch torchvision torchaudio torch-directml onnx onnx-simplifier onnxruntime onnxruntime-directml numpy opencv-python comtypes pandas cupy bettercam psutil colorama ultralytics PyAutoGUI PyGetWindow pywin32 pyyaml tqdm matplotlib seaborn requests ipython dxcam
```

## 🔸 CPU-Only Users 💻
No special hardware-dependent steps required. Install the necessary libraries:

```
python -m pip install torch torchvision torchaudio onnx onnx-simplifier onnxruntime numpy opencv-python comtypes pandas cupy bettercam psutil colorama ultralytics PyAutoGUI PyGetWindow pywin32 pyyaml tqdm matplotlib seaborn requests ipython dxcam
```
