import io
import re
from io import BytesIO
from pathlib import Path
from typing import List, Optional, Tuple

import requests
from mutagen.flac import Picture
from mutagen.id3 import PictureType
from natsort import os_sort_key
from PIL import Image

rjid_pat = re.compile(r"RJ[0-9]{6}", flags=re.IGNORECASE)


def _split(audio_files: List[Path]) -> List[List[Path]]:
    regexes = [
        r'^omake_?.*[0-9]{1,2}.*$',
        r'^.*ex[0-9]{1,2}.*$',
        r'^ex_.+$',
        r'^後日談.*$',
        r'^おまけ_?[0-9]{0,2}.*$',
        r'^反転おまけ_?[0-9]{1,2}.*$',
        r'^反転_?[0-9]{1,2}.*$',
        r'^20..年?[0-9]{1,2}月配信.*$',
        r'^.*特典.*$',
        r'^追加[0-9]{1,2}.*$',
        r'^opt[0-9]?.*',
        r'^#[0-9]+(-|ー)B',
        r'^#[0-9]+(-|ー)C',
        r'^ASMR_.*',
        r'^.+Bパート',
        r'^番外編',
    ]  # regex expressions must keep no collision with each other

    results = {}
    paths = []
    regular = []
    for audio_file in audio_files:
        matched = False
        for regex_expr in regexes:
            if re.match(regex_expr, audio_file.stem, re.IGNORECASE):
                matched = True
                if results.get(regex_expr):
                    results[regex_expr].append(audio_file)
                else:
                    results[regex_expr] = [audio_file]
                break

        if not matched:
            regular.append(audio_file)

    if len(regular):
        paths.append(regular)

    for _, v in results.items():
        paths.append(v)

    return paths


def _walk(basepath: Path):
    dirs = []
    files = []
    for file in basepath.iterdir():
        if file.is_dir():
            dirs.append(file)
        else:
            files.append(file)
    yield files

    dirs = sorted(dirs, key=lambda d: os_sort_key(d.name))
    for d in dirs:
        for f in _walk(d):
            yield f


def get_audio_paths_list(
        basepath: Path) -> Tuple[List[List[Path]], List[List[Path]]]:
    """get audio files(Path) from base_path recursively

    Args:
        base_path (Path): base path

    Returns:
        Tuple[List[List[Path]], List[List[Path]]]: flac_paths_list, mp3_paths_list
    """
    flac_paths_list = []
    mp3_paths_list = []

    for files in _walk(basepath):
        mp3_paths = []
        flac_paths = []
        for file in files:
            if file.name.endswith(".flac"):
                flac_paths.append(file)
            elif file.name.endswith(".mp3"):
                mp3_paths.append(file)

        if len(flac_paths):
            flac_paths_list.extend(_split(flac_paths))
        if len(mp3_paths):
            mp3_paths_list.extend(_split(mp3_paths))

    return flac_paths_list, mp3_paths_list


def get_rjid(name: str) -> Optional[str]:
    """get rjid(or say, rj code) from a string

    Args:
        name (str): a string

    Returns:
        Optional[str]: return a string(upper case, like RJ123123) if found, otherwise return None
    """
    m = rjid_pat.search(name)
    if m:
        return m.group().upper()
    return None


def get_image(url: str) -> Image.Image:
    cover_path = requests.get(url, stream=True).raw
    return Image.open(cover_path)


def get_png_byte_arr(im: Image.Image) -> BytesIO:
    img_byte_arr = io.BytesIO()
    im.save(img_byte_arr, "png")
    return img_byte_arr


mode_to_bpp = {
    '1': 1,
    'L': 8,
    'P': 8,
    'RGB': 24,
    'RGBA': 32,
    'CMYK': 32,
    'YCbCr': 24,
    'I': 32,
    'F': 32
}


def get_picture(png_byte_arr: BytesIO, width: int, height: int,
                mode: str) -> Picture:
    picture = Picture()
    picture.mime = "image/png"
    picture.width = width
    picture.height = height
    picture.type = PictureType.COVER_FRONT

    picture.depth = mode_to_bpp[mode]
    picture.data = png_byte_arr.getvalue()

    return picture
