## 프로젝트 구성을 위한 설정
```shell
# 원하는 버전의 파이썬 가상환경을 실행시킵니다.
pyenv activate py3.10

poetry new django_test_schema
cd django_test_schema; poetry update package
```

```shell
poetry add django
poetry add djangorestframework
poetry add pytest-django
```

### 프로젝트의 기본 골격

```shell
pyproject.toml
mysite/
- apps/
- projects/
- tests/
  - products/
    - test_apis.py
- manage.py
- pytest.ini
```
- apps에는 도메인으로 사용할 앱들을 추가하게 됩니다.
- project에는 프로젝트를 실행하기 위한 설정값들을 설정합니다. (settings.py, wsgi.py, asgi.py 등)
- mysite를 work directory로 생각하고, `poetry run pytest`를 통해 테스트를 수행할 수 있습니다. (`test_*.py` 항목에 대해 테스트를 수행하며, 도메인별로 테스트를 생성하는 방식으로 구성합니다.)

#### pytest 관련 설정
```shell
# pytest.ini
[pytest]
DJANGO_SETTINGS_MODULE = project.settings
```
- pytest는 django에서 테스트를 실행할 때, 프로젝트의 setting 값을 사용합니다.