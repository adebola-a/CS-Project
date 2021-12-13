import numpy as np
from flask import Flask, request, Response, render_template
import jsonpickle


# Initialize the Flask application
app = Flask(__name__)

imageDB = {}

# route http posts to this method
@app.route('/api/test', methods=['POST'])
def test():
    r = request
    # convert string of image data to uint8
    # decode image
    #img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # do some fancy processing here....

    # build a response dict to send back to client
    #response = {'message': 'image received. size={}x{}'.format(img.shape[1], img.shape[0])}
    # encode response using jsonpickle
    #response_pickled = jsonpickle.encode(response)

    #return Response(response=response_pickled, status=200, mimetype="application/json")
    imageDB[r.headers["Userid"]] = r.data.decode('utf-8')
    #print(r.data.decode('utf-8'))
    #print(type(r.data.decode('utf-8')))
    return "test"

@app.route('/api/get/<string:user_id>', methods=['GET'])
def getting(user_id):
  if user_id in imageDB:
    value = imageDB[user_id]
    return render_template('test2.html', user_id = user_id, image = value)
  else:
    return "User Does Not Exist!"
# start flask app
app.run(host="0.0.0.0", port=5000)