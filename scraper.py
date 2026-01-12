"""
동적 웹 페이지 스크래퍼 클래스
Q5: 이 클래스를 완성하세요.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import logging
import config
from utils import create_webdriver, wait_for_element


class DynamicWebScraper:
    """
    JavaScript로 동적으로 로드되는 웹 페이지를 크롤링하는 클래스
    """
    
    def __init__(self, browser_type=None, headless=None):
        """
        스크래퍼 초기화
        Q5-1: WebDriver를 어떻게 초기화할까요?
        
        힌트:
        - browser_type: 사용할 브라우저 ("chrome", "firefox", "edge")
        - headless: 헤드리스 모드 여부
        - driver: WebDriver 인스턴스
        - wait: WebDriverWait 인스턴스 (명시적 대기용)
        """
        # TODO: 초기화 코드 작성
        # 힌트: create_webdriver() 사용
        pass
    
    def navigate_to(self, url):
        """
        페이지로 이동하는 메서드
        Q5-2: 페이지로 어떻게 이동할까요?
        
        질문:
        - driver.get()을 어떻게 사용할까요?
        - 페이지 로드 완료를 어떻게 확인할까요?
        - 에러 처리는 어떻게 할까요?
        """
        # TODO: 페이지 이동 코드 작성
        # 힌트: self.driver.get(url)
        pass
    
    def find_elements(self, by, value, wait_time=None):
        """
        요소를 찾는 메서드
        Q5-3: 요소를 어떻게 찾을까요?
        
        질문:
        - CSS 선택자, XPath, ID 등 어떤 방법을 사용할까요?
        - find_elements()와 find_element()의 차이는?
        - 명시적 대기를 어떻게 사용할까요?
        
        반환값: WebElement 리스트
        """
        # TODO: 요소 찾기 코드 작성
        # 힌트: 
        # - self.driver.find_elements(by, value)
        # - WebDriverWait 사용 고려
        pass
    
    def extract_quotes(self):
        """
        명언 데이터를 추출하는 메서드
        Q5-4: 동적 콘텐츠에서 데이터를 어떻게 추출할까요?
        
        질문:
        - quotes.toscrape.com/js/의 HTML 구조는?
        - 각 명언의 텍스트, 작가, 태그를 어떻게 추출할까요?
        - 요소의 텍스트는 어떻게 가져올까요? (.text 속성)
        
        반환값: 명언 데이터 리스트 (딕셔너리 형태)
        """
        # TODO: 데이터 추출 코드 작성
        # 힌트:
        # quotes = self.find_elements(By.CLASS_NAME, "quote")
        # for quote in quotes:
        #     text = quote.find_element(By.CLASS_NAME, "text").text
        #     author = quote.find_element(By.CLASS_NAME, "author").text
        #     tags = [tag.text for tag in quote.find_elements(By.CLASS_NAME, "tag")]
        pass
    
    def scroll_page(self, scroll_pause_time=1):
        """
        페이지를 스크롤하는 메서드 (필요시)
        Q5-5: 페이지를 어떻게 스크롤할까요?
        
        질문:
        - JavaScript를 실행하려면? (driver.execute_script())
        - 스크롤을 얼마나 내릴까요?
        - 스크롤 후 대기 시간은?
        """
        # TODO: 페이지 스크롤 코드 작성 (필요시)
        # 힌트: self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        pass
    
    def scrape(self, url=None):
        """
        전체 크롤링 프로세스를 실행하는 메서드
        Q5-6: 위의 메서드들을 연결하여 전체 프로세스를 구현하세요.
        
        프로세스:
        1. navigate_to()로 페이지 이동
        2. 페이지 로드 대기
        3. extract_quotes()로 데이터 추출
        4. 로깅 및 결과 반환
        
        반환값: 추출한 데이터 리스트
        """
        # TODO: 전체 크롤링 프로세스 구현
        pass
    
    def close(self):
        """
        브라우저를 종료하는 메서드
        Q5-7: 브라우저를 어떻게 안전하게 종료할까요?
        
        질문:
        - driver.quit()과 driver.close()의 차이는?
        - 에러가 발생해도 브라우저를 종료하려면?
        """
        # TODO: 브라우저 종료 코드 작성
        # 힌트: self.driver.quit()
        pass
    
    def __enter__(self):
        """컨텍스트 매니저 진입"""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """컨텍스트 매니저 종료 (자동으로 브라우저 종료)"""
        self.close()
