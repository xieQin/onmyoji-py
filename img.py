import cv2, numpy, time, os, random
from PIL import ImageGrab
import numpy as np
# from matplotlib import pyplot as plt

def locate(target, want, show = 0, msg = 0):
  print("start finding target")
  loc_pos = []
  want, treshold, c_name = want[0], want[1], want[2]
  result = cv2.matchTemplate(target, want, cv2.TM_CCOEFF_NORMED)
  location = numpy.where(result >= treshold)

  if msg:  #显示正式寻找目标名称，调试时开启
    print(c_name,'searching... ')
  
  h, w = want.shape[:-1]

  n,ex,ey=1,0,0
  for pt in zip(*location[::-1]):    #其实这里经常是空的
    x,y=pt[0]+int(w/2),pt[1]+int(h/2)
    if (x-ex)+(y-ey)<15:  #去掉邻近重复的点
      continue
    ex,ey=x,y

    cv2.circle(target,(x,y),10,(0,0,255),3)

    if msg:
      print(c_name,'we find it !!! ,at',x,y)
        
    x,y=int(x),int(y)
    loc_pos.append([x,y])

  if show:  #在图上显示寻找的结果，调试时开启
    cv2.imshow('we get',target)
    cv2.waitKey(0) 
    cv2.destroyAllWindows()

  if len(loc_pos)==0:
    print(c_name,'not find')

  return loc_pos

def cut(screen,upleft,downright): 
  a,b=upleft
  c,d=downright
  screen=screen[b:d,a:c]

  return screen


def load_imgs():
  targets = {}
  path = os.getcwd() + '/imgs'
  file_list = os.listdir(path)

  for file in file_list:
    name = file.split('.')[0]
    file_path = path + '/' + file
    temp = [cv2.imread(file_path), 0.85, name]
    targets[name] = temp
  
  return targets

# imgs = load_imgs()
# # # screen = ImageGrab.grab()
# # # screen.save('screen.png')
# screen = cv2.imread('screen.png')

# want = imgs['close']
# target = screen
# pts = locate(target, want, 0)
# if not pts:
#   print('error')
# else:
#   print('ok')
#   print(pts[0][0], pts[0][1])

# img = cv2.imread('screen.png')
# template = cv2.imread('./imgs/index.png')
# w, h = template.shape[:-1]

# res = cv2.matchTemplate(img, template, cv2.TM_SQDIFF_NORMED)
# min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
# top_left = max_loc
# bottom_right = (top_left[0] + w, top_left[1] + h)
# print(top_left, bottom_right)

# cv2.rectangle(img, top_left, bottom_right, 255, 2)
# plt.subplot(121),plt.imshow(res,cmap = 'gray')
# plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(img,cmap = 'gray')
# plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
# plt.suptitle(cv2.TM_SQDIFF_NORMED)

# plt.show()