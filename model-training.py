import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np


data_dict = pickle.load(open('./data.pickle', 'rb'))
print(type(data_dict))
"""
print(data_dict['data'][:1])  # Print the first 10 items to check their structure
for i, item in enumerate(data_dict['data']):
    if len(item) != 42:  # Replace `expected_length` with what you expect
        print(f"Item {i} has length {len(item)}")
from numpy import pad

expected_length = max(len(item) for item in data_dict['data'])  # Find max length

# Now pad each item to the expected length
padded_data = [pad(item, (0, expected_length - len(item)), mode='constant') for item in data_dict['data']]
data = np.asarray(padded_data)
print(shape(data))
"""
umap = {}
data = []
labels = []
#n = 0
print(len(data_dict['data']))
for i in range(len(data_dict['data'])):
    c = data_dict['data'][i]
    d = data_dict['labels'][i]
    if d == 'nothing' or d == 'del' or d == 'space' or len(c) != 42: continue
    if d == '[': d = " "
    
    if len(c) != 42:
        continue
    if d not in umap:
            umap[d] = 0
    if  umap[d] < 50:
        data.append(c)
        labels.append(d)
        umap[d] += 1
#        print(d)
print(umap)
print(len(data), len(labels))
data = np.array(data)
labels = np.array(labels)
print(data.shape, labels.shape)
#data = np.asarray(data_dict['data'])
#labels = np.asarray(data_dict['labels'])
#print(len(labels))
#for i in data:
#    print(len(i))

#for i in labels:
#    print(i)
#print(len(data))



x_train, x_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, shuffle=True, stratify=labels)
print(x_train.shape,x_test.shape,y_train.shape,y_test.shape)
model = RandomForestClassifier()

model.fit(x_train, y_train)
print("fit done")
y_predict = model.predict(x_test)
print("line 69")
accuracy = accuracy_score(y_predict, y_test)*100

print(f'{accuracy:.4f}%  classified correctly ')

f = open('model.p', 'wb')
pickle.dump({'model': model}, f)
f.close()
