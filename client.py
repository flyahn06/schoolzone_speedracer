# +--------------+--------------+-----------------------------------------------------------------+
# |    Author    |     Date     |                            Changed                              |
# +--------------+--------------+-----------------------------------------------------------------+
# |   flyahn06   |  2023/05/15  | Initial release. Feat: track people using YOLOv8n               |
# +-------------+--------------+------------------------------------------------------------------+
# |   flyahn06   |  2023/05/14  | Feat: record coordinates and heights of bounding boxes          |
# +-------------+--------------+------------------------------------------------------------------+
# |   flyahn06   |  2023/05/14  | Feat: real-time height estimation (height_estimation.py         |
# +-------------+--------------+------------------------------------------------------------------+
# |   flyahn06   |  2023/05/18  | Enhancement: updated regression equation                        |
# +-------------+--------------+------------------------------------------------------------------+
# |   flyahn06   |  2023/05/18  | Feat: implement network communication with server (client.py)   |
# +-------------+--------------+------------------------------------------------------------------+

from ultralytics import YOLO
import socket
import cv2

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.connect(("192.168.0.3", 1234))

# files = glob.glob("./resource/trim/*.mov")
files = ["./resource/trim/multi.mov", "./resource/trim/choijemo.mov", "resource/trim/ahndonggi.mov"]

height1 = lambda y_coord, h: 190.446644-0.03590398*y_coord+0.01524424*h
height2 = lambda x_coord, y_coord, h: 204.8226661-0.009074452*x_coord-0.041186334*y_coord+0.009549047*h
height3 = lambda x_coord, y_coord, h: 195.959868+0.00561793*x_coord-0.0561879*y_coord-0.0074354*h

default = "37\n".encode()
child = "34\n".encode()
children = "33\n".encode()


for file in files:
    model = YOLO("./model/yolov8n.pt")
    cap = cv2.VideoCapture(file)
    person_name = file.split("/")[-1].split(".")[0]

    while True:
        detected_child = 0
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

            if height3(x1, y1, point.xywh[0][2]) < 170:
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)
                cv2.putText(
                    frame,
                    "{0:.1f}".format(height3(x1, y1, point.xywh[0][2])),
                    (x1, y1-20),
                    cv2.FONT_HERSHEY_DUPLEX,
                    2,
                    (255, 255, 255),
                    1
                )
                detected_child += 1
            else:
                cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 3)
                cv2.putText(
                    frame,
                    "{0:.1f}".format(height3(x1, y1, point.xywh[0][2])),
                    (x1, y1-20),
                    cv2.FONT_HERSHEY_DUPLEX,
                    2,
                    (255, 255, 255),
                    1
                )

        cv2.imshow("YOLOv8n - Object Tracking :: {}".format(person_name), frame)

        if detected_child:
            soc.send(child)
        else:
            soc.send(default)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()
