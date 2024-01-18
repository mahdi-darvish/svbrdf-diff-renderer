# MaterialGAN: Reflectance Capture using a Generative SVBRDF Model

[Yu Guo](https://tflsguoyu.github.io/), Cameron Smith, [Miloš Hašan](http://miloshasan.net/), [Kalyan Sunkavalli](http://www.kalyans.org/) and [Shuang Zhao](https://shuangz.com/).

In ACM Transactions on Graphics (SIGGRAPH Asia 2020).

<img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/github/teaser.jpg" width="1000px">

[[Paper](https://github.com/tflsguoyu/materialgan_paper/blob/master/materialgan.pdf)]
[[Code](https://github.com/tflsguoyu/svbrdf-diff-renderer)]
[[Supplemental Materials](https://tflsguoyu.github.io/materialgan_suppl/)]
[[Poster](https://github.com/tflsguoyu/materialgan_poster/blob/master/materialgan_poster.pdf)]
[Fastforward on Siggraph Asia 2020 ([Video](https://youtu.be/fD6CTb1DlbE))([Slides](https://www.dropbox.com/s/qi594y27dqa7irf/materialgan_ff.pptx?dl=0))] \
[Presentation on Siggraph Asia 2020 ([Video](https://youtu.be/CrAoVsJf0Zw))([Slides](https://www.dropbox.com/s/zj2mhrminoamrdg/materialgan_main.pptx?dl=0))]

## Python dependencies
numpy, torch, torchvision, opencv-python, lpips, tqdm, matplotlib, pupil_apriltags

## Pretrained MaterialGAN model
Download [`materialgan.pth`](https://www.dropbox.com/scl/fi/z41e6tedyh7m57vatse7p/materialgan.pth?rlkey=ykovb3owafmz6icvss13sdddl&dl=0) to `tool` folder.

## Usage
### Capture your own data with smartphone
1. Print "tool/tag36h11_print.png" on a solid paper with proper size and crop the center area.
2. Place it on the material you want to capture.
3. Turn on camera flashlight and capture images from different views.
4. Copy captured images to a certain folder (e.g "data/bath_tile") and run `python run_prepare.py`.

Tips:
1. All markers should be captured.
2. It's better to capture during night and turn off other lights.
3. Change camera mode to manual, keep white balance and focal lenth the same during the captures.

### Render
Run `python run_render.py`

### Generate textures with MaterialGAN
Run `pyton run_gentextures.py`

### Optimization on SVBRDF maps directly
Run `python run_optim_svbrdf.py`

### Optimization on MaterialGAN latent space (TODO, still working on it)
Run `python run_optim_ganlatent.py`

## Notes
- TODO: add GAN part
- 12/30/2023: Start to use this repo.
