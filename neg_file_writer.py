import os
import cv2

txt = open("pos.txt", "w+")
files = os.listdir("neg")
for file in files:
    if os.path.isfile("neg/" + file):
        txt.writelines("neg/" + file + "\n")