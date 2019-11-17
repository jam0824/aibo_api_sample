# file name is "execute_action_api.py"
import requests
import sys
import json
import time

deviceId = ''
headers = {
'Authorization': 'Bearer 取得したaccessToken',
}

TIME_OUT_LIMIT = 30

#GETを使うときの
def get_method(url):
    response = requests.get(url, headers=headers)
    return json.loads(response.text)

#一匹めのdeviceIdを取得
def get_deviceId():
    get_result =get_method('https://public.api.aibo.com/v1/devices')
    return get_result['devices'][0]['deviceId']

#コマンド実行を行い、executionIdを返す
def get_executionId(post_url, data):
    # POST API
    response = requests.post(post_url, headers=headers, data=data)
    post_result = json.loads(response.text)
    return post_result["executionId"]

#コマンド実行後の結果取得
def get_result(get_result_url):
    TimeOut = 0
    while True:
        get_result =get_method(get_result_url)
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

#実行したいコマンドとパラメーターを渡すと、実行して、結果を返す
def exec_api(api_name, arguments):
    post_url = 'https://public.api.aibo.com/v1/devices/' + deviceId + '/capabilities/' + api_name + '/execute'
    data = '{"arguments":' + arguments + '}'  if arguments != '' else '{}'
    executionId = get_executionId(post_url, data)
    # Get Result of API execution
    get_result_url = 'https://public.api.aibo.com/v1/executions/' + executionId
    print("get url: " + get_result_url)
    return get_result(get_result_url)


if __name__ == '__main__':
    length = len(sys.argv)
    if length == 3:
        deviceId = get_deviceId()
        result = exec_api(sys.argv[1], sys.argv[2])
        print(result)
    elif length == 2:
        deviceId = get_deviceId()
        result = exec_api(sys.argv[1], '')
        print(result)
    else :
        print("If you want to exec Action API, aibo_api.py <action api name> <parameters>, \nin the case of Cognition API, aibo_api.py <action api name>")
        print("\nCommand list: https://developer.aibo.com/jp/docs#action-api\n")
        exit(1)