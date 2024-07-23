from .keypress import *
from .screen import *


MID_ADJUST = 60
LOW_ADJUST = 30
MID_HIGH_ADJUST = 40
HIGH_ADJUST = 50
MAX_ADJUST = 14
LOWER_BOUND = 50
UPPER_BOUND = 76
UPPER_MID_BOUND = 130
JUMP_THRESHOLD = 40

confirmed_position_jump = 0
confirmed_position_squat = 0
is_jumping = False
is_squatting = False
key_pressed = False

def jump(image, width, positions, distances):

    global confirmed_position_jump, confirmed_position_squat
    global is_jumping, key_pressed, is_squatting

    right_eye_y = positions['right_eye_y']
    right_shoulder_y = positions['right_shoulder_y']
    nose_y = positions['nose_y']

    distance_head_ceiling = distances['distance_head_ceiling']
    distance_head_nose = distances['distance_hands_nose']

    if distance_head_ceiling >= UPPER_BOUND and distance_head_ceiling <= UPPER_MID_BOUND:
        adjustment = LOW_ADJUST

    elif distance_head_ceiling > UPPER_MID_BOUND:
        adjustment = MAX_ADJUST

    elif LOWER_BOUND < distance_head_ceiling < UPPER_BOUND:
        adjustment = MID_HIGH_ADJUST

    elif distance_head_ceiling <= LOWER_BOUND:
        adjustment = HIGH_ADJUST

    else:
        adjustment = MID_ADJUST 

    if distance_head_nose < JUMP_THRESHOLD:
        confirmed_position_jump = int(right_eye_y * (1 - adjustment / 100))
        confirmed_position_squat = int(right_shoulder_y*(1-0/100))
        print("Posição do pulo alterada")

    drawn_moviment_positions_points_on_screen(image, width, confirmed_position_jump, confirmed_position_squat)

    if confirmed_position_jump and nose_y < confirmed_position_jump:
        if not is_jumping:
            press_key_in_background('c', 'press')
            is_jumping = True
    else:
        is_jumping = False

    if nose_y > confirmed_position_squat:
        if not is_squatting:
            press_key_in_background('down', 'keydown')
            is_squatting = True
            key_pressed = True
    else:
        if key_pressed:
            press_key_in_background('down', 'keyup')
            key_pressed = False
        is_squatting = False