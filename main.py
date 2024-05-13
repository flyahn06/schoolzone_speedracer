from ultralytics import YOLO
import glob
import cv2

files = glob.glob("./resource/trim/*.mov")
target_id = {
    "ahndonggi": 1,
    "choijemo": 1,
    "jooyunjae": 4,
    "kimyosap": 2,
    "leesungryeol": 1,
    "shinjunghoon": 1,
    "shinwoojin": 3,
    "multi": 0
}

for file in files:
    model = YOLO("./model/yolov8n.pt")
    cap = cv2.VideoCapture(file)
    person_name = file.split("/")[-1].split(".")[0]
    f = open(f"./result/{person_name}.csv", 'w')

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        results = model.track(frame, persist=True,
                              device="mps",
                              conf=0.5,
                              classes=[0]
                              )

        frame = results[0].plot(line_width=3)

        for box in results[0].boxes:
            if box.id[0] == target_id[person_name]:
                x, y, w, h = box.xywh[0]
                print(f"{person_name} id {target_id[person_name]} -> x={x}, y={y}, h={h}")
                f.write(f"{x},{y},{h}")
                f.write("\n")

        cv2.imshow("YOLOv8n - Object Tracking :: {} id {}".format(person_name, target_id[person_name]), frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            f.close()
            break

    f.close()
    cv2.destroyAllWindows()
