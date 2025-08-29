import numpy as np
from datetime import datetime


parking = np.zeros((2,10))
parking_log = {}
discount = {
    "1234":30,
    "1409":50
}

def dis() :
    park2 = np.where(parking == 0, "[ ]", "[X]")
    print("       A   B   C   D   E   F   G   H   I   J")
    floor = 2
    for pa in reversed(park2) :
        print(f"{floor}층 | ", end='')
        print(*pa)
        floor-=1

def car_in(car_num) :
    while True :    
        time_in = datetime.now()
        tar_floor = int(input("원하는 층 : "))
        tar_loc = input("원하는 자리 : ").upper()
        idx_fl = tar_floor-1
        idx_loc = ord(tar_loc)-65
        if parking[idx_fl][idx_loc] == 0 :
            break
        else :
            print("이미 주차된 자리입니다.")
    parking[idx_fl][idx_loc] = 1
    parking_log[car_num] = [(idx_fl, idx_loc), time_in, 0, 0]

def car_out(car_num) :
    time_out = datetime.now()
    parking_log[car_num][2] = time_out
    time = time_out - parking_log[car_num][1]
    print(f"""========={car_num} 출차 정보=========
주차 위치 | {parking_log[car_num][0][0]+1}층 {chr(parking_log[car_num][0][1]+65)}
주차 시간 | {time}
주차 요금 |""", end=' ')
    if car_num in discount.keys() :
        cost = 50*np.ceil(time.seconds//60/10)*10*(100-discount[car_num])/100
        print(f"{int(cost)}원 ({discount[car_num]}% 할인)")
    else :
        cost = 50*np.ceil(time.seconds//60/10)*10
        print(f"{int(cost)}원")
    parking[parking_log[car_num][0][0]][parking_log[car_num][0][1]] = 0

while True :
    dis()
    car_num = input("차량 번호를 입력해주세요 : ")
    if car_num == "exit" :
        break
    if car_num in parking_log :
        car_out(car_num)
    else :
        car_in(car_num)