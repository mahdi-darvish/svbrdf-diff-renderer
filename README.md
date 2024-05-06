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

## Python dependencies [torch, torchvision, opencv-python, matplotlib, pupil_apriltags]
Tested on 
1. MacOS, python3.11, pytorch2.2(CPU)
2. Windows10, python3.11, pytorch2.3, CUDA11.8 

## Pretrained MaterialGAN model
Download all the checkpoints to the folder `ckp`: 
[`materialgan.pth`](https://www.dropbox.com/scl/fi/z41e6tedyh7m57vatse7p/materialgan.pth?rlkey=ykovb3owafmz6icvss13sdddl&dl=0)
[`latent_avg_W+_256.pt`](https://www.dropbox.com/scl/fi/nf4kfoiqx6h7baxpbfu01/latent_avg_W-_256.ptrlkey=ot0yfkbgq47vt45huh65mgwit&st=724ubgqp&dl=0)
[`latent_const_W+_256.pt`](https://www.dropbox.com/scl/fi/mdh8boshpfc6lwktrfh4i/latent_const_W-_256.pt?rlkey=gy55tp5h6c91icxhdzzbf5sss&st=hzxk2580&dl=0)
[`latent_const_N_256.pt`](https://www.dropbox.com/scl/fi/320aov4ahc4wkhaq8mpve/latent_const_N_256.pt?rlkey=ckydqxdpyvzy7kns2h0geuh4e&st=d7ytmxz5&dl=0)

## Usage
See `run.py` for the details.

## Capture your own data with smartphone
1. Print "fig/tag36h11_print.png" on a solid paper with a proper size and crop the center area.
2. Measure `size`(in cm unit) with a ruler, see the red arrow line in below figure.
3. Place it on the material you want to capture, and make the paper as flat as possible.
4. Turn on camera flashlight and capture images from different views.
5. Create a data folder, e.g `data/yellow_box`, and copy captured images to `data/yellow_box/raw`.
6. Run script. 
The `size` here in `input_obj.eval(size=17, depth=0.1)` is the number you measured from step 2. `depth` is distance (in cm unit) between marker plane and material plane. For example, if you attach the markers on a thick cardboard, you should use a larger `depth`.
7. The generate target images is located in `data/yellow_box/target/1024` and corresponding `data/yellow_box/optim.json` file is generated as well.
<img src="https://github.com/tflsguoyu/svbrdf-diff-renderer/blob/master/fig/fig1.png" width="600px">

Tips:
1. All markers should be captured and in focus and the letter `A` should be facing up.
2. It's better to capture during the night or in a dark room and turn off other lights.
3. It's better to see the highlights in the cropped area.
4. Change camera mode to manual, keep white balance and focal lenth the same during the captures.
5. `.heic` image format is not supported now. Convert it to `.png`/`.jpg` first. 
6. Preferred capturing order: highlight in topleft -> top -> topright -> left -> center -> right -> bottomleft -> bottom -> bottomright. See images in `data/yellow_box/raw` as references.

## The real data we used in the paper [[Download](https://drive.google.com/file/d/1Vs2e35c4bNHRUu3ON4IsuOOP6uK8Ivji/view?usp=sharing)]
The dataset includes corresponding json files. We put our results here as reference, and you can also generate the results using our codes `run.py`.

In general, we use `ckp = ["ckp/latent_avg_W+_256.pt"]` as the initialization, as shown below.

From left to right: input photos, output texture maps (256x256) from materialgan, output high res maps (1024x1024).

<img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/bathroomtile1/target/all.jpg" width="120px"> <img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/bathroomtile1/optim_latent/256/tex.jpg" width="120px"> <img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/bathroomtile1/optim_latent/1024/tex.jpg" width="120px">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/bathroomtile2/target/all.jpg" width="120px"> <img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/bathroomtile2/optim_latent/256/tex.jpg" width="120px"> <img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/bathroomtile2/optim_latent/1024/tex.jpg" width="120px">

<img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/book1/target/all.jpg" width="120px"> <img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/book1/optim_latent/256/tex.jpg" width="120px"> <img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/book1/optim_latent/1024/tex.jpg" width="120px">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/book2/target/all.jpg" width="120px"> <img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/book2/optim_latent/256/tex.jpg" width="120px"> <img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/book2/optim_latent/1024/tex.jpg" width="120px">

<img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/cards-blue/target/all.jpg" width="120px"> <img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/cards-blue/optim_latent/256/tex.jpg" width="120px"> <img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/cards-blue/optim_latent/1024/tex.jpg" width="120px">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/cards-red/target/all.jpg" width="120px"> <img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/cards-red/optim_latent/256/tex.jpg" width="120px"> <img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/cards-red/optim_latent/1024/tex.jpg" width="120px">

<img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/giftbag1/target/all.jpg" width="120px"> <img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/giftbag1/optim_latent/256/tex.jpg" width="120px"> <img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/giftbag1/optim_latent/1024/tex.jpg" width="120px">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/giftbag2/target/all.jpg" width="120px"> <img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/giftbag2/optim_latent/256/tex.jpg" width="120px"> <img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/giftbag2/optim_latent/1024/tex.jpg" width="120px">

<img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/giftbag3/target/all.jpg" width="120px"> <img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/giftbag3/optim_latent/256/tex.jpg" width="120px"> <img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/giftbag3/optim_latent/1024/tex.jpg" width="120px">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/leather-blue/target/all.jpg" width="120px"> <img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/leather-blue/optim_latent/256/tex.jpg" width="120px"> <img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/leather-blue/optim_latent/1024/tex.jpg" width="120px">

<img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/leather-brown/target/all.jpg" width="120px"> <img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/leather-brown/optim_latent/256/tex.jpg" width="120px"> <img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/leather-brown/optim_latent/1024/tex.jpg" width="120px">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/leather-darkbrown/target/all.jpg" width="120px"> <img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/leather-darkbrown/optim_latent/256/tex.jpg" width="120px"> <img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/leather-darkbrown/optim_latent/1024/tex.jpg" width="120px">

<img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/plastic-carpet/target/all.jpg" width="120px"> <img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/plastic-carpet/optim_latent/256/tex.jpg" width="120px"> <img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/plastic-carpet/optim_latent/1024/tex.jpg" width="120px">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/plastic-foam/target/all.jpg" width="120px"> <img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/plastic-foam/optim_latent/256/tex.jpg" width="120px"> <img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/plastic-foam/optim_latent/1024/tex.jpg" width="120px">

<img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/plastic-red-carton/target/all.jpg" width="120px"> <img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/plastic-red-carton/optim_latent/256/tex.jpg" width="120px"> <img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/plastic-red-carton/optim_latent/1024/tex.jpg" width="120px">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/plastic-red-grid/target/all.jpg" width="120px"> <img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/plastic-red-grid/optim_latent/256/tex.jpg" width="120px"> <img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/plastic-red-grid/optim_latent/1024/tex.jpg" width="120px">

<img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/rubber-pattern/target/all.jpg" width="120px"> <img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/rubber-pattern/optim_latent/256/tex.jpg" width="120px"> <img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/rubber-pattern/optim_latent/1024/tex.jpg" width="120px">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/stone-bathroom-tile/target/all.jpg" width="120px"> <img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/stone-bathroom-tile/optim_latent/256/tex.jpg" width="120px"> <img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/stone-bathroom-tile/optim_latent/1024/tex.jpg" width="120px">

<img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/stone-bigtile/target/all.jpg" width="120px"> <img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/stone-bigtile/optim_latent/256/tex.jpg" width="120px"> <img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/stone-bigtile/optim_latent/1024/tex.jpg" width="120px">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/stone-smalltile/target/all.jpg" width="120px"> <img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/stone-smalltile/optim_latent/256/tex.jpg" width="120px"> <img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/stone-smalltile/optim_latent/1024/tex.jpg" width="120px">

<img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/stone-spec-granite/target/all.jpg" width="120px"> <img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/stone-spec-granite/optim_latent/256/tex.jpg" width="120px"> <img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/stone-spec-granite/optim_latent/1024/tex.jpg" width="120px">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/stone-spec-ground-flake/target/all.jpg" width="120px"> <img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/stone-spec-ground-flake/optim_latent/256/tex.jpg" width="120px"> <img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/stone-spec-ground-flake/optim_latent/1024/tex.jpg" width="120px">

<img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/stone-spec-shiny/target/all.jpg" width="120px"> <img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/stone-spec-shiny/optim_latent/256/tex.jpg" width="120px"> <img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/stone-spec-shiny/optim_latent/1024/tex.jpg" width="120px">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/stone-spec-vinyl-floor/target/all.jpg" width="120px"> <img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/stone-spec-vinyl-floor/optim_latent/256/tex.jpg" width="120px"> <img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/stone-spec-vinyl-floor/optim_latent/1024/tex.jpg" width="120px">

<img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/wall-color/target/all.jpg" width="120px"> <img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/wall-color/optim_latent/256/tex.jpg" width="120px"> <img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/wall-color/optim_latent/1024/tex.jpg" width="120px">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/wall-red-bump/target/all.jpg" width="120px"> <img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/wall-red-bump/optim_latent/256/tex.jpg" width="120px"> <img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/wall-red-bump/optim_latent/1024/tex.jpg" width="120px">

<img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/wall-plaster-green/target/all.jpg" width="120px"> <img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/wall-plaster-green/optim_latent/256/tex.jpg" width="120px"> <img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/wall-plaster-green/optim_latent/1024/tex.jpg" width="120px">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/wall-plaster-white/target/all.jpg" width="120px"> <img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/wall-plaster-white/optim_latent/256/tex.jpg" width="120px"> <img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/wall-plaster-white/optim_latent/1024/tex.jpg" width="120px">

<img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/wood-alder/target/all.jpg" width="120px"> <img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/wood-alder/optim_latent/256/tex.jpg" width="120px"> <img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/wood-alder/optim_latent/1024/tex.jpg" width="120px">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/wood-jatoba/target/all.jpg" width="120px"> <img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/wood-jatoba/optim_latent/256/tex.jpg" width="120px"> <img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/wood-jatoba/optim_latent/1024/tex.jpg" width="120px">

<img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/wood-knotty/target/all.jpg" width="120px"> <img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/wood-knotty/optim_latent/256/tex.jpg" width="120px"> <img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/wood-knotty/optim_latent/1024/tex.jpg" width="120px">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/wood-laminate/target/all.jpg" width="120px"> <img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/wood-laminate/optim_latent/256/tex.jpg" width="120px"> <img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/wood-laminate/optim_latent/1024/tex.jpg" width="120px">

<img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/wood-t/target/all.jpg" width="120px"> <img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/wood-t/optim_latent/256/tex.jpg" width="120px"> <img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/wood-t/optim_latent/1024/tex.jpg" width="120px">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/wood-tile/target/all.jpg" width="120px"> <img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/wood-tile/optim_latent/256/tex.jpg" width="120px"> <img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/wood-tile/optim_latent/1024/tex.jpg" width="120px">

<img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/wood-treeskin/target/all.jpg" width="120px"> <img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/wood-treeskin/optim_latent/256/tex.jpg" width="120px"> <img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/wood-treeskin/optim_latent/1024/tex.jpg" width="120px">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/wood-walnut/target/all.jpg" width="120px"> <img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/wood-walnut/optim_latent/256/tex.jpg" width="120px"> <img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/wood-walnut/optim_latent/1024/tex.jpg" width="120px">

<img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/wood-bamboo/target/all.jpg" width="120px"> <img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/wood-bamboo/optim_latent/256/tex.jpg" width="120px"> <img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/wood-bamboo/optim_latent/1024/tex.jpg" width="120px">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/bamboo-veawe/target/all.jpg" width="120px"> <img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/bamboo-veawe/optim_latent/256/tex.jpg" width="120px"> <img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/bamboo-veawe/optim_latent/1024/tex.jpg" width="120px">

<!-- <img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/VVVVVVVVVVV/target/all.jpg" width="120px"> <img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/VVVVVVVVVVV/optim_latent/256/tex.jpg" width="120px"> <img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/VVVVVVVVVVV/optim_latent/1024/tex.jpg" width="120px">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/VVVVVVVVVVV/target/all.jpg" width="120px"> <img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/VVVVVVVVVVV/optim_latent/256/tex.jpg" width="120px"> <img src="https://github.com/tflsguoyu/materialgan_suppl/blob/master/data/VVVVVVVVVVV/optim_latent/1024/tex.jpg" width="120px"> -->

