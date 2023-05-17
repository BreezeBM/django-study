# django-study

### requirements
- python 3.10
- venv

### scripts for study
- 프로젝트를 생성하는 스크립트
- ```django-admin startproject ***(프로젝트 이름)```


- 앱을 생성하는 스크립트
- ```python manage.py startapp ***(앱 이름)```


- 프로젝트 안에 있는 모든 static 파일을 한 곳으로 모으는 명령어
- ```python manage.py collectstatic```


- models.py에 쓰는 내용을 디비와 연결시킬 py파일로 만드는 명령어 
- ```python manage.py makemigrations```


- 마이그레이션 파일을 만들고 연동하는 명령어
- ```python manage.py migrate```