# Selenium 웹 자동화 및 크롤링 학습 프로젝트

## 📚 프로젝트 소개

이 프로젝트는 Selenium을 이용한 웹 자동화 및 크롤링 파이프라인을 단계별로 학습할 수 있도록 구성되었습니다.
**Q&A 형식**으로 진행하며, 각 질문에 답하면서 코드를 완성해나갑니다.

### 학습 주제
**동적 웹 페이지 크롤링 파이프라인** - JavaScript로 동적으로 로드되는 웹 페이지에서 데이터를 수집하고 저장하는 시스템

---

## 🤖 Selenium이란?

### 개념
**Selenium**은 웹 브라우저를 자동으로 제어하는 도구입니다. 
실제 브라우저를 실행하여 웹 페이지와 상호작용할 수 있게 해주며, JavaScript로 동적으로 생성되는 콘텐츠도 크롤링할 수 있습니다.

### Selenium의 동작 과정
1. **브라우저 실행**: WebDriver를 통해 실제 브라우저(Chrome, Firefox 등) 실행
2. **페이지 로드**: URL로 이동하여 페이지 로드 대기
3. **요소 찾기**: CSS 선택자, XPath 등으로 웹 요소 찾기
4. **상호작용**: 클릭, 입력, 스크롤 등 사용자 행동 시뮬레이션
5. **데이터 추출**: 로드된 콘텐츠에서 데이터 추출
6. **브라우저 종료**: 작업 완료 후 브라우저 닫기

### Selenium의 활용 분야
- **동적 웹 크롤링**: JavaScript로 로드되는 콘텐츠 수집
- **웹 테스팅**: 자동화된 웹 애플리케이션 테스트
- **웹 자동화**: 반복적인 웹 작업 자동화
- **E2E 테스트**: 사용자 시나리오 기반 테스트
- **데이터 수집**: SPA(Single Page Application) 데이터 수집

### Selenium vs BeautifulSoup4
| 도구 | 사용 시기 | 장점 | 단점 |
|------|----------|------|------|
| **BeautifulSoup4** | 정적 HTML 페이지 | 빠름, 가벼움, 간단함 | JavaScript 실행 불가 |
| **Selenium** | 동적 페이지, JavaScript 필요 | 실제 브라우저 제어, 상호작용 가능 | 느림, 무거움, 리소스 사용 많음 |

**결론**: JavaScript로 동적으로 콘텐츠가 로드되는 사이트는 Selenium이 필요합니다!

### Selenium 구성 요소
1. **Selenium WebDriver**: 브라우저를 제어하는 API
2. **WebDriver**: 각 브라우저별 드라이버 (ChromeDriver, GeckoDriver 등)
3. **Selenium Grid**: 여러 브라우저에서 병렬 실행
4. **Selenium IDE**: 브라우저 확장 프로그램 (녹화/재생)

---

## 🎯 학습 목표

1. Selenium WebDriver 기본 사용법 이해
2. 동적 웹 페이지 크롤링 파이프라인 설계
3. 대기 전략(Wait Strategy) 이해 및 적용
4. 코드 모듈화 및 재사용성 향상
5. 에러 처리 및 로깅 구현
6. 데이터 저장 및 관리

---

## 📋 사전 준비사항

### Q1: 필요한 패키지들을 설치하기 위해 `requirements.txt` 파일을 만들어야 합니다.
**질문**: Selenium 크롤링에 필요한 주요 패키지들은 무엇일까요?
- 브라우저 자동화: `selenium`
- 데이터 저장: `pandas` (선택사항)
- 로깅: Python 내장 `logging` 모듈 사용

**과제**: `requirements.txt` 파일을 작성하세요.

**⚠️ 중요**: Selenium을 사용하려면 브라우저별 WebDriver가 필요합니다:
- **Chrome**: ChromeDriver (Chrome for Testing 사용 권장)
- **Firefox**: GeckoDriver
- **Edge**: EdgeDriver

---

## 🏗️ 아키텍처 설계

### Q2: 크롤링 파이프라인을 어떻게 구성하면 좋을까요?
**질문**: 크롤링 파이프라인은 보통 어떤 단계로 나뉠까요?

