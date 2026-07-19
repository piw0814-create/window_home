import schedule
import time  # 대기 루프용
import logging # 성공실패 기록

logging.basicConfig(level = logging.INFO)

def run_daily_report():
    try :
        #df = load_and_clean('sales.csv')
        #stats = compute_stat(df)
        #render_report(stats)

        logging.info('아침 리포트 생성 완료') # 성공기록

    except Exception as e:
        logging.error('리포트 실패', '+ str(e)') # 실패기록

schedule.every().day.at('08:00').do(run_daily_report)
schedule.every().monday.at('09:00').do(run_daily_report)
schedule.every(1).hours.do(run_daily_report)

while True: # 프로그램을 켜두면
    schedule.run_pending() # 예약 시간이 된 작업을 실행하고,
    time.sleep(60) # 1분마다 예약 확인