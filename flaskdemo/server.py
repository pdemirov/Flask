from flask import Flask, jsonify, make_response

app = Flask(__name__) #After importing the Flask module, create your Flask application by initializing the Flask class.

@app.route("/") #You can now use the app you created in the previous task to create your first route.
def index():  #Define the method for the main root URL.
    #return "hello world"  #Return the “Hello World” message to the client.

    #return {  #json return  #standart dictionary json
    #    "1": 'hello',
    #    "2": 'world'
    #}
    return jsonify(message = 'hello world!!!') #jsonify 

@app.route("/no_content")
def no_content():
    #return jsonify(message = "no content found"), 204
    return {"message": "no content found"}, 204
    

@app.route('/exp')
def index_explicit():
    resp = make_response({"message": "response with make response ;)"})
    resp.status_code = 200
    return resp

