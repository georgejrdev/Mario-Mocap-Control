import cv2
import mediapipe as mp


def start_screen(video_path:str|int, video_size:tuple=(640, 480)):

    video = cv2.VideoCapture(video_path)

    pose = mp.solutions.pose
    mp_pose = pose.Pose(min_tracking_confidence=0.5, min_detection_confidence=0.5)
    mp_draw = mp.solutions.drawing_utils

    _, image = video.read()

    image = cv2.resize(image, (video_size[0], video_size[1]))
    video_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    results = mp_pose.process(video_rgb)
    points = results.pose_landmarks

    mp_draw.draw_landmarks(image, points, pose.POSE_CONNECTIONS)


    return {
        "image": image,
        "points": points,
        "pose":pose
    }


def drawn_init_points_on_screen(image,positions,width,height):

    cv2.line(image, (0, positions["nose_y"]), (width, positions["nose_y"]), (0, 255, 0), 1)
    cv2.line(image, (positions["right_elbow_x"], 0), (positions["right_elbow_x"], height), (0, 255, 0), 1)
    cv2.line(image, (positions["left_elbow_x"], 0), (positions["left_elbow_x"], height), (0, 255, 0), 1)    


def drawn_moviment_positions_points_on_screen(image,width,confirmed_position_jump,confirmed_position_squat):
    cv2.line(image, (0, confirmed_position_jump), (width, confirmed_position_jump), (0, 0, 255), 1)
    cv2.line(image, (0,confirmed_position_squat), (width,confirmed_position_squat), (0, 0, 255), 1)