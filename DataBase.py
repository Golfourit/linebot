#======這裡是匯入資料庫=====
#import firebase_admin 
from firebase import firebase
students = [{"no":1 , "name":"李天龍"},
{"no":2 , "name":"高藝人"},
{"no":3 , "name":"宏大同"},   
{"no":4 , "name":"哈哈哈"}        
]
url = "https://eggrollbase.firebaseio.com/"
fb = firebase.FirebaseApplication(url, None)

for student in students:
    fb.post("/students", student)
    print("{} 儲存完畢".format(student))
#======這裡是匯入資料庫=====
