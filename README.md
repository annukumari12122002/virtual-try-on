## Virtual-Try_ON ; Official PyTorch Implementation



![Teaser image](./assets/teaser.png)

> Paper: https://arxiv.org/abs/2103.16874<br>
> Project page: https://psh01087.github.io/VITON-HD

> **Abstract:** Image-based virtual try-on transfers a target clothing item onto a person's corresponding region, typically achieved by fitting the item to the desired body part and fusing it with the person. Despite numerous studies, synthesized images' resolution remains limited (e.g., 256x192), posing a challenge in satisfying online consumers. We identify key challenges: as resolution increases, artifacts in misaligned areas between warped clothes and desired regions become noticeable; existing architectures struggle to generate high-quality body parts and maintain clothing texture sharpness. To overcome these challenges, we introduce VITON-HD, a method synthesizing 1024x768 virtual try-on images. We employ segmentation maps to guide synthesis, roughly fit target clothing to a person's body, and introduce ALIgnment-Aware Segment (ALIAS) normalization and generator to handle misaligned areas and preserve details. Through rigorous comparisons, VITON-HD significantly surpasses baselines in synthesized image quality, both qualitatively and quantitatively.

## Installation

Clone this repository:

```
https://github.com/annukumari12122002/virtual-try-on.git
```

Install PyTorch and other dependencies:

```
conda create -y -n env python=3.8
conda activate env
conda install -y pytorch==1.6.0 torchvision cudatoolkit==9.2 -c pytorch
pip install opencv-python torchgeometry
```

## Dataset

We collected 1024 x 768 virtual try-on dataset for **our research purpose only**.
You can download a preprocessed dataset from [VITON-HD DropBox](https://www.dropbox.com/s/10bfat0kg4si1bu/zalando-hd-resized.zip?dl=0).
The frontal view woman and top clothing image pairs are split into a training and a test set with 11,647 and 2,032 pairs, respectively. 


## Pre-trained networks

We provide pre-trained networks and sample images from the test dataset. Please download `*.pkl` and test images from the [VITON-HD Google Drive folder](https://drive.google.com/drive/folders/0B8kXrnobEVh9fnJHX3lCZzEtd20yUVAtTk5HdWk2OVV0RGl6YXc0NWhMOTlvb1FKX3Z1OUk?resourcekey=0-OIXHrDwCX8ChjypUbJo4fQ&usp=sharing) and unzip `*.zip` files. `test.py` assumes that the downloaded files are placed in `./checkpoints/` and `./datasets/` directories.

## Testing

To generate virtual try-on images, run:

``
python test.py --name [NAME]

```

The results are saved in the `./results/` directory. You can change the location by specifying the `--save_dir` argument. To synthesize virtual try-on images with different pairs of a person and a clothing item, edit `./datasets/test_pairs.txt` and run the same command.

## License

All material is made available under [Creative Commons BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). You can **use, redistribute, and adapt** the material for **non-commercial purposes**, as long as you give appropriate credit by **citing our paper** and **indicate any changes** that you've made.

## Citation

If you find this work useful for your research, please cite our paper:

```
@inproceedings{choi2021viton,
  title={VITON-HD: High-Resolution Virtual Try-On via Misalignment-Aware Normalization},
  author={Choi, Seunghwan and Park, Sunghyun and Lee, Minsoo and Choo, Jaegul},
  booktitle={Proc. of the IEEE conference on computer vision and pattern recognition (CVPR)},
  year={2021}
}
```
