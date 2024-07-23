import math


def get_distances(positions):
    print("")
    print(positions)
    print("")
    distance_right_hand_shoulder = int(
        math.hypot(positions["right_index_x"] - positions["right_shoulder_x"], positions["right_index_y"] - positions["right_shoulder_y"]))

    distance_left_hand_shoulder= int(
        math.hypot(positions["left_index_x"]-positions["left_shoulder_x"], positions["left_index_y"]-positions["left_shoulder_y"]))
    
    distance_between_hands = int(
        math.hypot(positions["right_index_x"]-positions["left_index_x"], positions["right_index_y"]-positions["left_index_y"]))

    distance_head_ceiling = int(
        math.hypot(positions["right_eye_y"],0))

    distance_hands_nose = int(
        math.hypot(positions["right_index_x"]-positions["nose_x"], positions["right_index_y"]-positions["nose_y"]))

    distance_right_hand_waist = int(
        math.hypot(positions["right_index_x"]-positions["right_hip_x"], positions["right_index_y"]-positions["right_hip_y"]))
    
    distance_left_hand_waist = int(
        math.hypot(positions["left_index_x"]-positions["left_hip_x"], positions["left_index_y"]-positions["left_hip_y"]))
    

    return {
        "distance_right_hand_shoulder":distance_right_hand_shoulder,
        "distance_left_hand_shoulder":distance_left_hand_shoulder,
        "distance_between_hands":distance_between_hands,
        "distance_head_ceiling":distance_head_ceiling,
        "distance_hands_nose":distance_hands_nose,
        "distance_right_hand_waist":distance_right_hand_waist,
        "distance_left_hand_waist":distance_left_hand_waist
    }