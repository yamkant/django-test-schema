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

### 테스트 수행 과정
1. `conftest.py`에 설정된 `django_db_setup`을 통해 `tests.fixtures`의 json 기반 파일들을 데이터베이스에 미리 설정합니다.
2. 

### pytest를 왜 사용할까?
- pytest를 위한 플러그인들을 사용할 수 있습니다. 
- unittest나 subclass를 사용할 필요 없이 바로 테스트를 진행할 수 있으며, 기존의 unittest 스타일로 테스트를 수행하더라도 호환이 잘됩니다.
- 내장되어있는 장고의 기본 테스트와 달리, function 단위로 테스트를 작성할 수 있습니다.
- 단순한 `assert` 키워드 만으로 테스트를 평가할 수 있습니다.
- config를 파일로 지정할 수 있으며 fixture를 정해놓고 여러 곳에서 원하는 순서에 맞춰 실행시킬 수 있습니다.

### pytest fixture 옵션값 설정
- fixtrue가 어떤 단위로 1회 생성되는지를 정해줍니다.
- `@pytest.fixture(scope="function")`: 함수 단위로 생성됩니다. (기본값입니다.)
- `@pytest.fixture(scope="class")` : 클래스 단위로 생성됩니다.
- `@pytest.fixture(scope="module")` : 파일 단위로 생성됩니다.
- `@pytest.fixture(scope="package")` : 패키지 단위로 생성됩니다.
- `@pytest.fixture(scope="session")` : test session동안  생성됩니다.
- `@pytest.fixture(autouse=True)`로 설정하면, 별도의 요청 없이 모든 테스트에서 해당 fixture를 사용할 수 있게 됩니다.

#### fixture 초기값 설정 설정 방법
- `django_db_setup`: 테스트를 위한 db가 생성될 때 마이그레이션을 적용하며, 테스트 종료 후 이를 제거합니다. (`conftest.py`에 오버라이드해서 사용)
- `django_db_blocker`: db 접근 권한은 기본적으로 막혀있지만, `django_db_blocker`를 사용하면 접근을 허용할 수 있게 됩니다. 
  - `.unblock()`: db 접근을 허용합니다. 
  - `.block()`: db 접근을 허용하지 않습니다.
  - `.restore()`: db blocking 상태 이전으로 db를 복원합니다.

#### pytest 관련 설정
```shell
# pytest.ini
[pytest]
DJANGO_SETTINGS_MODULE = project.settings
```
- pytest는 django에서 테스트를 실행할 때, 프로젝트의 setting 값을 사용합니다.