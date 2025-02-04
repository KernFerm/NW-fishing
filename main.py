# DISCLAIMER:
# This code is provided for educational purposes only and is not intended for use in malicious activities or to promote cheating.
# This tool is designed to assist individuals with physical disabilities, aiming to enhance accessibility in gaming.
# The authors do not endorse nor condone the use of this software for violating the terms of service of any game.
# Users are advised to ensure that their use of this software complies with the game's terms of service and applicable laws.
# The developers assume no liability for any misuse of this software or any violations of terms of service agreements.

import pyautogui
import pygetwindow
import time
import random
from PIL import Image
import gc
import win32api
import win32con
import bettercam
import cv2
import numpy as np
import config
import torch
import pandas as pd
import cupy
import psutil
import colorama
import yaml
import tqdm
import matplotlib.pyplot as plt
import seaborn as sns
import requests
import IPython.display as display
import dxcam
from ultralytics import YOLO
import onnxruntime as ort
from onnxsim import simplify

def load_model():
    if config.model_path.endswith('.pt'):
        model = YOLO(config.model_path)
        model.conf = config.model_confidence_threshold
        return model
    elif config.model_path.endswith('.onnx'):
        options = ort.SessionOptions()
        options.intra_op_num_threads = 1
        options.execution_mode = ort.ExecutionMode.ORT_PARALLEL
        options.graph_optimization_level = ort.GraphOptimizationLevel.ORT_ENABLE_EXTENDED
        session = ort.InferenceSession(config.model_path, options=options)
        return session

def parse_onnx_results(results):
    detections = []
    for result in results[0]:
        detection = {'x1': result[0], 'y1': result[1], 'x2': result[2], 'y2': result[3], 'confidence': result[4], 'class': result[5]}
        detections.append(detection)
    return detections

def main():
    model = load_model()
    new_world_windows = pygetwindow.getWindowsWithTitle("New World")
    new_world_window = next((window for window in new_world_windows if window.title == "New World"), None)
    if not new_world_window:
        print("New World window not found.")
        return
    new_world_window.activate()
    center_w = new_world_window.left + (new_world_window.width / 2)
    center_h = new_world_window.top + (new_world_window.height / 2)
    win32api.SetCursorPos((int(center_w), int(center_h)))
    region = (new_world_window.left + round(new_world_window.width / 3), max(new_world_window.top, 0), new_world_window.left + (round(new_world_window.width / 3) * 2), new_world_window.top + new_world_window.height)
    camera = bettercam.create(region=region, output_color="BGRA", max_buffer_len=512)
    camera.start(target_fps=120, video_mode=True)
    time.sleep(2)

    while not win32api.GetAsyncKeyState(ord(config.quit_key)):
        frame = camera.get_latest_frame()
        sct_img = Image.fromarray(frame).convert('RGB')
        if isinstance(model, YOLO):
            results = model(sct_img)
            detections = results.pandas().xyxy[0]
        elif isinstance(model, ort.InferenceSession):
            input_tensor = np.array(sct_img).transpose(2, 0, 1).astype('float32')[None, :]
            inputs = {model.get_inputs()[0].name: input_tensor}
            results = model.run(None, inputs)
            detections = parse_onnx_results(results)

        if config.visuals:
            cv2.imshow('Live Feed', np.array(sct_img))
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        pyautogui.keyDown(config.free_cam_key)
        pyautogui.mouseDown()
        casting_time = config.casting_base_time + (config.casting_random_time * random.random())
        time.sleep(casting_time)
        pyautogui.mouseUp()
        time.sleep(2)

        for i in range(3):
            sct_img = Image.fromarray(np.array(camera.get_latest_frame()))
            if pyautogui.locateOnScreen("imgs/fishIcon.png", grayscale=True, confidence=.65):
                pyautogui.click()
                break
            time.sleep(1)

        while not win32api.GetAsyncKeyState(ord(config.quit_key)):
            sct_img = Image.fromarray(np.array(camera.get_latest_frame()))
            if pyautogui.locateOnScreen("imgs/cast.png", grayscale=True, confidence=.50):
                break
            pyautogui.mouseDown()
            if pyautogui.locateOnScreen("imgs/fishReelingOrange.png", grayscale=True, confidence=.75):
                pyautogui.mouseUp()
                time.sleep(config.line_slack_time)
            gc.collect()

        pyautogui.mouseUp()
        time.sleep(config.animation_sleep_time)
        pyautogui.keyUp(config.free_cam_key)

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        import traceback
        traceback.print_exc()
        pyautogui.keyUp('alt')  # Ensure 'alt' key is released on error
