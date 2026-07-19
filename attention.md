## 1주

7/15

    제너레이터로 대용량 파일을 메모리 아끼며 처리하기

    dataclass로 데이터 레코드 깔끔하게 정의하기

    Pydantic으로 입력값 검증하기

    functools·파일 IO·pathlib·예외를 한 흐름으로

    pytest 로 정제 함수 테스트하고 Ruff 로 정리

    asyncio·httpx 로 여러 API를 동시에 수집

    Parquet으로 저장하고 필요한 열만 골라 읽기

    수집→검증→저장을 한 스크립트로 — 미니 데이터 파이프라인

    예상되는 문제점들 예외 처리 신경쓰기

    practice1: 매출 레코드 집계 — Counter·defaultdict·컴프리헨션

    TypedDict + mypy — dict 에 타입 계약을 새겨 실행 전에 오류 잡기

    ProcessPoolExecutor — CPU 무거운 전처리를 코어 수만큼 병렬로

    cProfile — 느린 함수를 느낌이 아니라 측정으로 찾기

    practice2 : safe_load_csv와 Pydantic SalesRecord 스키마, valid/errors 분리 저장과 재로딩 검증

    종합실습 1 지정 API — countries.dev 국가 정보 조회 (보완 안내)

        공공 데이터포털 등 무료 JSON API에서 asyncio·httpx로 데이터를 비동기 수집하고, Pydantic으로 스키마를 검증한 뒤 Parquet로 저장하는 스크립트를 작성해 제출한다.

        위 스크립트의 수집·변환 함수에 pytest 테스트를 최소 2개 붙이고, ruff로 정리한 뒤 requirements.txt와 함께 Git으로 커밋해 재현 가능한 형태로 만든다.


7/16

    DataFrame 만들고 열 선택하기, 조건으로 행 필터링하기, groupby로 그룹별 평균 내기

    Polars Lazy API
    
    Plotly Express 로 인터랙티브 차트 한 줄

    t-검정으로 두 그룹 차이가 우연인지 확인

    sklearn Pipeline 으로 전처리+모델을 한 덩어리로 저장

    업종별 매출 합계 상위 뽑고 막대그래프를 파일로 저장하기

    ColumnTransformer — 숫자 열과 글자 열을 각각 다르게 전처리해 결합

    실습3: IQR 이상치 제거 후 named aggregation 집계 (Practice 3)

    실습3: DuckDB로 DataFrame에 바로 SQL 집계 (Practice 3)

    실습4: 카이제곱 검정 — 두 범주형 변수의 독립성 (Practice 4)

    pivot_table 과 merge — 엑셀 피벗과 SQL JOIN 을 Pandas 로

    Pandas 2.x Copy-on-Write — 걸러낸 조각을 고칠 때의 함정

    apply 대신 벡터화 — str·dt 접근자로 열 전체를 한 번에

    schedule 로 매일 아침 리포트 자동 실행 — 반복 분석 자동화
