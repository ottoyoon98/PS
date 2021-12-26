def solution(fees, records):
    baseT, baseP, unitT, unitP = fees
    cars = {}
    for X in records:
        HHMM, carID, state = X.split(" ")
        time = int(HHMM[0:2])*60+int(HHMM[3:])
        carID = int(carID)
        previous = cars.get(carID)
        # cars = { key(carID): value([total time, lastIntime])}      // if lastInTime==-1 out상태
        totalTime=0
        parkingTime=0
        if previous != None:
            totalTime = previous[0]
            parkingTime = (time-previous[1])
        if state == "IN":
            cars[carID] = [totalTime, time]
        else:
            cars[carID] = [totalTime+parkingTime,-1]
    print(cars)
    time = 23 * 60 + 59
    cars2 = []
    for key, value in cars.items():
        temp = value[0]
        if value[1] != -1:
            temp += time - value[1]
        print(temp)
        cars2.append([key, baseP+(((temp-baseT if temp-baseT > 0 else 0)+(unitT-1))//unitT)*unitP])
    cars2 = sorted(cars2, key=lambda x: (x[0]))
    answer = list([x[1] for x in cars2])
    return answer
print(solution([180, 5000, 10, 600],["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))