**힌트**:
1. **설정 관리** (config.py) - URL, 브라우저 설정, 저장 경로 등
2. **브라우저 제어** (scraper.py) - WebDriver 초기화 및 제어
3. **페이지 탐색** (scraper.py) - URL 이동, 대기, 요소 찾기
4. **데이터 추출** (scraper.py) - 동적 콘텐츠에서 데이터 추출
5. **데이터 처리** (pipeline.py) - 데이터 정제 및 변환
6. **데이터 저장** (pipeline.py) - 파일 또는 DB 저장
7. **에러 처리** (utils.py) - 예외 처리 및 로깅

**과제**: 각 모듈의 역할을 이해하고, 파일 구조를 파악하세요.

---

## 📝 단계별 학습 가이드

### Step 1: 설정 파일 작성 (config.py)

#### Q3: 크롤링에 필요한 설정 정보는 무엇일까요?
**질문**: 
- 크롤링할 웹사이트 URL은?
- 어떤 브라우저를 사용할까요? (Chrome, Firefox, Edge)
- 브라우저를 헤드리스 모드로 실행할까요?
- 데이터를 저장할 경로는?
- 페이지 로드 대기 시간은 얼마나?

**과제**: `config.py` 파일을 완성하세요.

##### 🎯 안전한 크롤링 사이트 추천

크롤링 연습을 위해 **저작권 및 보안 문제가 없는** 안전한 사이트들을 추천합니다:

1. **Quotes to Scrape** (추천 ⭐)
   - URL: `https://quotes.toscrape.com/js/`
   - 특징: JavaScript로 로드되는 명언 사이트
   - 장점: Selenium 연습에 적합, 구조가 단순함
   - 추출 가능: 명언 텍스트, 작가명, 태그

2. **Books to Scrape**
   - URL: `https://books.toscrape.com`
   - 특징: 크롤링 연습용 가상 서점 사이트
   - 장점: 여러 페이지, 다양한 데이터 구조
   - 추출 가능: 책 제목, 가격, 평점, 재고 상태

3. **Selenium Practice Site**
   - URL: `https://the-internet.herokuapp.com`
   - 특징: 다양한 웹 요소 테스트 사이트
   - 장점: 동적 요소, 대기 전략 연습에 적합

4. **JSONPlaceholder** (API 테스트)
   - URL: `https://jsonplaceholder.typicode.com`
   - 특징: REST API 테스트 사이트
   - 장점: API와 Selenium 비교 학습 가능

**⚠️ 주의**: 실제 상업 사이트를 크롤링하기 전에 반드시 `robots.txt`를 확인하고, 서비스 약관을 읽어보세요!

```python
# 예시 구조 (완성하지 말고, 스켈레톤만 참고)
# 추천: Quotes to Scrape JS 버전 사용
TARGET_URL = "https://quotes.toscrape.com/js/"  # 크롤링할 사이트
BROWSER = "..."  # 어떤 브라우저를 사용할까요?
HEADLESS = ...  # 헤드리스 모드로 실행할까요?
SAVE_PATH = "..."  # 어디에 저장할까요?
IMPLICIT_WAIT = ...  # 몇 초로 설정할까요?
```

---

### Step 2: 유틸리티 함수 작성 (utils.py)

#### Q4: 크롤링 시 필요한 유틸리티 함수들은?
**질문**:
1. 로깅을 설정하려면 어떻게 해야 할까요?
2. 파일 경로를 안전하게 생성하려면?
3. WebDriver를 어떻게 초기화할까요?
4. 명시적 대기(Explicit Wait)는 어떻게 구현할까요?

**과제**: `utils.py`에 다음 함수들을 구현하세요:
- `setup_logging()` - 로깅 설정
- `ensure_directory()` - 디렉토리 생성
- `create_webdriver()` - WebDriver 생성
- `wait_for_element()` - 요소가 나타날 때까지 대기

---

### Step 3: 스크래퍼 클래스 작성 (scraper.py)

#### Q5: 스크래퍼 클래스는 어떤 메서드가 필요할까요?
**질문**:
1. WebDriver를 초기화하는 메서드는?
2. 페이지로 이동하는 메서드는?
3. 요소를 찾는 메서드는?
4. 데이터를 추출하는 메서드는?
5. 스크롤은 어떻게 할까요?
6. 에러 처리는 어떻게 할까요?

**과제**: `scraper.py`의 `DynamicWebScraper` 클래스를 완성하세요.

