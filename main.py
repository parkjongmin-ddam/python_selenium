"""
메인 실행 파일
Q7: 이 파일을 완성하여 전체 파이프라인을 실행하세요.
"""

# Q7-1: 필요한 모듈들을 import하세요.
# 힌트: config, utils, scraper, pipeline, logging

# Q7-2: 로깅을 설정하세요.
# 힌트: utils.setup_logging() 사용


def main():
    """
    메인 함수
    Q7-3: 전체 파이프라인을 실행하는 코드를 작성하세요.
    
    프로세스:
    1. 설정 확인 (config에서 값 가져오기)
    2. DynamicWebScraper 인스턴스 생성
    3. CrawlingPipeline 인스턴스 생성
    4. pipeline.run() 실행
    5. 에러 처리 (try-except-finally)
    6. 브라우저 종료 보장 (finally 블록 또는 컨텍스트 매니저)
    7. 결과 출력
    
    ⚠️ 중요: 브라우저는 반드시 종료해야 합니다! (메모리 누수 방지)
    """
    # TODO: 메인 로직 작성
    
    # 예시 구조:
    # scraper = None
    # try:
    #     scraper = DynamicWebScraper(...)
    #     pipeline = CrawlingPipeline(...)
    #     result = pipeline.run()
    #     print(f"크롤링 완료! {len(result)}개의 데이터를 수집했습니다.")
    # except Exception as e:
    #     logging.error(f"에러 발생: {e}")
    # finally:
    #     if scraper:
    #         scraper.close()
    
    # 또는 컨텍스트 매니저 사용:
    # with DynamicWebScraper(...) as scraper:
    #     pipeline = CrawlingPipeline(scraper, ...)
    #     result = pipeline.run()
    pass


if __name__ == "__main__":
    main()
