import exifread
import csv
import pandas as pd
from PIL import Image
from PIL.ExifTags import TAGS
import csv_manip
import sys
import os
import df_manip 
import filetype
import numpy as np

# change those values to handle other file and folders
csv_path = '../metaDataCsv/csvtest.csv'
folder_path = '../images/images/accordion/'

# get the resolution of the image
def get_resolution(df, image_path):
    typee = filetype.guess(image_path)
    df['type/mime'] = str(typee.extension + typee.mime)

# Get the size of the image
def get_size(df, image_path):
    i = Image.open(image_path)
    statinfo = os.stat(image_path)
    df["st_size"] = str(statinfo.st_size)
    df["size"] = str(i.size)

# get the type of the image
def get_type(df, image_path):
    with open(image_path, "rb") as f:
        data = f.read()
    if data[0:2] != b"\xff\xd8":
        return
    if data[2:4] != b"\xff\xe0":
        return
    else:
        if data[13] == b"\x00":
            unit = "no unit"
        elif data[13] == b"\x01":
            unit = "dpi"
        elif data[13] == b"\x02":
            unit = "dpcm"
        else:
            return
        x = 256 * ord(data[14]) + ord(data[15])
        y = 256 * ord(data[16]) + ord(data[17])
        df["resolution"] = str((x, y))
        df["unit"] = str(unit)

    from iptcinfo3 import IPTCInfo
    info = IPTCInfo(path)

# Get the exif meta data from exifread library
def get_exif_tags(image_path, csv_path, df):
    img = open(image_path, 'rb')
    tags = {}
    tags = exifread.process_file(img)
    df_manip.add_dict_to_df(df, tags)
    df.to_csv(csv_path, index= False)
    return df

# get the exif meta data from PIL image library
def get_exif_data(image_path, csv_path, df):
    ret = {}
    i = Image.open(image_path)
    info = i._getexif()
    if (info):
        for tag, value in info.items():
            decoded = TAGS.get(tag, tag)
            ret[decoded] = value
        df_manip.add_dict_to_df(df, ret)

# Get a random state of scam or not
def get_random_state(df):
    choice = np.random.choice([True, False])
    df["state"] = str(choice)

if __name__ == "__main__":
    csv ={}
    l =  []
    csv['df'] = pd.DataFrame()
    print("Getting meta Data...")
    for image in os.listdir(folder_path):
        csv['df'] = pd.DataFrame()
        image_path = folder_path + image
        # open the csv file
        csv = csv_manip.open_csv(csv_path, image_path, csv)
        # get the different data
        csv['df'] = get_exif_tags(image_path, csv_path, csv['df'])
        get_exif_data(image_path, csv_path, csv['df'])
        get_resolution(csv["df"], image_path)
        get_size(csv["df"], image_path)
        ee = pd.read_csv
        l.append(csv["df"])
        get_random_state(csv["df"])
    # Manage and write the data
    print("Managing Data Frame...")
    new_df = pd.concat(l, sort=True)
    print("Writing in csv file...")
    csv_manip.write_in_csv(csv['csv_file'], new_df)
    print("The program ended well.")