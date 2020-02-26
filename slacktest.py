import json
from slacker import Slacker
from flask import Flask, request, make_response


with open('config.json') as json_file:
    json_data = json.load(json_file)

    # 문자열
    # key가 json_string인 문자열 가져오기
    json_string = json_data["Bot Token"]
    print(json_string)
