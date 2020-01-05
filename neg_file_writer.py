import os
import cv2

txt = open("neg.txt", "w+")
files = os.listdir("b")
for file in files:
    if os.path.isfile("bg/" + file):
        txt.writelines("bg/" + file + "\n")
