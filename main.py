import os
import numpy as np
from PIL import Image

def list_with_full_path(dir: str) -> list[str]:
    return [os.path.join(dir, f) for f in os.listdir(dir)]

def list_and_order(dir: str) -> list[str]:
    return sorted(list_with_full_path(dir))

def open_img_with_pil(path: str) -> Image:
    return Image.open(path)

def transform_to_np_array(img: Image) -> np.ndarray:
    return np.array(img)

def wrapper_to_numpy_array(path: str) -> np.ndarray:
    return transform_to_np_array(open_img_with_pil(path))

def calc_dice(img1: np.ndarray,
              img2: np.ndarray) -> float:
    intersection = np.sum(np.logical_and(img1, img2))
    union = np.sum(np.logical_or(img1, img2))
    dice = 2 * intersection / (intersection + union)
    return dice