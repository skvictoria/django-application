# DjangoApplication

## Preparation
```
Eclipse
Python
JDK
```

## How to use Django in Virtual Machine

'''
move to eclipse workspace folder
python -m venv $your-virtualmachine-name
cd $your-virtualmachine-name
activate // (Activate your virtual machine)
'''

## Environment Setting
'''
pip install django==1.8
django-admin startproject $your-testfolder-name
cd $your-testfolder-name
manage.py migrate // (I will  use this folder)
manage.py createsuperuser // (put superuser's id and pw)
manage.py runserver // (run server)
'''

## How to use subApp in Virtual Machine
'''
manage.py startapp $your-subapp-name
restart your server
'''

### CAUTION
#### 1. cannot use powershell (cannot use "activate") -> use CMD!
#### 2. How to write Korean in Eclipse? : window-preferences-general-workspace-text file encoding to utf-8


## test0413/test0413/url.py
'''
from $your-testfolder-name import views

url(r'^$your-url-name/', include(admin.site.urls)), //이 때 127.0.0.1:8000/$your-url-name 으로 접근해야.

url(r'^$your-url-name/', $your-file.$your-function-name), //등으로 고칠 수 있음($your-file, $your-function 만들기 전제)
'''

## --------------------------------------------------------------------------

## (20200707 추가) How to use django project in Pycharm + MySQL workbench

- 1. setting에서 virtual interpreter 설정

- 2. run configuration에서 manage.py 선택하고 runserver 설정
