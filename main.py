## IMPORTS
import praw
import time
import steam        # for getting replay files from steam
import re

## GLOBALS

COLOR_DICT = {0 : "blue",
              1 : "teal",
              2 : "purple",
              3 : "yellow",
              4 : "orange",
              128:"pink",
              129:"puse",
              130:"light blue",
              131:"green",
              132:"brown"}

## FUNCTIONS

def check_comment(comment):
	# check the comment based on regex, give back the ID
    if re.match("(http[s]?://)?(www.)?dotabuff.com/players/\d{0,10}",
                    comment.body):
        return str(re.findall("\d{0,10}", comment.body))
    else:
        return False

# To be used, haven't configured it yet.
def oauth():
    # temporary, will change to use praw.ini
    f = open("botpass.txt")
    bot_pass = f.readline()
    f.close()

    r.set_oauth_app_info(client_id='H7CZAzGmv6h-cQ',
                         client_secre=bot_pass,
                         redirect_uri='http://127.0.0.1:65010/'
                                  'authorize_callback')
    access_info = r.get_access_information('hGauT37otwsdciy38Y3yUVNpNXY')

# returns the Reddit object
def connect():

    user_agent = "Windows:DotaColor:v1.0 by /u/blueish101"
    r = praw.Reddit(user_agent=user_agent)
    r.login()
    print("Connecting to Reddit with user_agent")
    return r

# posts a reply to reddit
def reddit_reply(comment, color):
    comment.reply("""Analyzed 100 matches.\n\nThis bot analyzes which color\
        you most commonly play as.\n\n\
        This person is most commonly {}.""".format(color))
    print("Replied to a comment")


## Main method: put it all together:
def main():
    # first call connect
    r = connect()

    for comment in praw.helpers.comment_stream(r, "test"):
        #print("Checking a comment")
        # check the comment if it matches, if it does, we have the profile #
        num = check_comment(comment)
        if num:
            # now we call steam and get the latest 100 game infos
            result = steam.main(num)
            color = COLOR_DICT[result]

            # we have the most used color, reply back to reddit with the info
            reddit_reply(comment, color)

            # print("Replied to a comment")

        #time.sleep(1800)
        # no else condition, skip the comment, and continue
        
    


if __name__ == "__main__":
    main()
