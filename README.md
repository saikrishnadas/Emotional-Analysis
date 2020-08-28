# README 

# EMOTION DETECTION 

# NOTE
If need of the code, 
mail me : saikrishnadas666@gmail.com
or
https://www.fiverr.com/share/Kwevvk

## INTRODUCTION 

Live prediction of emotion on a person or many for a period and returning a visualization chart.



## Requirements:

 - TENSORFLOW
 - KERAS
 - OPENCV
 - PYTHON (3.6)- PANDAS , NUMPY , MATPLOTLIB , TIME , JSON ,GLOB, OS, SSL, BASE64
 - TASK SCHEDULER OR SYSTEM SCHEDULER 
 - CAMERA
 
## Installation :
**Tensorflow :**

    pip install tensorflow
**Keras :**

    pip install keras
**Opencv :**

    pip install opencv-python
**PANDAS , NUMPY , MATPLOTLIB , TIME , JSON ,GLOB, OS, SSL, BASE64 :**

    pip install pandas
    pip install numpy
    pip install matplolib
    pip install time
    pip install json
    pip install glob
    pip install os
    pip install ssl
    pip install base64

 






## DESCRIPTION AND USAGE :

This project captures images of people for a period i.e shutters picture each 10 minutes for 6 hours. These pictures are fed into predict.py script and SightHound API is called into these images which return json format. The json format is stored into a file and retrieved later. At last, a pie chart is created for the total captured emotions.  

# FILE DESCRIPTION :

## img_cap.py:
This script is used to capture images. Opencv is used to capture images `cv2.VideoCapture(0)` is used to capture images through webcams that are in-build . `cv2.VideoCapture(1)` is used to capture images through external cameras.
Capture set is defined to a frame size of **640x480** . A image counter is initialized to capture the images till the limit is reached. A start clock take the time module to find the current system time `start_time = time.time()` . The image is captured as a GrayScaled image for better dark-side determination `cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)` . If the key '**q**' is  pressed that triggers the break of the script and exits the frame manually. The `time.time()` is defined `>=` 300 seconds i.e 5 minutes, which would capture images each 5 minutes. The image is stored  into the same folder where the script is and each name of the image will be "**FaceFrame{}.jpg**" .
The image is stored in **.jpg** because at last it is easy to delete images after the pie chart is generated. The is stored back to color image for better human readability. The script runs for  21600 seconds i.e 6 hours totally each day `time.clock() - start_clock > 21600` this breaks the script after 6 hours.
  

##  predict script :

The predict script predicts the emotion on each image captured and returns a total average of the each emotion onto a pir chart. The prediction is done by calling SightHound API on each image which in turn returns a json format as the output.
This code is used to call the API :
	X-Access-Token can be generate by SightHound account : 
	https://www.sighthound.com/account/#/account/login

     import http.client as httplib 
    headers = {"Content-type": "application/json",
               "X-Access-Token": "YOUR-ACCESS-TOKEN"}
    conn = httplib.HTTPSConnection("dev.sighthoundapi.com", 
           context=ssl.SSLContext(ssl.PROTOCOL_TLSv1))  

API is called on each image 

    for filename in glob.glob("*.jpg") : 
    base64.b64encode(open(filename,"rb").read()).decode()
 After the API on each image, the emotion ratio and probability is returned a json format as output.
 Then these JSON format is stored into a file so that it is each to retrieve dictionary **key:value** .
A empty array is initialized for all the 6 emotions . At each time the emotion is found on images it returns probability of emotions which is then stores the probability into each emotion's array .
The "neutral" emotion only stored the value if it is greater that 0.79 because for each image the API returns multiple emotions, so to overcome the bias towards neutral emotion. 

    if max_val > 0.79

For the second emotion, it only stores the value of emotion if it is greater than 0.10 ,

     if max_2val > 0.10
This script prints the emotions on each image and find the length of the array of each image 

    neutral_faces =  len(neutral)
Number of total faces are found by,

    total_faces = neutral_faces + sadness_faces + disgust_faces + anger_faces 
    + surprise_faces + fear_faces + happiness_faces
    print(total_faces)
At finally each Emotional average is found for total images and a pie chart is plotted .

    
    emotions =[neutral_avg,sadness_avg,disgust_avg,anger_avg,surprise_avg,fear_avg,happiness_avg]
    labels = ['Neutral','Sadness','Disgust','Anger','Surprise','Fear','Happiness']
    plt.pie(emotions,labels = labels,shadow=True, startangle=140,autopct='%1.1f%%')
    plt.axis('equal')
    date_string = time.strftime("%Y-%m-%d")
    plt.savefig(date_string+'.png')
The image is stored by current date name and in .png format.

At last all the captured images of people are deleted for making better storage capacity.

    for file in os.listdir('../Final Project'):
        if file.endswith('.jpg'):
            os.remove(file)
**NOTE**: do not store the chart generated to .jpg format which will cause delectation of the image . It is recommended not the change the format from .png to .jpg .


 




## .py to .exe :

img_cap.py and predict script are both converted into .exe files(img_cap.exe and predict.exe) for automation of script by **System Scheduler**.
Converting .py to .exe : 

    pyinstaller -F img_cap.py
    pyinstaller -F predict.py
**NOTE :** *pyinstaller* must be installed for this convert. 

    pip install pyinstaller

 
## System Scheduler :

System Scheduler is used to automate the .exe files( files generated by pyinstaller).
The time to activate files : 
			**img_cap.exe - 10 am Each day excluding Weekends.
			predict.exe - 4:30 pm Each day excluding Weekends.**







