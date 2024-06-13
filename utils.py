import os
import cv2
import numpy as np
from PIL import Image
import torch


def gen_noise(shape):
    noise = np.zeros(shape, dtype=np.uint8)
    ### noise
    noise = cv2.randn(noise, 0, 255)
    noise = np.asarray(noise / 255, dtype=np.uint8)
    noise = torch.tensor(noise, dtype=torch.float32)
    return noise


def save_images(img_tensors, img_names, save_dir):
    os.makedirs(save_dir, exist_ok=True)
    for img_tensor, img_name in zip(img_tensors, img_names):
        tensor = (img_tensor.clone() + 1) * 0.5 * 255
        tensor = tensor.cpu().clamp(0, 255).byte()

        try:
            array = tensor.numpy()
        except:
            array = tensor.detach().numpy()

        if array.shape[0] == 1:
            array = array.squeeze(0)
        elif array.shape[0] == 3:
            array = array.transpose(1, 2, 0)

        im = Image.fromarray(array)
        im.save(os.path.join(save_dir, img_name + '.jpg'), format='JPEG')


def load_checkpoint(model, checkpoint_path):
    if not os.path.exists(checkpoint_path):
        raise ValueError("'{}' is not a valid checkpoint path".format(checkpoint_path))
    model.load_state_dict(torch.load(checkpoint_path))
