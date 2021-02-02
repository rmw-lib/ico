#!/usr/bin/env python3

import traceback
from skimage import io
from os.path import isfile, getsize
import cv2
import os
import datetime
import numpy as np
from pexpect import run


def autocrop(img):
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  _,flatImage = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)
  threshold = 0
  rows = np.where(
    np.max(flatImage,
           0) > threshold
  )[0]
  if rows.size:
    cols = np.where(
      np.max(flatImage,
             1) > threshold
    )[0]
    img = img[cols[0]:cols[-1] + 1,
              rows[0]:rows[-1] + 1]
  else:
    img = img[:1, :1]

  return img


def change_size(read_file):
  image = io.imread(
    read_file,
  )  # 读取图片 image_name应该是变量
  image = autocrop(image)
  return image


def main(n):

  source_path = f"./in/{n}/"  # 图片来源路径
  save_path = f"./out/{n}/"  # 图片修改后的保存路径

  if not os.path.exists(save_path):
    os.mkdir(save_path)

  file_names = os.listdir(source_path)

  starttime = datetime.datetime.now()
  for i in range(len(file_names)):
    fname = file_names[i]
    print(i, "裁剪：", fname)
    outname = file_names[i].replace("jpg", "png")
    outfile = save_path + outname
    avif = outfile[:-3] + "avif"
    if isfile(avif):
      if getsize(avif):
        continue
    try:
      x = change_size(
        source_path + fname
      )  # 得到文件名
      io.imsave(outfile, x)
      cmd = f"/root/.yarn/bin/coffee ./png2avif.coffee {outfile}"
      run(cmd)
    except Exception as err:
      traceback.print_exc()

    # while (i == 2600):
    #   break
  print("裁剪完毕")
  endtime = datetime.datetime.now()  # 记录结束时间
  endtime = (endtime - starttime).seconds
  print("裁剪总用时", endtime)


for i in sorted(os.listdir("./in")):
  print(f">> {i}")
  main(i)
