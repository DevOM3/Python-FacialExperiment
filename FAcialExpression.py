from fer import FER
import cv2

detector = FER()

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    emotions = detector.detect_emotions(frame)

    if len(emotions) >= 1:
        top_emotions = [
            max(e["emotions"], key=lambda key:e["emotions"][key]) for e in emotions
        ]

        top_emotion = top_emotions[0]
        score = emotions[0]["emotions"][top_emotion]

        cv2.rectangle(frame, detector.find_faces(frame)[0], (0, 255, 0), 1)
        font = cv2.FONT_HERSHEY_PLAIN
        if detector.find_faces(frame).__len__() >= 1:
            pos = detector.find_faces(frame)[0]
            cv2.putText(frame, top_emotion, (pos[0], pos[1] + pos[2] + 21),
                        font, 1, (0, 0, 0), 1)

    cv2.imshow("Frame", frame)
    cv2.waitKey(5)

cap.release()
cv2.destroyAllWindows()
