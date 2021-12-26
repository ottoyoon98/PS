import requests
import json

x_auth_token = 'bc15b59d9d79f9de5b7c37287fb0a80d'
base_url = 'https://huqeyhi95c.execute-api.ap-northeast-2.amazonaws.com/prod'
start_url = '/start'
waiting_url = '/waiting_line'
GameResult_url = '/game_result'
UserInfo_url = '/user_info'
Match_url = '/match'
ChangeGrade_url = '/change_grade'

# start API & 0 turn

print("START API request")
url = base_url+start_url
headers = {
    'X-Auth-Token': x_auth_token,
    'Content-Type': 'application/json',
}
data = '{"problem": 2}'
response = requests.post(url=url, headers=headers, data=data)
rdata = response.json()
print(rdata)
auth_key = rdata["auth_key"]
headers = {
    'Authorization': auth_key,
    'Content-Type': 'application/json'
}
user_info = requests.get(url=base_url+UserInfo_url, headers=headers)
data = '{"command": ['
n = len(user_info.json()['user_info'])
ability = list([4000 for _ in range(n+1)])
for x in user_info.json()['user_info']:
    data += "{\'id\': "+str(x['id'])+", \'grade\': 4000}, "
    #data += ''
data += ']}'
response = requests.put(url=base_url+ChangeGrade_url, headers=headers, data=data)


print("Match API")
url = base_url + Match_url
data = '{"pairs": [[1,1]]}'
match = (requests.put(url=url, headers=headers, data=data)).json()
print(match)

# 1~595 turn
for turn in range(1, 596): # 596
    print(turn)
    # GameResult API
    print("GameResult API request")
    url = base_url+GameResult_url
    gameResult = requests.get(url=url, headers=headers)

    # ChangeGrade API
    data = '{"command": ['
    for x in gameResult.json()['game_result']:
        win = x['win']
        lose = x['lose']
        taken = x['taken']
        diff = int((40-taken)*49500//35)
        if ability[lose]-ability[win]>500 and taken <=10:
            ability[win]-=diff
            ability[lose]+=diff

        ability[win]+=diff
        ability[lose]-=diff
        data += "{'id': "+str(win)+", 'grade': "+str(ability[win])+"}, "
        data += "{'id': "+str(win)+", 'grade': "+str(ability[lose])+"}, "
    data += ']}'
    response = requests.put(url=base_url+ChangeGrade_url, headers=headers, data=data)


    #print(gameResult.json()['game_result'])
    data = '{"pairs": ['
    if turn <= 555:
        # WaitingLine API
        print("waitingLine API request")
        url = base_url+waiting_url
        waitingLine = requests.get(url=url, headers=headers)
        print(waitingLine.json())
        waiting = sorted(waitingLine.json()['waiting_line'], key=lambda x: (-ability[x['id']], x['from']))
        m = len(waiting)
        if m==2:
            A = waiting[0]
            B = waiting[1]
            if (turn-A['from'])>10 or (turn-B['from'])>10:
                data += '[' + str(A['id']) + ',' + str(B['id']) + '],'
        else:
            i = 1
            while i < m-1:
                A = waiting[i-1]
                B = waiting[i]
                C = waiting[i+1]
                if abs(ability[B['id']]-ability[A['id']]) < abs(ability[C['id']]-ability[B['id']]):
                    data += '[' + str(A['id']) + ',' + str(B['id']) + '],'
                    i+=2
                else:
                    data += '[' + str(B['id']) + ',' + str(C['id']) + '],'
                    i+=3

    # Match API
    print("Match API request")
    url = base_url+Match_url
    data += '[1,1]]}'
    match = requests.put(url=url, headers=headers, data=data)
    print(match.json())


print(ability)

#score API
response = requests.get(url=base_url+'/score', headers=headers)
print(response.json())
