import cv2
import cv2.aruco as aruco

# Global variables
ref_length_cm = 5.0  # ArUco marker real-world size in cm
clicked_point = None
measure_done = False

# Mouse callback function to set clicked point
def mouse_callback(event, x, y, flags, param):
    global clicked_point, measure_done
    if event == cv2.EVENT_LBUTTONDOWN:
        clicked_point = (x, y)
        measure_done = Fagilse  # reset if re-click

def detect_marker_and_get_scale(frame, marker_length_cm=ref_length_cm):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)
    parameters = aruco.DetectorParameters()
    detector = aruco.ArucoDetector(aruco_dict, parameters)
    corners, ids, _ = detector.detectMarkers(gray)
    if ids is not None and len(corners) > 0:
        corner = corners[0][0]
        pixel_length = cv2.norm(corner[0], corner[1])
        cm_per_pixel = marker_length_cm / pixel_length
        return cm_per_pixel
    return None

def get_roi_size(frame, center, size=100):
    x, y = center
    h, w = frame.shape[:2]
    x1 = max(x - size // 2, 0)
    y1 = max(y - size // 2, 0)
    x2 = min(x + size // 2, w)
    y2 = min(y + size // 2, h)
    roi = frame[y1:y2, x1:x2]
    return roi, (x1, y1, x2, y2)

def main():
    global clicked_point, measure_done
    cap = cv2.VideoCapture(0)
    cv2.namedWindow("Measure")
    cv2.setMouseCallback("Measure", mouse_callback)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        cm_per_pixel = detect_marker_and_get_scale(frame)
        display = frame.copy()

        if clicked_point and cm_per_pixel and not measure_done:
            roi, (x1, y1, x2, y2) = get_roi_size(frame, clicked_point)

            # Convert to grayscale and threshold to isolate the object
            gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
            _, thresh = cv2.threshold(gray_roi, 50, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

            contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            if contours:
                largest = max(contours, key=cv2.contourArea)
                rect = cv2.boundingRect(largest)
                px_w, px_h = rect[2], rect[3]
                cm_w = round(px_w * cm_per_pixel, 2)
                cm_h = round(px_h * cm_per_pixel, 2)

                cv2.rectangle(display, (x1+rect[0], y1+rect[1]), (x1+rect[0]+px_w, y1+rect[1]+px_h), (0, 255, 0), 2)
                cv2.putText(display, f"W: {cm_w} cm, H: {cm_h} cm", (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 255), 2)
                measure_done = True

        if clicked_point:
            cv2.circle(display, clicked_point, 5, (255, 255, 0), -1)

        cv2.imshow("Measure", display)
        if cv2.waitKey(1) & 0xFF == 27:  # Press ESC to exit
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

