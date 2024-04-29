import os
import cv2
Directory_for_data = './data'
if not os.path.exists(Directory_for_data):
    os.makedirs(Directory_for_data)

cap = cv2.VideoCapture(0)
for j in range(27):
    #26 alphabets and spacebar
    #if chr(65+j) < "Z": continue
    if not os.path.exists(os.path.join(Directory_for_data, chr(65+j))):
        os.makedirs(os.path.join(Directory_for_data, chr(65+j)))

    print(f'Letter {chr(65+j)}')

    while True:
        ret, frame = cap.read()
        cv2.putText(frame, 'Press "F" to capture:)', (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 128, 128), 2,
                    cv2.LINE_AA)
        cv2.imshow('frame', frame)
        if cv2.waitKey(25) == ord('f'):
            break

    counter = 0
    while counter < 85:
        ret, frame = cap.read()
        cv2.imshow('frame', frame)
        cv2.waitKey(25)
        cv2.imwrite(os.path.join(Directory_for_data, chr(65+j), f'{counter}.jpg'), frame)

        counter += 1

cap.release()
cv2.destroyAllWindows()
