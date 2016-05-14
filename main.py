## git:blueish/all-chat-bot

## IMPORTS
import praw
import time
# import reddit       # for the reddit portion
import subprocess   # for calling all of the different modules
import process      # for processing the json fles
import steam        # for getting replay files from steam
import re

def check_comment(comment):
	# check the comment based on re
	return re.match("(http[s]?://)?(www.)?dotabuff.com/players/\d{0,10}",
	                comment.body) ? 
	                re.findall("\d{0,10}", comment.body) : False



## Main method: put it all together:
def main():
    # first call connect
    r = connect_to_reddit()

    for comment in praw.helpers.comment_stream(r, "allchatbot"):
    	num = check_comment(comment)
    	if num:

            # find a way to save all of the match IDs we've processed, and
            # filter them so we don't do them again.

            # We now have match IDs as strings, we need the matches
            # connect to Steam API to retrieve them
            # for item in arr:
            #     success = steam.main(item)
            #     success ?
            #         print("Sucessful download of {} from steam".format(item)) :
            #         print("Error downloading of {} from steam".format(item))


            # We have the replay files, now we call them with clarity
            # for item in arr:
            #     clarity_output = subprocess.check_output([item  + ".TODO~!!"])
            #         print("Error processing item{}\n".format(item))

            # Clarity has processed each match, and placed it in a file "matchID.json"
            # now we call the process.py for translation back into python classes
            all_chat = []
            for item in arr:
                chat_message = process.main(item)
                chat_message ?
                    print("Sucessful processing of {} from steam".format(item)) :
                    print("Error processing of {} from steam".format(item))
                all_chat.append(chat_message)

            # we have each match processed and all of the messages are now in an array
            # let's process results
            result = process.process_chat(all_chat)
            
        # no else condition, skip the comment, and continue
        
    


# if __name__ == "main.py":
    # main()
