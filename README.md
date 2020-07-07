# DjangoApplication

## How to use Django in Virtual Machine

(eclipse workspace folder에서) python -m venv $your-virtualmachine-name

cd $your-virtualmachine-name

activate //가상머신 활성화

(workspace folder에서)pip install django==1.8

django-admin startproject $your-testfolder-name

cd $your-testfolder-name

manage.py migrate //위 폴더를 쓰겠다

manage.py createsuperuser //master의 아이디랑 비밀번호 입력

manage.py runserver //이렇게 하면 서버가 돌아감

## How to use subApp in Virtual Machine

manage.py startapp $your-subapp-name //이후 eclipse 새로고침

### CAUTION
#### - powershell에서는 activate가 안먹힘. 어떻게 고쳐야하는지 모름. 일단 cmd 쓰자
#### - eclipse, python, jdk download 전제
#### - 한글입력 방법(Eclipse) : window-preferences-general-workspace-text file encoding to utf-8

## test0413/test0413/url.py

from $your-testfolder-name import views

url(r'^$your-url-name/', include(admin.site.urls)), //이 때 127.0.0.1:8000/$your-url-name 으로 접근해야.

url(r'^$your-url-name/', $your-file.$your-function-name), //등으로 고칠 수 있음($your-file, $your-function 만들기 전제)


## --------------------------------------------------------------------------

## (20200707 추가) How to use django project in Pycharm + MySQL workbench

- 1. setting에서 virtual interpreter 설정

- 2. run configuration에서 manage.py 선택하고 runserver 설정
