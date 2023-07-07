import time

def pomodoro_timer(total_time):
    print("开始专注时间！")
    remaining_time = total_time * 60

    while remaining_time > 0:
        minutes = remaining_time // 60
        seconds = remaining_time % 60
        print(f"剩余时间：{minutes:02d}:{seconds:02d}")
        time.sleep(1)
        remaining_time -= 1

    print("专注时间结束！")

if __name__ == "__main__":
    total_time = int(input("请输入专注时长（单位：分钟）："))
    pomodoro_timer(total_time)
