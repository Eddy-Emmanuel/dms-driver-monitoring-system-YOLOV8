import cv2
import supervision as sv
from ultralytics import YOLO
from supervision import BoxAnnotator

model = YOLO("best.pt")
box_annotator = BoxAnnotator(text_thickness=1)

def main():
    cam = cv2.VideoCapture(0)
    while cam.isOpened():
        success, frame = cam.read()
        if success:
            predictions = model(frame)[0]
            detections = sv.Detections.from_ultralytics(predictions)
            labels = [f"{model.model.names[class_id]}--{confidence:.2f}" for class_id, confidence in zip(detections.class_id, detections.confidence)]
            annotated_frame = box_annotator.annotate(scene=frame, detections=detections, labels=labels)

            cv2.imshow("Detection", annotated_frame)

            if cv2.waitKey(1) == ord("q"):
                break

        else:
            raise("Can't Open Camera")
    
    cam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()