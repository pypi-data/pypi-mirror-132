import cv2
import mediapipe as mp
import time


class FaceDetector:
    def __init__(self, minDetectionCon=0.5):
        self.minDetectionCon = minDetectionCon
        self.mp_face_detection = mp.solutions.face_detection
        self.mp_drawing = mp.solutions.drawing_utils
        self.face_detection = self.mp_face_detection.FaceDetection(self.minDetectionCon)

    def findFaces(self, img, drawRect=True, showPercentage=True, textColor=(255, 0, 255)):
        """
        Finds faces to detect in a BGR image or from a webcam.
        :param img: Image to find the faces to detect.
        :param drawRect: Flag to draw the Rectangle around Faces.
        :param showPercentage: Flag to show the accuracy percentage.
        :param textColor: Color of the percentage's text to display.
        :return: Image with or without drawings and bounding box info.
        """
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.face_detection.process(imgRGB)
        bboxs = []

        if self.results.detections:
            for detection in self.results.detections:
                bboxC = detection.location_data.relative_bounding_box
                ih, iw, ic = img.shape
                bbox = int(bboxC.xmin * iw), int(bboxC.ymin * ih), int(bboxC.width * iw), int(bboxC.height * ih)
                bboxs.append([bbox, detection.score])
                if drawRect:
                    img = self.fancyDraw(img, bbox)
                if showPercentage:
                    cv2.putText(img, f' {int(detection.score[0] * 100)} %',
                                (bbox[0], bbox[1] - 20), cv2.FONT_HERSHEY_PLAIN, 2, textColor, 2)
        return img, bboxs

    def fancyDraw(self, img, bbox, l=30, t=3, rt=1):
        x, y, w, h = bbox
        x1, y1 = x + w, y + h
        cv2.rectangle(img, bbox, (255, 255, 255), rt)
        # Top left x,y
        cv2.line(img, (x, y), (x + l, y), (255, 0, 255), t)
        cv2.line(img, (x, y), (x, y + l), (255, 0, 255), t)

        # Top right x1,y
        cv2.line(img, (x1, y), (x1 - l, y), (255, 0, 255), t)
        cv2.line(img, (x1, y), (x1, y + l), (255, 0, 255), t)

        # Bottom left x,y1
        cv2.line(img, (x, y1), (x + l, y1), (255, 0, 255), t)
        cv2.line(img, (x, y1), (x, y1 - l), (255, 0, 255), t)

        # Bottom Right x1,y1
        cv2.line(img, (x1, y1), (x1 - l, y1), (255, 0, 255), t)
        cv2.line(img, (x1, y1), (x1, y1 - l), (255, 0, 255), t)

        return img


def main():
    cap = cv2.VideoCapture(0)
    pTime = 0
    detector = FaceDetector(minDetectionCon=0.85)
    while True:
        success, img = cap.read()
        img = cv2.cv2.flip(img, 1)
        img, bboxs = detector.findFaces(img, showPercentage=False)
        print(bboxs)
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, f'FPS: {int(fps)}', (20, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)
        cv2.imshow('Image', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


if __name__ == "__main__":
    main()
