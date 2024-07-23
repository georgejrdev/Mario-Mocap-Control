from .keypress import *


key_right_pressed = False             
key_left_pressed = False     

def walk_forward(postitions,distances):

    global key_right_pressed

    right_index_x = postitions['right_index_x']
    right_index_y = postitions['right_index_y']
    right_elbow_x = postitions['right_elbow_x']
    right_hip_y = postitions['right_hip_y']

    distance_right_hand_waist = distances['distance_right_hand_waist']
    distance_between_hands = distances['distance_between_hands']

    if ((not distance_right_hand_waist > 60) or (not distance_between_hands > 100) or (not right_index_y < (right_hip_y-30))):
        if key_right_pressed:
            press_key_in_background('x', 'keyup')
            press_key_in_background('right', 'keyup')
            key_right_pressed = False

    if key_right_pressed is False:
        press_key_in_background('right', 'keydown')
        key_right_pressed = True

    if (right_index_x < right_elbow_x):
        press_key_in_background('x', 'keydown')      
    else:
        press_key_in_background('x', 'keyup')
    

def walk_backward(postitions,distances):

    global key_left_pressed

    left_index_x = postitions['left_index_x']
    left_index_y = postitions['left_index_y']
    left_elbow_x = postitions['left_elbow_x']
    left_hip_y = postitions['left_hip_y']

    distance_left_hand_waist = distances['distance_left_hand_waist']
    distance_between_hands = distances['distance_between_hands']

    if ((not distance_left_hand_waist > 60) or (not distance_between_hands > 100) or (not left_index_y < (left_hip_y-30))):
        if key_left_pressed:
            press_key_in_background('x', 'keyup')
            press_key_in_background('left', 'keyup')
            key_left_pressed = False

    if key_left_pressed is False:
        press_key_in_background('left', 'keydown')
        key_left_pressed = True

    if (left_index_x > left_elbow_x):
        press_key_in_background('x', 'keydown')      
    else:
        press_key_in_background('x', 'keyup')