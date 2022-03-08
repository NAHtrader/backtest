# backtest

## 파일 구성

### 실행

- run.py
  전략 백테스팅
- crawl_data.py
  과거 데이터 크롤링용 파일

### 모듈

- backtest.py
  전략은 이곳에 수정
- evaluation.py
  백테스팅 전략 평가용 (현재 기준 : 트레이드 횟수/승률/최고자본잠식률/수익률)

- get.py
  pyupbit 활용 과거 데이터 추출용
- indicator.py
  캔들 지표 모아두는 파일
