## subapp 만드는 방법

# 서브앱 생성
manage.py startapp $phonebook

manage.py runserver

Project Explorer 에서 F5 키 누르면 $phonebook 서브앱 생성됨

template folder에 $PBOOK 폴더 만들어주기


# 모델 만들기
메인앱/urls.py에서 url(r'^phonebook/', include(, name = "")) 해주기

서브앱/urls.py(참고)

서브앱/views.py(참고)

서브앱/models.py(참고) 이용하여 model 만들기



# 모델 등록
메인앱/settings.py에서 INSTALLED_APPS=()에 마지막에 '$phonebook' 이라고 써주기

manage.py makemigrations $phonebook

manage.py migrate $phonebook

manage.py runserver

서브앱/migrations 에 커서 두고 F5 누르면 migrate된 모델 나옴

 
# admin페이지에 모델이 안보여요
$phonebook/admin.py(참고)

  -> 이 때, class phonebookview에서 list_display라는 변수 이름 그대로!
