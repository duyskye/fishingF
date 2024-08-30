import requests
import time
import random as rd
import json

def read_to_json(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)

    return data



def catchFish(userId, fishId, transId, token):
    url = f"https://fishing-frenzy-api-0c12a800fbfe.herokuapp.com/v1/fish/catchFish?userId={userId}&fishInfoId={fishId}&transactionId={transId}"

    payload = {}

    headers = {
    'Accept-Language': 'en-US,en;q=0.9,vi;q=0.8',
    'Authorization': token,
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Origin': 'https://fishingfrenzy.co',
    'Pragma': 'no-cache',
    'Referer': 'https://fishingfrenzy.co/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    'accept': 'application/json',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.status_code)
    print(response.text)

def getFish(token, userId):
    url = f"https://fishing-frenzy-api-0c12a800fbfe.herokuapp.com/v1/fish/getResult?userId={userId}&range=long_range"

    payload = {}
    headers = {
    'Accept-Language': 'en-US,en;q=0.9,vi;q=0.8',
    'Authorization': token,
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Origin': 'https://fishingfrenzy.co',
    'Pragma': 'no-cache',
    'Referer': 'https://fishingfrenzy.co/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    'accept': 'application/json',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.status_code)
    print(response.text)
    if response.status_code == 200:
        data = response.json()
        transactionId = data['transactionId']
        fishInfoId = data['randomFish']['id']
        time.sleep(rd.randint(5,10))
        catchFish(userId, fishInfoId, transactionId, token)



def main(token):
    url = "https://fishing-frenzy-api-0c12a800fbfe.herokuapp.com/v1/inventory"

    payload = {}
    headers = {
    'Accept-Language': 'en-US,en;q=0.9,vi;q=0.8',
    'Authorization': token,
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Origin': 'https://fishingfrenzy.co',
    'Pragma': 'no-cache',
    'Referer': 'https://fishingfrenzy.co/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    'accept': 'application/json',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.status_code)
    if response.status_code == 200:
        data = response.json()
        run_time = data['energy'] // 3
        print(f"Fishing {run_time} times")
        user_id = data['userId']
        for _ in range(run_time):
            getFish(token, user_id)
        print("Done!!!")



accounts = read_to_json("accounts.json")

for token in accounts:
    main(token)
