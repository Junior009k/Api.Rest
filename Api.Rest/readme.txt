C:/Users/Junior/AppData/Local/Programs/Python/Python310/python.exe  -m pip install django version=2.2.3   
 django-admin start-proyect miPrimerProject 
 C:/Users/Junior/AppData/Local/Programs/Python/Python310/python.exe  -m pip install requests       
django-admin startproject api       
C:/Users/Junior/AppData/Local/Programs/Python/Python310/python.exe  -m pip install  mysqlclient pymysql 
& C:/Users/Junior/AppData/Local/Programs/Python/Python310/python.exe  manage.py makemigration 
 & C:/Users/Junior/AppData/Local/Programs/Python/Python310/python.exe  manage.py createsuperuser  
 "C:\Users\Junior\AppData\Local\Programs\Python\Python310\Scripts\django-admin.exe" startapp API     
& C:/Users/Junior/AppData/Local/Programs/Python/Python310/python.exe  manage.py migrate                            
 & C:/Users/Junior/AppData/Local/Programs/Python/Python310/python.exe  manage.py runserver  192.168.0.146:80                                                                                                                        
               
crear requerimientos
C:/Users/Junior/AppData/Local/Programs/Python/Python310/python.exe  -m pip freeze > requirements.txt  
C:/Users/Junior/AppData/Local/Programs/Python/Python310/python.exe  -m pip install -r requirements.txt


OPCIONAL
 virtualenv -p python3 env 