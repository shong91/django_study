#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'firstdjango.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

# 웹앱 생성>python manage.py startapp first(webapp name)
# 서버 실행>python manage.py runserver
# 마이그레이션>python manage.py makemigrations
# model.py 의 모델 클래스들을 database 엔진에 맞는 형태로 코드를 정해주기 위한 마이그레이션. => \0001_initial.py 생성
# 마이그레이트>python manage.py migrate (database 생성 완료)