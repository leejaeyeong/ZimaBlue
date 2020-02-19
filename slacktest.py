from slacker import Slacker


token = 'xoxb-944330254352-947046696531-tCEAJQLRa0PNLW7GyA0DGO2y'

slack = Slacker(token)

s = '1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n'
slack.chat.post_message('#jbot_test', ':thumbsup:')
