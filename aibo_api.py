# file name is "execute_action_api.py"
import requests
import sys
import json
import time

deviceId = 'aiboのdeviceId'
headers = {
'Authorization': 'Bearer 取得したaccessToken',
}

TIME_OUT_LIMIT = 30

def get_executionId(post_url, data):
    # POST API
    response = requests.post(post_url, headers=headers, data=data)
    post_result = json.loads(response.text)
    return post_result["executionId"]

def get_result(get_result_url):
    TimeOut = 0
    while True:
        response = requests.get(get_result_url, headers=headers)
        get_result = json.loads(response.text)
        get_status = get_result["status"]

        if get_status == "SUCCEEDED":
            break
        elif get_status == "FAILED":
            break

        TimeOut += 1
        if TimeOut > TIME_OUT_LIMIT:
            print("Time out")
            break
        print('Elapsed time : ' + str(TimeOut) + "sec")
        time.sleep(1)
    return get_result

def exec_api(api_name, arguments):
    post_url = 'https://public.api.aibo.com/v1/devices/' + deviceId + '/capabilities/' + api_name + '/execute'
    data = '{"arguments":' + arguments + '}'  if arguments != '' else '{}'
    executionId = get_executionId(post_url, data)
    # Get Result of API execution
    get_result_url = 'https://public.api.aibo.com/v1/executions/' + executionId
    print("get url: " + get_result_url)
    return get_result(get_result_url)

#Action APIを実行するときはこんな感じ。コマンドプロンプトからはダブルクォーテーションはエスケープして渡す。
#python aibo_api.py turn_around '{\"TurnSpeed\":2,\"TurnAngle\":180}'
#Cognition APIを実行するときは以下。
#python aibo_api3.py hungry_status
if __name__ == '__main__':
    length = len(sys.argv)
    if length == 3:
    	print(sys.argv[2])
    	result = exec_api(sys.argv[1], sys.argv[2])
    	print(result)
    elif length == 2:
        result = exec_api(sys.argv[1], '')
        print(result)
    else :
        print("If you want to exec Action API, aibo_api.py <action api name> <parameters>, \nin the case of Cognition API, aibo_api.py <action api name>")
        print("\nCommand list: https://developer.aibo.com/jp/docs#action-api\n")
        exit(1)