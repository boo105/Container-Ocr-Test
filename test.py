import os
import cv2
from recognize import ocr
reader = ocr.Reader()
from multiprocessing import freeze_support

def test_all() :
    test_images = "D:/hackathon/hackathon/"

    for image in os.listdir(test_images):
        if image.find(".jpg") != -1 :
            result1 = reader.readtext(test_images + image)
            print(result1)
            frame = cv2.imread(test_images + image)
            for box in result1:
                cordinates = box[0]
                cv2.putText(frame, box[1], (int(cordinates[0][0]), int(cordinates[0][1])-15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2, cv2.LINE_AA)
                for i, point in enumerate(cordinates):
                    frame = cv2.line(frame, (int(cordinates[i-1][0]), int(cordinates[i-1][1])),(int(point[0]), int(point[1])), (255,0,0), 2)
            cv2.imshow("frame", frame)
            print(80*"*")
            if cv2.waitKey(0) == ord('q'):
                cv2.destroyAllWindows()
                break

def test_only_one() :
    directory = "D:/hackathon/hackathon/"
    #directory = "C:/Users/user/Desktop/test/"

    # 세로
    # image_name = "IMG_CON_GATE_FRONT_B_20210727132256_707374.jpg"
    #image_name = "KakaoTalk_20211223_161008402.jpg"
    # 가로
    image_name = "IMG_CON_CRANE_SIDE_A_20210421014725_721066.jpg"

    result1 = reader.readtext(directory + image_name)
    print(result1)

    frame = cv2.imread(directory + image_name)
    for box in result1:
        cordinates = box[0]
        cv2.putText(frame, box[1], (int(cordinates[0][0]), int(cordinates[0][1])-15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2, cv2.LINE_AA)
        for i, point in enumerate(cordinates):
            frame = cv2.line(frame, (int(cordinates[i-1][0]), int(cordinates[i-1][1])),(int(point[0]), int(point[1])), (255,0,0), 2)
    cv2.imshow("frame", frame)
    print(80*"*")
    if cv2.waitKey(0) == ord('q'):
        cv2.destroyAllWindows()    

if __name__ == "__main__" :
    freeze_support()
    test_only_one()
    # test_all()
