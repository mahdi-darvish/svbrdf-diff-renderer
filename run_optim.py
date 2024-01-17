# -*- coding: utf-8 -*-
#
# Copyright (c) 2023, Yu Guo. All rights reserved.

import os
from pathlib import Path
import numpy as np
import torch as th

from src.microfacet import Microfacet
from src.svbrdf import SvbrdfIO, SvbrdfOptim
from src.materialgan import MaterialGANOptim


def optim_svbrdf(data_dir, res, epochs, tex_init=True):

    device = th.device("cuda:0" if th.cuda.is_available() else "cpu")
    # device = th.device("cpu")

    svbrdf_obj = SvbrdfIO(data_dir, device)
    targets = svbrdf_obj.load_images_th("reference", "1024", res)

    renderer_obj = Microfacet(res, svbrdf_obj.n_of_imgs, svbrdf_obj.im_size, svbrdf_obj.cl, device)

    optim_obj = SvbrdfOptim(device, renderer_obj)
    optim_obj.load_targets(targets)

    if tex_init:
        textures = svbrdf_obj.load_textures_th("reference", res)
        optim_obj.init_from_tex(textures)
    else:
        optim_obj.init_from_randn()

    optim_obj.optim(epochs)

    svbrdf_obj.save_textures_th(optim_obj.textures, "optimized", res)
    rendereds = renderer_obj.eval(optim_obj.textures)
    svbrdf_obj.save_images_th(rendereds, "optimized", res)


def optim_materialgan(data_dir, res, epochs):

    device = th.device("cuda:0" if th.cuda.is_available() else "cpu")
    # device = th.device("cpu")

    svbrdf_obj = SvbrdfIO(data_dir, device)
    targets = svbrdf_obj.load_images_th("reference", "1024", res)

    renderer_obj = Microfacet(res, svbrdf_obj.n_of_imgs, svbrdf_obj.im_size, svbrdf_obj.cl, device)

    optim_obj = MaterialGANOptim(device, renderer_obj, ckp="tool/materialgan.pth")
    optim_obj.load_targets(targets)
    optim_obj.init_from_latent()

    optim_obj.optim(epochs)

    svbrdf_obj.save_textures_th(optim_obj.textures, "optimized", res)
    rendereds = renderer_obj.eval(optim_obj.textures)
    svbrdf_obj.save_images_th(rendereds, "optimized", res)


if __name__ == "__main__":
    data_dir = Path("data/card_blue")
    # optim_svbrdf(data_dir, 256, 1000)
    optim_materialgan(data_dir, 256, 1000)