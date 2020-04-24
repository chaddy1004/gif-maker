import fire
import imageio
import os
from glob import glob as glob
from PIL import Image


def create_gif(filename, src_dir, tar_dir, width=None, height=None, loop=0, fps=10, palettesize=256,
               subrectangles=False):
    filename_abs = os.path.join(tar_dir, filename)
    src_dir_all = os.path.join(src_dir, "*")
    print(f"src_dir: {src_dir_all}")
    print(f"tar_dir: {filename_abs}")
    img_uris = sorted(glob(src_dir_all))
    imgs = []
    _width, _height, _ = imageio.imread(img_uris[0]).shape
    dim_set = True
    if width is None:
        dim_set = False
        width = _width
    if height is None:
        height = _height

    for img_uri in img_uris:
        _width, _height, _ = imageio.imread(img_uris[0]).shape
        if not dim_set and (width != _width or height != _height):
            raise ValueError("The images are not consistent size. Please indicate the size")

        img = Image.open(img_uri)
        img = img.resize(size=(width, height), resample=Image.NEAREST)
        imgs.append(img)
    imageio.mimwrite(uri=filename_abs, ims=imgs, format="GIF", loop=loop, fps=fps, palettesize=palettesize,
                     subrectangles=subrectangles)
    return


if __name__ == '__main__':
    fire.Fire(create_gif)
