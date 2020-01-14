from __future__ import print_function
import json
import urllib
import requests

# https://cashstar.atlassian.net/wiki/display/QA/Mock+Processor+Card+Manipulation

# curl -H "Content-Type: application/json" -X POST --data '{"descriptor": "SUBWAY_SUBWAY_NORMP", "value": 10}' "http://mockproc.qa.cashstar.net:8081/AdminService/create_card"

card_code_bank = "IKEA_IKEAUS_BATCH_NORM_USD"
card_count = 100
output_file = "/tmp/ikea_test_usd_cards_0815a.txt"

data = {
    "descriptor": card_code_bank,
    "value": 0,
    "active": False,
    "issued": False
}

responses = []
for i in range(0, card_count):
    req = requests.Request('http://mockproc.qa.cashstar.net:8081/AdminService/create_card')

    # req.add_header('Content-Type', 'application/json')

    response = requests.urlopen(req, json.dumps(data))
    responses.append(json.load(response))
    print('.', end="")

print("\n")

# format like ikea
with open(output_file, "w") as text_file:
    text_file.write("SELP Card Import;CAZ2;2016-06-10 14:37:17\n")
    for data_response in responses:
        text_file.write(data_response["pan"] + ";" + data_response["pin"] + ";\n")

# upload to qa ftp
print("Run the following command to upload to QA:\n")

print("scp " + output_file + " ftp1.qa.cashstar.net://users/ikea_user/upload/codes/")
