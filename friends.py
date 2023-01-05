import requests
import datetime

def sortSecond(val):
    return val[1]

def getId(paramsId):
    usersUrl = 'https://api.vk.com/method/users.get?v=5.71&access_token=[token]&user_ids=[user_id]'
    r = requests.get(usersUrl, params=paramsId)
    r = r.json()
    return r['response'][0]['id']

def getFriensAgeList(paramsFr):
    urlFriends = 'https://api.vk.com/method/friends.get?v=5.71&access_token=[token]&user_id=[user_id]&fields=bdate'
    respFriends = requests.get(urlFriends, params=paramsFr)
    r = respFriends.json()
    firstlist = r['response']['items']
    return result(generateResList(firstlist))

def calc_age(uid):
    now=int(str(datetime.datetime.now())[:4])
    return now-uid

def generateResList(firstlist):
    resList = list()
    for i in firstlist:
        if('bdate' in i):
            if 7<len(i['bdate']):
                resList.append(calc_age(int(i['bdate'].split('.')[2])))

    return  resList

def result(arr):
    resultDict = dict();
    for i in arr:
        resultDict[str(i)]=0
    for i in arr:
        resultDict[str(i)]+=1
    resultList = list()
    for i in resultDict:
        a = [int(i) , resultDict[i]]
        a = tuple(a)
        resultList.append(a)
    return resultList

if 1 == 1:
    ACCESS_TOKEN = '17da724517da724517da72458517b8abce117da17da72454d235c274f1a2be5f45ee711'
    username = 'maxuver'
    paramsId = {'access_token': ACCESS_TOKEN, 'user_ids': username}
    id = getId(paramsId)
    paramsFr={'access_token':ACCESS_TOKEN, 'user_id': id}
    r = getFriensAgeList(paramsFr)
    r.sort(reverse=True, key=sortSecond)
    print(r)
    r.sort(key=sortSecond)
    print(r)
