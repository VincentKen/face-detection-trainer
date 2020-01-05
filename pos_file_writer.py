import os
import cv2
import shutil

txt = open("pos.txt", "w+")

if not os.path.exists('pos'):
        os.makedirs('pos')
else:
    folder = 'pos/'
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

label = 0
prefix = "images/"
directories = os.listdir(prefix)
for dir in directories:
    if not os.path.isdir(prefix + dir):
        pass
    for f in os.listdir(prefix+dir):
        file = os.path.join(prefix+dir, f)
        if not os.path.isfile(file):
            pass
        cv2.imwrite('pos/' + str(label) + '.jpg', (cv2.resize(cv2.imread(file, 0), (100, 100))))
        files = os.listdir("neg")

        txt.writelines("pos/" + str(label) + ".jpg\n")
        label+=1

