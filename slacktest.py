from slacker import Slacker


token = ''

slack = Slacker(token)


s = '1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n'
slack.chat.post_message('#jbot_test', ':thumbsup:')
