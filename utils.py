"""
유틸리티 함수 모음
Q4: 이 파일의 함수들을 완성하세요.
"""

import os
import time
import logging
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import config

# webdriver-manager 사용 시 (권장)
try:
    from webdriver_manager.chrome import ChromeDriverManager
    from webdriver_manager.firefox import GeckoDriverManager
    from webdriver_manager.microsoft import EdgeChromiumDriverManager
    WEBDRIVER_MANAGER_AVAILABLE = True
except ImportError:
    WEBDRIVER_MANAGER_AVAILABLE = False


def setup_logging(log_file="data/selenium_crawler.log", level=logging.INFO):
    """
    로깅 설정 함수
    Q4-1: 로깅을 어떻게 설정해야 할까요?
    
    힌트:
    - logging.basicConfig()를 사용합니다
    - 파일과 콘솔에 모두 로그를 출력하도록 설정하세요
    - 포맷: 시간, 레벨, 메시지
    """
    # TODO: 로깅 설정 코드 작성
    # 힌트: 
    # - ensure_directory()로 로그 파일 디렉토리 생성
    # - logging.basicConfig()로 기본 설정
    # - FileHandler와 StreamHandler 추가
    pass


def ensure_directory(directory_path):
    """
    디렉토리가 없으면 생성하는 함수
    Q4-2: 디렉토리를 안전하게 생성하려면?
    
    힌트:
    - os.path.exists() 또는 Path.exists() 사용
    - os.makedirs() 또는 Path.mkdir() 사용
    - exist_ok=True 옵션 고려
    """
    # TODO: 디렉토리 생성 코드 작성
    pass


def create_webdriver(browser_type="chrome", headless=False, options_list=None):
    """
    WebDriver를 생성하는 함수
    Q4-3: WebDriver를 어떻게 초기화할까요?
    
    질문:
    - 어떤 브라우저를 사용할까요? (chrome, firefox, edge)
    - 헤드리스 모드를 어떻게 설정할까요?
    - webdriver-manager를 사용할까요, 아니면 수동 경로를 지정할까요?
    
    반환값: WebDriver 인스턴스
    """
    # TODO: WebDriver 생성 코드 작성
    # 힌트:
    # if browser_type == "chrome":
    #     options = ChromeOptions()
    #     if headless:
    #         options.add_argument("--headless")
    #     # webdriver-manager 사용 또는 수동 경로 지정
    #     driver = webdriver.Chrome(service=..., options=options)
    pass


def wait_for_element(driver, by, value, timeout=10):
    """
    요소가 나타날 때까지 대기하는 함수 (선택사항)
    Q4-4: 명시적 대기(Explicit Wait)는 어떻게 구현할까요?
    
    질문:
    - WebDriverWait를 어떻게 사용할까요?
    - expected_conditions는 어떤 것을 사용할까요?
    
    반환값: WebElement 또는 None
    """
    # TODO: 명시적 대기 구현
    # 힌트:
    # wait = WebDriverWait(driver, timeout)
    # element = wait.until(EC.presence_of_element_located((by, value)))
    pass


def format_timestamp():
    """
    현재 시간을 문자열로 반환하는 함수 (선택사항)
    파일명에 타임스탬프를 추가할 때 사용
    """
    # TODO: 타임스탬프 포맷팅 (예: "2024-01-01_12-00-00")
    pass
