import cv2
import os

image_folder = 'images'
if not os.path.exists(image_folder):
    os.makedirs(image_folder)

image_count = 0


def save_and_exit(key, cap, image_count, image_folder):
    if key == ord('s'):
        cv2.imwrite(f'{image_folder}/img{image_count}.png', cap.read()[1])
        print("Image saved!")
        image_count += 1


cap = cv2.VideoCapture(2)

while cap.isOpened():
    success, img = cap.read()

    key = cv2.waitKey(5)

    save_and_exit(key, cap, image_count, image_folder)

    if key == 27:  # Escape Key
        break

    cv2.imshow('Img', img)

cap.release()
cv2.destroyAllWindows()
