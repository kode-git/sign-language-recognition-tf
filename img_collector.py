import os
import time
import uuid
import cv2
import string

# image path to collect images
IMAGES_PATH = "./workspace/images/collection/"

# loading of 26 letters from the ascii_lowercase
# we don't have any distinguish between lower cases and upper cases
labels = list(string.ascii_lowercase)
number_images = 13

for label in labels:
    if os.path.exists(IMAGES_PATH + label):
        # if the directory exists, we remove it and his content
        os.system("rm -rf " + IMAGES_PATH + label)
    # and we can create new one now
    os.mkdir(IMAGES_PATH + label)

    # cv2 changing depending on Operating System, check it on documentation if this line give you an error
    cap = cv2.VideoCapture(0)
    print('Collecting images for {}'.format(label))
    time.sleep(5)
    for img_num in range(number_images):
        print('Collecting image {}'.format(img_num))
        ret, frame = cap.read()
        img_name = os.path.join(IMAGES_PATH, label, label + '.' + '{}.jpg'.format(str(uuid.uuid1())))
        cv2.imwrite(img_name, frame)
        cv2.imshow('frame', frame)
        time.sleep(2)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
