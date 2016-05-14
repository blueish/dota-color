import urllib.request
import json

base_id = "http://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/v1/"


def call_steam(key, ID):
	''' Calls steam and returns a dict of the result given the key, and the ID of user'''
	path = base_id + "?key=" + key + "&account_id=" + ID
	r = urllib.request.urlopen(path)
	data = json.loads(r.read().decode(r.info().get_param('charset') or 'utf-8'))
	return data

def parse_data(data, ID):
	count = {0:0, 1:0, 2:0, 3:0, 4:0, 128:0, 129:0, 130:0, 131:0, 132:0}
	# if status == 15, private profile, can't get
	if data['result']['status'] == 15:
		return False
	# iterate through matches, find the player and add corresponding color
	else:
		for match in data['result']['matches']:
			for player in match["players"]:
				if player["account_id"] == ID:
					count[player["player_slot"]] += 1
		# easy trick from stackoverflow.com/questions/268272
		# gets the key for the largest value
		inverse = [(value, key) for key, value in count.items()]
		return max(inverse)[1]

def main(ID):
    # call steam
    f = open("key.txt")
    key = f.readline()

    # now we parse through the data
    data = call_steam(key, ID)
    return parse_data(data, ID)





