"""
Selenium 크롤링 파이프라인 설정 파일
Q3: 이 파일을 완성하세요.
"""

# 크롤링할 웹 사이트 URL
# Q3-1: 어떤 웹 사이트를 크롤링할까요?
# 
# 🎯 안전한 크롤링 사이트 추천 (저작권 및 보안 문제 없음):
# 1. "https://quotes.toscrape.com/js/" - JavaScript로 로드되는 명언 사이트 (추천!)
# 2. "https://books.toscrape.com" - 크롤링 연습용 서점 사이트
# 3. "https://the-internet.herokuapp.com" - 다양한 웹 요소 테스트 사이트
# 4. "https://scrapethis.site/" - 크롤링 연습용 사이트
#
# 예시: "https://quotes.toscrape.com/js/"
TARGET_URL = "https://quotes.toscrape.com/js/"

# 사용할 브라우저
# Q3-2: 어떤 브라우저를 사용할까요?
# 옵션: "chrome", "firefox", "edge"
BROWSER = "chrome"

# 헤드리스 모드 (백그라운드 실행)
# Q3-3: 헤드리스 모드로 실행할까요?
# True: 브라우저 창을 띄우지 않음 (서버 환경에 적합)
# False: 브라우저 창을 띄움 (디버깅에 유용)
HEADLESS = False

# 데이터 저장 경로
# Q3-4: 크롤링한 데이터를 어디에 저장할까요?
SAVE_PATH = "data"

# 암시적 대기 시간 (초)
# Q3-5: 요소를 찾을 때까지 몇 초를 기다릴까요?
# 페이지 로드 후 요소가 나타날 때까지 자동으로 대기
IMPLICIT_WAIT = 10

# 명시적 대기 시간 (초)
# 요소가 나타날 때까지 최대 대기 시간
EXPLICIT_WAIT = 20

# 페이지 로드 타임아웃 (초)
PAGE_LOAD_TIMEOUT = 30

# 저장 파일 형식
# Q3-6: 데이터를 어떤 형식으로 저장할까요? ("json", "csv", "txt")
SAVE_FORMAT = "json"

# 로그 파일 경로
LOG_FILE = "data/selenium_crawler.log"

# Chrome 옵션 (선택사항)
# Q3-7: Chrome 브라우저에 추가 옵션을 설정할까요?
# 예: 사용자 에이전트, 창 크기, 언어 설정 등
CHROME_OPTIONS = [
    "--no-sandbox",
    "--disable-dev-shm-usage",
    # "--window-size=1920,1080",  # 창 크기 설정
    # "--lang=ko-KR",  # 언어 설정
]
