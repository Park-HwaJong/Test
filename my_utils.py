###Version 1.2

import os
import cv2
import numpy as np 

VERSION = 1.2

ERASE_LINE = '\x1b[2K' # erase line command

SPLIT_LINE = '#------------------------------------------------------------------------------------------------------------------------------------'

 
def __version__():
    print('my_utils version : ', VERSION)
    return VERSION

def PatchNote():
    print('added my_log class')
    print('removed create_folder')

def BGRtoRGB(imgs):
    imgs = imgs[...,::-1]
    return imgs

def load_images_in_folder(fpath, bgr2rgb=False, img_size=None, return_name=False):
    imgs = []
    names = []
    print('image loading ...')
    for root, dirs, files in os.walk(fpath):
        for fname in files:
            full_fname = os.path.join(root, fname)
            if full_fname[-3:] != 'png' and full_fname[-3:] != 'jpg':
                continue
            names.append(fname)
            img = cv2.imread(full_fname)
            if img_size != None:
                img = cv2.resize(img, dsize=img_size)
            imgs.append(img)
    imgs = np.array(imgs)
    if bgr2rgb:
        imgs = BGRtoRGB(imgs)
    print('image load success!')
 
    if return_name:
        return imgs, names 
    return imgs

 class my_log():
    def __init__(self, path):
        self.path = path

    def set_path(self, path):
        self.path = path

 
    def logging(self, context, log_only=False):
        if not os.path.exists(self.path):
            f = open(self.path, 'w')
        else:
            f = open(self.path, 'a')
 
        if isinstance(context, list):
            for data in context:
                f.write(str(data)+'\n')
                if not log_only:
                    print(data)
        elif isinstance(context, str):
            f.write(context+'\n')
            if not log_only:
                print(context)   
        f.close()

 
    def show(self, apply_split=False):
        if not os.path.exists(self.path):
            print('not exist file!! - path : %s' %self.path)
            return None

        else:
            f = open(self.path, 'r')
            text = []
            while True:
                line = f.readline()
                if not line: break
                line = line.strip()
                if apply_split:
                    line = line.split()
                print(line)
                text.append(line)
            f.close()

            return text

 
########################## removed ##################################

"""
def create_folder(path):
    if not os.path.exists(path):
        os.mkdir(path)


def save_text_file(path, context_list, mode='w'):
    #mode [r, w, a] r:read w:write a:add
    assert mode == 'r' or 'w' or 'a'
    f = open(path, mode)
    for data in context_list:
        f.write(str(data)+'\n')
    #print(path + ' file saved !!!')
    f.close()
 
"""
