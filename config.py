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
