from typing import *

import matplotlib.pyplot as plt
import numpy as np
import torch
from skimage.color import gray2rgb
from skimage.transform import resize


class Drosophila2Dataset(torch.utils.data.Dataset):
    def __init__(
        self,
        inp: List[List[Union[str, np.ndarray]]],
        load_f: Callable = lambda x: plt.imread(x),
        img_size: List[int] = [256, 512],
        heatmap_size: List[int] = [64, 128],
        augmentation: bool = False,
    ):
        self.inp = inp
        self.load_f = load_f
        self.img_size = img_size
        self.heatmap_size = heatmap_size
        self.augmentation = augmentation

    def __getitem__(self, idx):
        img_path, pts2d = self.inp[idx]
        img = self.load_f(img_path)
        img = resize(img, self.img_size)

        # gray2rgb
        if img.ndim == 2:
            img = gray2rgb(img)

        # h w c -> c h w
        img = img.transpose(2, 0, 1)

        # remove the mean
        img = img - 0.22

        return img, pts2d, tuple(self.inp[idx])

    def __len__(self):
        return len(self.inp)
