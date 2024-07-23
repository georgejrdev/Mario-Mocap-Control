def get_positions(pose,points,width:int,height:int):

    right_index_y = int(points.landmark[pose.PoseLandmark.RIGHT_INDEX].y * height)
    right_index_x = int(points.landmark[pose.PoseLandmark.RIGHT_INDEX].x * width)
    right_shoulder_y = int(points.landmark[pose.PoseLandmark.RIGHT_SHOULDER].y * height)
    right_shoulder_x = int(points.landmark[pose.PoseLandmark.RIGHT_SHOULDER].x * width)
    right_elbow_x = int(points.landmark[pose.PoseLandmark.RIGHT_ELBOW].x * width)
    right_elbow_y = int(points.landmark[pose.PoseLandmark.RIGHT_ELBOW].y * height)
    left_elbow_x = int(points.landmark[pose.PoseLandmark.LEFT_ELBOW].x * width)
    left_elbow_y = int(points.landmark[pose.PoseLandmark.LEFT_ELBOW].y * height)
    left_index_y = int(points.landmark[pose.PoseLandmark.LEFT_INDEX].y * height)
    left_index_x = int(points.landmark[pose.PoseLandmark.LEFT_INDEX].x * width)
    left_shoulder_y = int(points.landmark[pose.PoseLandmark.LEFT_SHOULDER].y * height)
    left_shoulder_x = int(points.landmark[pose.PoseLandmark.LEFT_SHOULDER].x * width)
    nose_y = int(points.landmark[pose.PoseLandmark.NOSE].y * height)
    nose_x = int(points.landmark[pose.PoseLandmark.NOSE].x * width)
    right_eye_x = int(points.landmark[pose.PoseLandmark.RIGHT_EYE].x * width)
    right_eye_y = int(points.landmark[pose.PoseLandmark.RIGHT_EYE].y * height)
    left_hip_x = int(points.landmark[pose.PoseLandmark.LEFT_HIP].x * width)
    left_hip_y = int(points.landmark[pose.PoseLandmark.LEFT_HIP].y * height)
    right_hip_x = int(points.landmark[pose.PoseLandmark.RIGHT_HIP].x * width)
    right_hip_y = int(points.landmark[pose.PoseLandmark.RIGHT_HIP].y * height)


    return {
        "right_index_y":right_index_y,
        "right_index_x":right_index_x,
        "right_shoulder_y":right_shoulder_y,
        "right_shoulder_x":right_shoulder_x,
        "right_elbow_x":right_elbow_x,
        "right_elbow_y":right_elbow_y,
        "left_elbow_x":left_elbow_x,
        "left_elbow_y":left_elbow_y,
        "left_index_y":left_index_y,
        "left_index_x":left_index_x,
        "left_shoulder_y":left_shoulder_y,
        "left_shoulder_x":left_shoulder_x,
        "nose_y":nose_y,
        "nose_x":nose_x,
        "right_eye_x":right_eye_x,
        "right_eye_y":right_eye_y,
        "left_hip_x":left_hip_x,
        "left_hip_y":left_hip_y,
        "right_hip_x":right_hip_x,
        "right_hip_y":right_hip_y
    }