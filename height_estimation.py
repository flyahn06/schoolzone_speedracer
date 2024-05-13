from ultralytics import YOLO
import glob
import cv2

files = glob.glob("./resource/trim/*.mov")
height1 = lambda y_coord, h: 190.446644-0.03590398*y_coord+0.01524424*h
# height2 = lambda x_coord, y_coord, h: 204.8226661-0.009074452*x_coord-0.041186334*y_coord+0.009549047*h

for file in files:
    model = YOLO("./model/yolov8n.pt")
    cap = cv2.VideoCapture(file)
    person_name = file.split("/")[-1].split(".")[0]

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        results = model.track(
            frame, persist=True,
            device="mps",
            conf=0.5,
            classes=[0]
        )[0]

        # print(results)

        for point in results.boxes:
            x1, y1, x2, y2 = map(int, point.xyxy[0])
            # print(x, y, w, h)

            cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 3)
            cv2.putText(
                frame,
                "{0:.1f}".format(height1(float(point.xywh[0][1]), float(point.xywh[0][3]))),
                (x1, y1-20),
                cv2.FONT_HERSHEY_DUPLEX,
                0.5,
                (255, 255, 255),
                1
            )

        cv2.imshow("YOLOv8n - Object Tracking :: {}".format(person_name), frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()
