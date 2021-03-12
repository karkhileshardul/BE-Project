import sys
import cognitive_face as CF
from global_variables import personGroupId
import sqlite3
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


#BASE_URL = 'https://southeastasia.api.cognitive.microsoft.com/face/v1.0'
#CF.BaseUrl.set(BASE_URL)
#Key = 'a7073ac5c5af4f4d9f6c1a609efc3a56'

BASE_URL = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0'
CF.BaseUrl.set(BASE_URL)
Key = '2c9ae23bb71242cca1eb17e10322fc6a'
CF.Key.set(Key)

if len(sys.argv) is not 1:
    res = CF.person.create(personGroupId,str(sys.argv[1]))
    print(res)
    extractId = str(sys.argv[1])[-2:]
    connect = sqlite3.connect("Face-DataBase")
    cmd = "SELECT * FROM Students WHERE ID = " + extractId
    cursor = connect.execute(cmd)
    isRecordExist = 0
    for row in cursor:                                                          # checking wheather the id exist or not
        isRecordExist = 1
    if isRecordExist == 1:                                                      # updating name and roll no
        connect.execute("UPDATE Students SET personID = ? WHERE ID = ?",(res['personId'], extractId))
    connect.commit()                                                            # commiting into the database
    connect.close()
    print "Person ID successfully added to the database"
