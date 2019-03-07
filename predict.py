import glob
#import cv2   
import json
import matplotlib.pyplot as plt
import seaborn as sns
import base64
import time
import os
import ssl
try:
    import httplib  # Python 2
except:
    import http.client as httplib  # Python 3

headers = {"Content-type": "application/json",
           "X-Access-Token": "tKgRsKVPa7RSxXHHw1TyoSqKpYPi21VrTjFb"}
conn = httplib.HTTPSConnection("dev.sighthoundapi.com", 
       context=ssl.SSLContext(ssl.PROTOCOL_TLSv1))

# To use a hosted image uncomment the following line and update the URL
#image_data = "http://example.com/path/to/hosted/image.jpg"

# To use a local file uncomment the following line and update the path
neutral = []
sadness = []
disgust = []
anger = []
surprise = []
fear = []
happiness = []
dummy_box = []





for filename in glob.glob("*.jpg"):
    image_data = base64.b64encode(open(filename, "rb").read()).decode()
    params = json.dumps({"image": image_data})
    conn.request("POST", "/v1/detections?type=face,person&faceOption=landmark,all", params, headers)
    response = conn.getresponse()
    result = response.read()
    
  
    result = json.loads(result) 

    #print("Detection Results = " + str(result))

   
    with open('faceemotion.json', 'w') as f:
        json.dump(result, f)

#Getting the data

   
    data = open('faceemotion.json', 'r').read()  

    #data = data.split('{', 1)[-1]    
    #data = data.rsplit('}', 1)[0]     
    #data = ''.join(['{', data, '}'])  
    
    jsonObj = json.loads(data)

    faces_list = []
    for i in list(range(0, len(jsonObj['objects']))):
        try:
            points = jsonObj['objects'][i]['attributes']['emotionsAll']
            faces_list.append(points)
        except:
            continue
 
            



    for points in faces_list:    

        key_max = max(points.keys(), key=(lambda k: points[k]))
        print(key_max)
        max_val  = points[key_max]
    
        if key_max == 'neutral':
            if max_val > 0.94:
                neutral.append(max_val)
            else:
                dummy_box.append(max_val)
        elif key_max == 'sadness':
            sadness.append(max_val)
        elif key_max == 'disgust':
            disgust.append(max_val)
        elif key_max == 'anger':
            anger.append(max_val)
        elif key_max == 'surprise':
            surprise.append(max_val)
        elif key_max == 'fear':
            fear.append(max_val)
        elif key_max == 'happiness':
            happiness.append(max_val)
        else :
            print('None')
    
        key_2max = max(points.keys(), key=(lambda k: points[k]))
        del points[key_2max]
        key_2max = max(points.keys(), key=(lambda k: points[k]))
        print(key_2max)
        max_2val  = points[key_2max]
        
        if key_2max == 'neutral':
            if max_2val < 0.80:
                dummy_box.append(max_2val)
        elif key_2max == 'sadness':
            #if max_2val > 0.05:
            sadness.append(max_2val)
        elif key_2max == 'disgust':
            #if max_2val > 0.05:
            disgust.append(max_2val)
        elif key_2max == 'anger':
            #if max_2val > 0.05:
            anger.append(max_2val)
        elif key_2max == 'surprise':
            #if max_2val > 0.05:
            surprise.append(max_2val)
        elif key_2max == 'fear':
            #if max_2val > 0.05:
            fear.append(max_2val)
        elif key_2max == 'happiness':
            #if max_2val > 0.05:
            happiness.append(max_2val)
        else :
            print('None')

print(neutral)
print(sadness)
print(disgust) 
print(anger) 
print(surprise) 
print(fear) 
print(happiness) 


neutral_faces = len(neutral)
sadness_faces = len(sadness)
disgust_faces = len(disgust)
anger_faces = len(anger)
surprise_faces = len(surprise)
fear_faces = len(fear)
happiness_faces = len(happiness)


print("Number of Faces: " )
total_faces = neutral_faces + sadness_faces + disgust_faces + anger_faces + surprise_faces + fear_faces + happiness_faces
#total_faces = total_faces - 7
print(total_faces)



neutral_sum = sum(neutral)
sadness_sum = sum(sadness)
disgust_sum = sum(disgust)
anger_sum = sum(anger)
surprise_sum = sum(surprise)
fear_sum = sum(fear)
happiness_sum = sum(happiness)

if len(neutral) > 0:
    neutral_avg = neutral_sum / total_faces
else :
    neutral_avg = 0
if len(sadness) > 0:
    sadness_avg = sadness_sum / total_faces
else :
    sadness_avg = 0    
if len(disgust) > 0:
    disgust_avg = disgust_sum / total_faces
else:
    disgust_avg = 0
if len(anger) > 0:
    anger_avg = anger_sum / total_faces
else :
    anger_avg = 0
if len(surprise) > 0:
    surprise_avg = surprise_sum / total_faces
else :
    surprise_avg = 0
if len(fear) > 0:
    fear_avg = fear_sum / total_faces
else :
    fear_avg = 0
if len(happiness) > 0:
    happiness_avg = happiness_sum / total_faces
else :
    happiness_avg = 0


print("Average Neutral Faces : ",neutral_avg)
print("Average Sadness Faces : ",sadness_avg)
print("Average Disgust Faces : ",disgust_avg)
print("Average Anger Faces : ",anger_avg)
print("Average Surprise Faces : ",surprise_avg)
print("Average Fear Faces : ",fear_avg)
print("Average Happiness Faces : ",happiness_avg)






#graph


emotions = [neutral_avg,sadness_avg,disgust_avg,anger_avg,surprise_avg,fear_avg,happiness_avg]
labels = ['Neutral','Sadness','Disgust','Anger','Surprise','Fear','Happiness']
plt.pie(emotions,labels = labels,shadow=True, startangle=140,autopct='%1.1f%%')
plt.axis('equal')
date_string = time.strftime("%Y-%m-%d")
plt.savefig(date_string+'.png')

#delete all pictures (.jpg)

for file in os.listdir('../data'):
    if file.endswith('.jpg'):
        os.remove(file)


