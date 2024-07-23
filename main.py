import cv2

from src import *

VIDEO_PATH = "video.mp4"
VIDEO_SIZE = (640, 480)

screen = start_screen(VIDEO_PATH, VIDEO_SIZE)
image = screen['image']
points = screen['points']
pose = screen['pose']

while True:

    height, width, _ = image.shape

    if points:

        positions = get_positions(pose,points,width,height)
        distances = get_distances(positions)

        walk_forward(positions,distances)
        walk_backward(positions,distances)

        jump(image,width,postitions,distances)
        
        drawn_init_points_on_screen(image)


    cv2.imshow("Image", image)

    if cv2.waitKey(10) == 27:
        break


press_key_in_background('x', 'keyup')
press_key_in_background('right', 'keyup')
press_key_in_background('left', 'keyup')
press_key_in_background('c', 'keyup')
press_key_in_background('down', 'keyup')