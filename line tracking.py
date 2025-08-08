import cv2
import numpy as np

def region_of_interest(image):
    height = image.shape[0]
    polygons = np.array([
        [(0, height), (image.shape[1], height), (image.shape[1], int(height * 0.6)), (0, int(height * 0.6))]
    ])
    mask = np.zeros_like(image)
    cv2.fillPoly(mask, polygons, 255)
    return cv2.bitwise_and(image, mask)

def detect_edges(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blur, 100, 200)
    return edges

def draw_filtered_lines(image, lines):
    line_image = np.zeros_like(image)
    if lines is not None:
        height, width = image.shape[:2]
        for line in lines:
            x1, y1, x2, y2 = line[0]
            slope = (y2 - y1) / (x2 - x1 + 1e-6)

            if abs(slope) < 0.4:
                continue

            if x1 < width / 2 and x2 < width / 2:
                color = (0, 255, 255)    # يسار - أصفر
            elif x1 > width / 2 and x2 > width / 2:
                color = (255, 204, 153)  # يمين - سماوي فاتح
            else:
                color = (255, 255, 255)  # وسط - أبيض

            cv2.line(line_image, (x1, y1), (x2, y2), color, 2, cv2.LINE_AA)
    return line_image

def process_frame(frame):
    edges = detect_edges(frame)
    cropped_edges = region_of_interest(edges)

    lines = cv2.HoughLinesP(
        cropped_edges,
        rho=1,
        theta=np.pi / 180,
        threshold=70,
        minLineLength=50,
        maxLineGap=150
    )

    line_image = draw_filtered_lines(frame, lines)
    result = cv2.addWeighted(frame, 0.8, line_image, 1, 1)
    return result

def process_video(video_path):
    cap = cv2.VideoCapture(video_path)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        final_frame = process_frame(frame)
        cv2.imshow("Lane Detection", final_frame)

        if cv2.waitKey(25) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


process_video("road.mp4")