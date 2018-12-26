from flask import Flask, render_template, Response
import json, requests, os

app = Flask(__name__)

@app.route('/')
def status():

    try:
        query = 'https://api.mcsrvstat.us/ping/' + os.getenv('SERVER', 'localhost')
        r = requests.get(query)
        j = json.loads(r.text)
    
        server_name = j["description"]["text"]
        online_players = j["players"]["online"]
        max_players = j["players"]["max"]
        version = j["version"]["name"]
        favicon = j["favicon"]
    
        if online_players >= 1:
            player_data = j["players"]["sample"]
        else:
            player_data = None
    
        return render_template('data.html', 
            server_name = server_name,
            online_players = online_players,
            max_players = max_players,
            player_data = player_data,
            version = version,
            favicon = favicon
        )

    except:
        return Response("Not Found", status=404)



