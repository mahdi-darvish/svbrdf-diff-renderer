# -*- coding: utf-8 -*-
#
# Copyright (c) 2023, Yu Guo. All rights reserved.

import os
import cv2
import numpy as np
from PIL import Image


def imread(filename, flag=None, dim=None):
    im = cv2.imread(str(filename), flags=cv2.IMREAD_ANYDEPTH | cv2.IMREAD_UNCHANGED)

    if dim is not None:
        im = imresize(im, dim)

    match im.dtype:
        case "uint8":
            im = im.astype("float32") / 255
        case "uint16":
            im = im.astype("float32") / 65535
        case _:
            im = im.astype("float32")

    match flag:
        case "srgb":
            if im.ndim != 3 or im.shape[2] != 3:
                print(f"[ERROR:imageio:imread:srgb] {filename} should be a 3 channel image")
                exit()
            im = im[:, :, [2, 1, 0]]

        case "rough":
            if im.ndim == 3 and im.shape[2] == 3:
                im = np.mean(im, axis=2)
            elif im.ndim == 2:
                im = im
            else:
                print(f"[ERROR:imageio:imread:rough] {filename} should be a 3 or 1 channel image")
                exit()

        case "normal":
            if im.ndim != 3 or im.shape[2] != 3:
                print(f"[ERROR:imageio:imread:normal] {filename} should be a 3 channel image")
                exit()
            im = im[:, :, [2, 1, 0]]
            im = im * 2 - 1
            im_norm = np.linalg.norm(im, axis=2)
            im_norm = np.dstack((im_norm, im_norm, im_norm))
            im /= im_norm

    return im


def imwrite(im, filename, flag=None, dim=None):

    if dim is not None:
        im = imresize(im, dim)

    match flag:
        case "srgb":
            im = im.clip(0, 1)
            im = im[:, :, [2, 1, 0]]

        case "rough":
            im = im.clip(0, 1)

        case "normal":
            im = (im.clip(-1, 1) + 1) / 2
            im = im[:, :, [2, 1, 0]]

    im = (im * 255).astype("uint8")
    cv2.imwrite(str(filename), im)


def imresize(im, dim):
    return cv2.resize(im, dim, interpolation=cv2.INTER_LANCZOS4)


def imconcat(im_list, size=(2, 2)):
    w, h = size
    im_col = []
    for i in range(h):
        im_row = []
        for j in range(w):
            im_row.append(im_list[i*w+j])
        im_col.append(cv2.hconcat(im_row))
    im = cv2.vconcat(im_col)

    return im


def img9to1(folder):
    ims = []
    for i in range(9):
        ims.append(imread(folder / f"{i:02d}.png"))

    im = imconcat(ims, (3, 3))
    imwrite(im, folder / "all.png")


def tex4to1(folder):
    normal = imread(folder / "nom.png")
    diffuse = imread(folder / "dif.png")
    specular = imread(folder / "spe.png")
    roughness = imread(folder / "rgh.png")

    if roughness.ndim == 2:
        roughness = np.dstack((roughness, roughness, roughness))

    tex = imconcat([normal, diffuse, specular, roughness])
    imwrite(tex, folder / "tex.png")


def img2gif(in_filenames, out_filename, method="Pillow"):
    if method == "Pillow":
        images = [Image.open(str(in_filename)) for in_filename in in_filenames]
        images[0].save(str(out_filename), save_all=True, append_images=images[1:], optimize=False, loop=0, duration=40)
    elif method == "ImageMagick":
        cmd = f"convert -delay 4 -loop 0 {str(in_filenames)} {str(out_filename)}"
        os.system(cmd)
    else:
        print(f"[ERROR:imageio:img2gif] Unknown method: {method}")
        exit()
