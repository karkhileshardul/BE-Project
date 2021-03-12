import sys
import os, time
import cognitive_face as CF
from global_variables import personGroupId
import urllib
import sqlite3
import cv2
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#BASE_URL = 'https://southeastasia.api.cognitive.microsoft.com/face/v1.0'
#CF.BaseUrl.set(BASE_URL)
#Key = 'a7073ac5c5af4f4d9f6c1a609efc3a56'
#CF.Key.set(Key)


BASE_URL = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0'
CF.BaseUrl.set(BASE_URL)
Key = '2c9ae23bb71242cca1eb17e10322fc6a'
CF.Key.set(Key)

def get_person_id():
	person_id = ''
	extractId = str(sys.argv[1])[-2:]
	connect = sqlite3.connect("Face-DataBase")
	c = connect.cursor()
	cmd = "SELECT * FROM Students WHERE ID = " + extractId
	c.execute(cmd)
	row = c.fetchone()
	person_id = row[3]
	connect.close()
	return person_id

def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        if img is not None:
            images.append(img)
    return images


def detecting_face(imgurl):
	res = CF.face.detect(imgurl)
	if len(res) != 1:
		print "No face detected in image"
	else:
		res = CF.person.add_face(imgurl, personGroupId, person_id)
		print(res)	
	time.sleep(6)

if len(sys.argv) is not 1:
    currentDir = os.path.dirname(os.path.abspath(__file__))
    imageFolder = os.path.join(currentDir, "dataset/" + str(sys.argv[1]))
    person_id = get_person_id()
    for filename in os.listdir(imageFolder):
        if filename.endswith(".jpg"):
#        	print(filename)
#        	imgurl = urllib.pathname2url(os.path.join(imageFolder, filename))
#		detecting_face()
		os.chdir("/home/shardul/BE PROJECT/dataset/"+sys.argv[1])
		i=1
#		while(filename.endswith(".jpg")):
		while(i<=20):
			if(i==1):
				os.chdir("/home/shardul/BE PROJECT/dataset/"+sys.argv[1])
				filename="1.jpg"
				print(filename)
				detecting_face(filename)
			if(i==2):
				os.chdir("/home/shardul/BE PROJECT/dataset/"+sys.argv[1])
				filename="2.jpg"
				print(filename)
				detecting_face(filename)
			if(i==3):
				os.chdir("/home/shardul/BE PROJECT/dataset/"+sys.argv[1])
				filename="3.jpg"
				print(filename)
				detecting_face(filename)			
			if(i==4):
				os.chdir("/home/shardul/BE PROJECT/dataset/"+sys.argv[1])
				filename="4.jpg"
				print(filename)
				detecting_face(filename)
			if(i==5):
				os.chdir("/home/shardul/BE PROJECT/dataset/"+sys.argv[1])
				filename="5.jpg"
				print(filename)
				detecting_face(filename)
			if(i==6):
				os.chdir("/home/shardul/BE PROJECT/dataset/"+sys.argv[1])
				filename="6.jpg"
				print(filename)
				detecting_face(filename)			
			if(i==7):
				os.chdir("/home/shardul/BE PROJECT/dataset/"+sys.argv[1])
				filename="7.jpg"
				print(filename)
				detecting_face(filename)
			if(i==8):
				os.chdir("/home/shardul/BE PROJECT/dataset/"+sys.argv[1])
				filename="8.jpg"
				print(filename)
				detecting_face(filename)
			if(i==9):
				os.chdir("/home/shardul/BE PROJECT/dataset/"+sys.argv[1])
				filename="9.jpg"
				print(filename)
				detecting_face(filename)			
			if(i==10):
				os.chdir("/home/shardul/BE PROJECT/dataset/"+sys.argv[1])
				filename="10.jpg"
				print(filename)
				detecting_face(filename)
			if(i==11):
				os.chdir("/home/shardul/BE PROJECT/dataset/"+sys.argv[1])
				filename="11.jpg"
				print(filename)
				detecting_face(filename)
			if(i==12):
				os.chdir("/home/shardul/BE PROJECT/dataset/"+sys.argv[1])
				filename="12.jpg"
				print(filename)
				detecting_face(filename)			
			if(i==13):
				os.chdir("/home/shardul/BE PROJECT/dataset/"+sys.argv[1])
				filename="13.jpg"
				print(filename)
				detecting_face(filename)
			if(i==14):
				os.chdir("/home/shardul/BE PROJECT/dataset/"+sys.argv[1])
				filename="14.jpg"
				print(filename)
				detecting_face(filename)
			if(i==15):
				os.chdir("/home/shardul/BE PROJECT/dataset/"+sys.argv[1])
				filename="15.jpg"
				print(filename)
				detecting_face(filename)			
				sys.exit(0)			
			i=i+1
'''
			if(i==16):
				os.chdir("/home/shardul/BE PROJECT/dataset/"+sys.argv[1])
				filename="16.jpg"
				print(filename)
				detecting_face(filename)
			if(i==17):
				os.chdir("/home/shardul/BE PROJECT/dataset/"+sys.argv[1])
				filename="17.jpg"
				print(filename)
				detecting_face(filename)
			if(i==18):
				os.chdir("/home/shardul/BE PROJECT/dataset/"+sys.argv[1])
				filename="18.jpg"
				print(filename)
				detecting_face(filename)
			if(i==19):
				os.chdir("/home/shardul/BE PROJECT/dataset/"+sys.argv[1])
				filename="19.jpg"
				print(filename)
				detecting_face(filename)			
			if(i==20):
				os.chdir("/home/shardul/BE PROJECT/dataset/"+sys.argv[1])
				filename="20.jpg"
				print(filename)
				detecting_face(filename)
				sys.exit(0)						

			i=i+1
'''
'''		if len(res) != 1:
			print "No face detected in image"
		else:
			res = CF.person.add_face(imgurl, personGroupId, person_id)
			print(res)	
		time.sleep(6)
'''
		
