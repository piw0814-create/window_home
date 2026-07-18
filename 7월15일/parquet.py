import pandas as pd #표(DataFrame) 처리 라이브러리

#도시별 날씨 수집이 끝났다고 가정한 표
df = pd.DataFrame({
    "도시": ["서울", "도쿄", "뉴욕", "런던"],
    "기온": [25.7, 28.1, 23.0, 24.3],
    "현지시각": ["16:46", "16:46", "03:46", "08:46"],   
})

df.to_parquet("weather.parquet") #parquet(열 단위 압축 형식) 파일로 저장

try:
    slim = pd.read_parquet("weather.parquet", columns=["도시","기온"])#필요한 열만 읽기
    print(slim)
except FileNotFoundError:
    print("weather.parquet 이 없습니다. 저장 단계를 먼저 실행하세요")

'''
궁금했던점

왜 굳이 parquet를 쓸까?
Parquet을 쓰는 핵심 이유는 데이터가 커질수록 CSV보다 저장과 분석이 효율적이기 때문

1. 파일 용량이 작아짐
Parquet은 열 단위로 저장하고 압축해.
예를 들어 도시 열에는 문자열만, 기온 열에는 실수만 모여 있어서 같은 성격의 데이터끼리 압축하기 유리해.

2. 읽는 속도가 빠름

CSV는 파일을 읽을 때 문자열을 다시 숫자나 날짜로 해석해야 해.
Parquet은 자료형을 저장하고 있어서 바로 읽을 수 있어.

3. 필요한 열만 읽을 수 있음

데이터에 열이 100개 있는데 기온 열만 필요하다면:
df = pd.read_parquet(
    "weather.parquet",
    columns=["기온"],
)
Parquet은 필요한 열만 읽을 수 있어.
CSV는 기본적으로 파일의 전체 행과 열을 훑어야 해서 비효율적일 수 있어.

4. 자료형이 보존됨

CSV는 전부 문자처럼 저장돼.

도시,기온
서울,25.7

다시 읽을 때 Pandas가 자료형을 추론해야 해.

Parquet은 다음과 같은 자료형 정보를 함께 저장해.

도시: 문자열
기온: 실수
날짜: datetime

그래서 데이터 타입이 비교적 안정적으로 유지돼.

5. 분석 도구와 잘 맞음

Parquet은 Pandas뿐 아니라 다음 도구에서도 많이 사용해.

Polars
DuckDB
Spark
PyArrow
데이터 레이크
클라우드 분석 환경

그래서 대용량 데이터 분석 파이프라인에서 많이 쓰여.

CSV
→ 사람이 직접 열어보기 쉬움
→ 제출, 공유, 간단한 데이터에 편리

Parquet
→ 용량이 작음
→ 읽기가 빠름
→ 자료형 보존
→ 필요한 열만 읽기 가능
→ 대용량 분석에 적합

csv 에서, 내가 원하는 열들만 골라서 parquet로 만들수도 있겠네

맞아. CSV를 읽을 때부터 원하는 열만 골라서 Parquet으로 저장할 수 있어.

import pandas as pd

df = pd.read_csv(
    "weather.csv",
    usecols=["도시", "기온"],
)

df.to_parquet("weather_selected.parquet", index=False)

weather.csv
→ 도시, 기온 열만 읽음
→ 작은 DataFrame 생성
→ weather_selected.parquet로 저장
'''