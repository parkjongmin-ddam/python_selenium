# 🚀 시작하기

## 🤖 Selenium이란?

**Selenium**은 웹 브라우저를 자동으로 제어하는 도구입니다.
- 실제 브라우저를 실행하여 웹 페이지와 상호작용
- JavaScript로 동적으로 생성되는 콘텐츠도 크롤링 가능
- 클릭, 입력, 스크롤 등 사용자 행동 시뮬레이션
- **중요**: BeautifulSoup4보다 느리고 무겁지만, 동적 페이지에 필수!

자세한 내용은 README.md의 "Selenium이란?" 섹션을 참고하세요.

---

## 첫 번째 단계

1. **패키지 설치**
   ```bash
   pip install -r requirements.txt
   ```

   ### 📦 pip 라이브러리 확인 명령어
   
   패키지 설치 후 확인하거나 관리할 때 유용한 명령어들입니다:
   
   | 명령어 | 설명 | 예시 |
   |--------|------|------|
   | `pip list` | 설치된 모든 패키지 목록 보기 | `pip list` |
   | `pip show 패키지명` | 특정 패키지 상세 정보 확인 | `pip show selenium` |
   | `pip freeze` | requirements.txt 형식으로 출력 | `pip freeze` |
   | `pip freeze > requirements.txt` | 현재 패키지 목록을 파일로 저장 | `pip freeze > requirements.txt` |
   | `pip list \| findstr 패키지명` | 특정 패키지 검색 (Windows) | `pip list \| findstr selenium` |
   | `pip list \| grep 패키지명` | 특정 패키지 검색 (Linux/Mac) | `pip list \| grep selenium` |
   
   **자주 사용하는 명령어:**
   - `pip list` - 전체 패키지 목록 확인
   - `pip show 패키지명` - 특정 패키지 정보 확인
   - `pip list \| findstr 패키지명` - 패키지 설치 여부 빠르게 확인

2. **WebDriver 설치**
   
   Selenium을 사용하려면 브라우저별 WebDriver가 필요합니다:
   
   **방법 1: webdriver-manager 사용 (권장)**
   ```bash
   pip install webdriver-manager
   ```
   코드에서 자동으로 WebDriver를 다운로드하고 관리합니다.
   
   **방법 2: 수동 설치**
   - Chrome: https://chromedriver.chromium.org/downloads
   - Firefox: https://github.com/mozilla/geckodriver/releases
   - Edge: https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/

3. **프로젝트 구조 이해**
   - `config.py` - 설정 파일
   - `utils.py` - 유틸리티 함수
   - `scraper.py` - Selenium 크롤링 로직
   - `pipeline.py` - 데이터 처리 및 저장
   - `main.py` - 실행 파일

4. **학습 순서**
   - README.md의 Q1부터 Q7까지 순서대로 진행
   - 각 질문에 답하면서 코드 작성
   - 막히면 힌트를 참고하세요

5. **안전한 크롤링 사이트 선택**
   - **추천**: `https://quotes.toscrape.com/js/` (JavaScript 버전)
   - 다른 추천 사이트는 README.md의 Q3 섹션 참고

## 빠른 시작 체크리스트

### Step 1: config.py 완성
- [ ] TARGET_URL 설정 (추천: "https://quotes.toscrape.com/js/")
- [ ] BROWSER 설정 ("chrome", "firefox", "edge")
- [ ] HEADLESS 설정 (True/False)
- [ ] SAVE_PATH 설정
- [ ] IMPLICIT_WAIT 설정
- [ ] SAVE_FORMAT 설정

### Step 2: utils.py 완성
- [ ] setup_logging() 함수
- [ ] ensure_directory() 함수
- [ ] create_webdriver() 함수
- [ ] wait_for_element() 함수 (선택사항)

### Step 3: scraper.py 완성
- [ ] __init__() 메서드
- [ ] navigate_to() 메서드
- [ ] find_elements() 메서드
- [ ] extract_data() 메서드
- [ ] close() 메서드
- [ ] scrape() 메서드

### Step 4: pipeline.py 완성
- [ ] __init__() 메서드
- [ ] clean_data() 메서드
- [ ] save_to_json() 메서드
- [ ] save_data() 메서드
- [ ] run() 메서드

### Step 5: main.py 완성
- [ ] import 문
- [ ] 로깅 설정
- [ ] main() 함수
- [ ] 브라우저 종료 처리 (try-finally)

## 디버깅 팁

1. **로깅 활용**: 각 단계에서 로그를 출력하여 진행 상황 확인
2. **작은 단위 테스트**: 각 함수를 개별적으로 테스트
3. **브라우저 시각화**: HEADLESS=False로 설정하여 브라우저 동작 확인
4. **대기 시간 조정**: 요소가 로드되지 않으면 대기 시간을 늘려보세요
5. **에러 메시지 확인**: Python의 에러 메시지를 자세히 읽어보세요
6. **웹사이트 구조 확인**: 브라우저 개발자 도구(F12)로 HTML 구조 파악

## 도움이 필요할 때

1. Selenium 문서: https://www.selenium.dev/documentation/
2. Selenium Python 바인딩: https://selenium-python.readthedocs.io/
3. WebDriver Manager: https://github.com/SergeyPirogov/webdriver_manager
4. Python 공식 문서: https://docs.python.org/3/

**화이팅! 💪**
