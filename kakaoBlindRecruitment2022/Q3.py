from collections import defaultdict

def checktime(in_h, in_m, h, m):
    if m < in_m:
        h -= 1
        m +=60

    diff_h, diff_m = h - in_h, m - in_m
    return diff_h * 60 + diff_m

def solution(fees, records):
    answer = []
    car = [False] * 10000

    parking_time = defaultdict(int)
    parking = {}

    for record in records:
        time, car_number, move = map(str, record.split())
        car[int(car_number)] = True
        h, m = map(int, time.split(':'))

        if move == "IN":
            parking[car_number] = [h, m]
        else:
            in_h, in_m = parking[car_number]
            time = checktime(in_h, in_m, h, m)

            parking_time[car_number] += time
            del parking[car_number]

    if parking:
        for car_number in parking:
            in_h, in_m = parking[car_number]
            time = checktime(in_h, in_m, 23, 59)

            parking_time[car_number] += time

    for i in range(10000):
        if car[i]:
            car_num = str(i).zfill(4)
            p_time = parking_time[car_num]
            fee = fees[1]
            if p_time > fees[0]: 
                fee += ((p_time - fees[0]) // fees[2]) * fees[3] if (p_time - fees[0]) % fees[2] == 0 else (((p_time - fees[0]) // fees[2]) + 1) * fees[3]

            answer.append(fee)
               
    return answer


print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
print(solution([120, 0, 60, 591], ["16:00 3961 IN", "16:00 0202 IN", "18:00 3961 OUT", "18:00 0202 OUT", "23:58 3961 IN"]))
print(solution([1, 461, 1, 10], ["00:00 1234 IN"]))