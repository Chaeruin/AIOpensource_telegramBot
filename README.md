2. telegram scheduler bot
 1) 과정
  - 최신 telegram bot api 업데이트로 인한 
   비동기 라이브러리 async / asyncio / 비동기 스케줄러 동시 사용성 문제 발생 
   -> 해당 동시 사용 관련 자료 부족 및 크론탭으로도 작동 안됨
  - 해결 : api 모듈 버전 다운그레이드 - 13.14 버전 사용

 2) 환경
  - 아나콘다 가상환경 (name : cv)(python==3.11)

