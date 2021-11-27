import torch
import numpy as np
import cv2
import scipy.ndimage.filters as scifilters
from skimage.util import view_as_windows


## General Utility Functions

def channels_to_complex(X):
    return torch.complex(X[..., 0], X[..., 1])

def channels_to_complex_np(X):
    return X[..., 0] + 1j * X[..., 1]

def complex_to_channels(Z):
    RE = torch.real(Z)
    IM = torch.imag(Z)

    Z_shape = Z.shape
    if Z_shape[-1] == 1:
        RE = torch.squeeze(RE, -1)
        IM = torch.squeeze(IM, -1)

    return torch.stack([RE, IM], axis=-1)

def complex_to_channels_np(Z):
    RE = np.real(Z)
    IM = np.imag(Z)

    if Z.shape[-1] == 1:
        RE = np.squeeze(RE, (-1))
        IM = np.squeeze(IM, (-1))

    return np.stack([RE, IM], axis=-1)

def real_to_channels_np(X):
    import math
    # Create complex with zero imaginary part
    X_c = X + 0.j
    return complex_to_channels_np(X_c)