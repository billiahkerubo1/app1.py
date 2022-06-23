from flask import *
import json,time
app = Flask(__name__)


@app.route('/', methods =['GET'] )
def home_page():
    dataset = {'Page': 'Home', 'Message': 'The home page is successfully loaded', 'Timestamp': time.time()}
    json_dump = json.dumps(dataset)
    return json.dump


@app.route('/user/', methods =['GET'] )
def request_page():

    user_query = str(request.args.get('user'))  #/user/?user = kerubobill
    dataset = {'Page': 'Request', 'Message': 'Successfully got the request for{user_query}', 'Timestamp': time.time()}
    json_dump = json.dumps(dataset)
    return json.dump    


if __name__ == '__main__':
    app.run( host = "0.0.0.0", port = 5501, debug = True)

