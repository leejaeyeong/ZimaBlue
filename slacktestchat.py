import json
from collections import OrderedDict
from slacker import Slacker

slack = None
with open('config.json') as json_file:
    token = json.load(json_file)["Bot Token"]
    slack = Slacker(token)

army = {
	"color" : '#2398cf',
    "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*[대성고속] 부릉부릉 버스 곧 출발합니다. :oncoming_bus:*"
                }
            },
            {
                "type": "divider"
            },
            {
                "type": "section",
                "fields": [
                    {
                        "type": "mrkdwn",
                        "text": "*어디로?*\n`한기대 -> 야우리`"
                    },
                    {
                        "type": "mrkdwn",
                        "text": "*남은 시간*\n `{}` 분".format(50)
                    },
                    {
                        "type": "mrkdwn",
                        "text": "*다음 버스*\n{}".format('_07:00_')
                    },
                    {
                        "type": "mrkdwn",
                        "text": "*그 다음 버스*\n{}".format('_08:20_')
                    },
					{
                        "type": "mrkdwn",
                        "text": '*전체 버스 시간표*\n<{}|{}>'.format('https://hantalk.io/bus','보기')
                    }

					
                ],
				"accessory": {
				"type": "image",
				"image_url": "https://raw.githubusercontent.com/leejaeyeong/ZimaBlue/master/reading_room_status.png",
				"alt_text": "Haunted hotel image"
			}
			
			
		}
    ]
}





api = {
	"blocks": [
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Danny Torrence left the following review for your property:"
			}
		},
		{
			"type": "section",
			"block_id": "section567",
			"text": {
				"type": "mrkdwn",
				"text": "<https://example.com|Overlook Hotel> \n :star: \n Doors had too many axe holes, guest in room 237 was far too rowdy, whole place felt stuck in the 1920s."
			},
			"accessory": {
				"type": "image",
				"image_url": "https://raw.githubusercontent.com/leejaeyeong/ZimaBlue/master/reading_room_status.png",
				"alt_text": "Haunted hotel image"
			}
		},
		{
			"type": "section",
			"block_id": "section789",
			"fields": [
				{
					"type": "mrkdwn",
					"text": "*Average Rating*\n1.0"
				}
			]
		}
	]
}





#slack.chat.post_message('#jbot_test',attachments=[notice])

#print(notice)
jsonData = OrderedDict()
jsonSub = OrderedDict()

jsonData['blocks'] = []
jsonData['blocks'].append({'type' :'section','text' : {'type' :'mrkdwn','text' : '<https://example.com|Overlook Hotel>' }})
jsonData['blocks'].append({'type' :'section','text' : {'type' :'mrkdwn','text' : '<http://naver.com|네이버>' }})
jsonData['blocks'].append({'type' :'section','text' : {'type' :'mrkdwn','text' : 'Danny Torrence left the following review for your :property:' }})
jsonData['blocks'].append({'type' :'section','text' : {'type' :'mrkdwn','text' : 'Danny Torrence left the following review for your :property:' }})



slack.chat.post_message('#jbot_test',attachments=[army])