**힌트**:
```python
class DynamicWebScraper:
    def __init__(self, browser_type, headless=False):
        # WebDriver 초기화 코드 작성
    
    def navigate_to(self, url):
        # 페이지로 이동
        # 페이지 로드 대기
    
    def find_elements(self, by, value):
        # 요소 찾기 (CSS 선택자, XPath 등)
    
    def extract_data(self):
        # 동적 콘텐츠에서 데이터 추출
    
    def scroll_page(self):
        # 페이지 스크롤 (필요시)
    
    def close(self):
        # 브라우저 종료
```

---

### Step 4: 파이프라인 작성 (pipeline.py)

#### Q6: 파이프라인은 어떻게 데이터를 처리할까요?
**질문**:
1. 스크래퍼에서 받은 데이터를 어떻게 정제할까요?
2. 데이터를 어떤 형식으로 저장할까요? (JSON, CSV, TXT?)
3. 중복 데이터는 어떻게 처리할까요?

**과제**: `pipeline.py`의 `CrawlingPipeline` 클래스를 완성하세요.

**힌트**:
```python
class CrawlingPipeline:
    def __init__(self, scraper, save_path):
        # 초기화
    
    def clean_data(self, data):
        # 데이터 정제 (공백 제거, 중복 제거 등)
    
    def save_data(self, data, filename):
        # 파일로 저장 (JSON 또는 CSV)
    
    def run(self):
        # 전체 파이프라인 실행
        # 1. 스크래퍼로 데이터 수집
        # 2. 데이터 정제
        # 3. 데이터 저장
```

---

### Step 5: 메인 실행 파일 작성 (main.py)

#### Q7: 메인 파일에서는 무엇을 해야 할까요?
**질문**:
1. 모든 모듈을 어떻게 연결할까요?
2. 에러 처리는 어디서 할까요?
3. 브라우저를 안전하게 종료하려면?
4. 사용자에게 결과를 어떻게 보여줄까요?

**과제**: `main.py`를 완성하여 전체 파이프라인을 실행하세요.

---

## 🚀 실행 방법

각 단계를 완성한 후:

```bash
# 패키지 설치
pip install -r requirements.txt

# ChromeDriver 설치 (Chrome 사용 시)
# 방법 1: webdriver-manager 사용 (권장)
pip install webdriver-manager

# 방법 2: 수동 설치
# https://chromedriver.chromium.org/downloads 에서 다운로드

# 실행
python main.py
```

---

## 💡 추가 학습 과제

### Q8: 파이프라인을 개선하려면?
1. **멀티페이지 크롤링**: 여러 페이지를 순회하며 크롤링
2. **데이터베이스 저장**: SQLite나 MySQL에 저장
3. **스케줄링**: 정기적으로 크롤링 실행
4. **병렬 처리**: 여러 브라우저 인스턴스로 동시 크롤링
5. **스크린샷**: 특정 요소나 페이지 스크린샷 저장
6. **쿠키/세션 관리**: 로그인 필요한 사이트 크롤링

---

## 📖 참고 자료

- [Selenium 공식 문서](https://www.selenium.dev/documentation/)
- [Selenium Python 바인딩](https://selenium-python.readthedocs.io/)
- [WebDriver Manager](https://github.com/SergeyPirogov/webdriver_manager)
- [Python 로깅 가이드](https://docs.python.org/3/howto/logging.html)

---

## ⚠️ 주의사항

1. **로봇 배제 표준(robots.txt) 확인**: 크롤링 전에 웹사이트의 robots.txt를 확인하세요
2. **요청 간격**: 서버에 부하를 주지 않도록 적절한 delay를 설정하세요
3. **저작권**: 크롤링한 데이터의 사용 목적을 확인하세요
4. **에러 처리**: 네트워크 오류, 요소 찾기 실패 등을 적절히 처리하세요
5. **리소스 관리**: 브라우저를 반드시 종료하여 메모리 누수 방지
6. **WebDriver 버전**: 브라우저 버전과 WebDriver 버전이 호환되는지 확인

---

## 🎓 학습 체크리스트

- [ ] Step 1: config.py 완성
- [ ] Step 2: utils.py 완성
- [ ] Step 3: scraper.py 완성
- [ ] Step 4: pipeline.py 완성
- [ ] Step 5: main.py 완성
- [ ] 전체 파이프라인 실행 및 테스트
- [ ] 에러 처리 및 로깅 확인
- [ ] 추가 개선 사항 구현

---

**Happy Automating! 🤖**
