import os
import cv2
import pickle
import mediapipe as mp

media_pipe_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

hands = media_pipe_hands.Hands(static_image_mode=True, min_detection_confidence=0.5)
#0.5 is atleast 50 % confident

directory_of_data = "C:/Users/HP/Desktop/asl_alphabet_train/asl_alphabet_train/"
directory_of_data = 'data/'
data = []
labels = []

for folder in os.listdir(directory_of_data):
    if folder == "Test":
        #Test is a dataset from kaggle
        #Ignored it to create my own dataset
        continue
    print(folder)
    count = 0
    for img_path in os.listdir(os.path.join(directory_of_data, folder)):
        count += 1      
        auxiliary_data_points = []
        x_axis = []
        y_axis = []

        img = cv2.imread(os.path.join(directory_of_data, folder, img_path))
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        #print(,len(data))
        results = hands.process(img_rgb)
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                for i in range(len(hand_landmarks.landmark)):
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y
                    x_axis.append(x)
                    y_axis.append(y)
                for i in range(len(hand_landmarks.landmark)):
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y
                    auxiliary_data_points.append(x - min(x_axis))
                    auxiliary_data_points.append(y - min(y_axis))
            #print("final",folder)
            data.append(auxiliary_data_points)
            labels.append(folder)
            print(img_path,len(x_axis),len(y_axis))
            
    print(count)
f = open('data.pickle', 'wb')
pickle.dump({'data': data, 'labels': labels}, f)
f.close()
