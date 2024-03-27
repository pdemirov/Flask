from flask import Flask, make_response, request

app = Flask(__name__)

data = [
    {
        "id": "3b58aade-8415-49dd-88db-8d7bce14932a",
        "first_name": "Tanya",
        "last_name": "Slad",
        "graduation_year": 1996,
        "address": "043 Heath Hill",
        "city": "Dayton",
        "zip": "45426",
        "country": "United States",
        "avatar": "http://dummyimage.com/139x100.png/cc0000/ffffff",
    },
    {
        "id": "d64efd92-ca8e-40da-b234-47e6403eb167",
        "first_name": "Ferdy",
        "last_name": "Garrow",
        "graduation_year": 1970,
        "address": "10 Wayridge Terrace",
        "city": "North Little Rock",
        "zip": "72199",
        "country": "United States",
        "avatar": "http://dummyimage.com/148x100.png/dddddd/000000",
    },
    {
        "id": "66c09925-589a-43b6-9a5d-d1601cf53287",
        "first_name": "Lilla",
        "last_name": "Aupol",
        "graduation_year": 1985,
        "address": "637 Carey Pass",
        "city": "Gainesville",
        "zip": "32627",
        "country": "United States",
        "avatar": "http://dummyimage.com/174x100.png/ff4444/ffffff",
    },
    {
        "id": "0dd63e57-0b5f-44bc-94ae-5c1b4947cb49",
        "first_name": "Abdel",
        "last_name": "Duke",
        "graduation_year": 1995,
        "address": "2 Lake View Point",
        "city": "Shreveport",
        "zip": "71105",
        "country": "United States",
        "avatar": "http://dummyimage.com/145x100.png/dddddd/000000",
    },
    {
        "id": "a3d8adba-4c20-495f-b4c4-f7de8b9cfb15",
        "first_name": "Corby",
        "last_name": "Tettley",
        "graduation_year": 1984,
        "address": "90329 Amoth Drive",
        "city": "Boulder",
        "zip": "80305",
        "country": "United States",
        "avatar": "http://dummyimage.com/198x100.png/cc0000/ffffff",
    }
]

# start flask app : flask --app server --debug run

@app.route("/")
def index():
    return "hello world"

#no content http response
@app.route("/no_content")
def no_content():
    return {"message": "no content!!!"}, 204

#success http response
@app.route("/exp")
def index_explicit():
    resp = make_response({"message": "hello world!!!"})
    resp.status_code = 200
    return resp

#show the lenght of the data
@app.route("/data")
def get_data():
    try:
        if data and len(data) > 0:
            return {"message": f"Data of lenght {len(data)} found"}
        else:
            return {"message": "Data is empty"}, 500
    except NameError:
        return {"message": "Data not found"}, 404

#search by name (first_name) in the data
@app.route("/name_search")
def name_search():
    query = request.args.get("q")

    if not query:
        return {"message:" : "Invalid input parameter"}, 422

    for person in data:
        if query.lower() in person["first_name"].lower():
            return person
        
    return {"message": " Person not found"}, 404


#get the count of the data
@app.route("/count")
def count():
    try:
        return {"data count": len(data)}
    except NameError:
        return {"message :" "data not defined"}, 500

#get user data by passing uuid into the url
# retrieve data from app for the particular app route : curl -X GET -i -w "\n" localhost:5000/{route url}    
@app.route("/person/<uuid:id>")
def find_by_uuid(id):
    for person in data:
        if person["id"] == str(id):
            return person

    return {"message" : "person not found"}, 404



#delete user by passing uuid into the url
# delete user by executing this command in the terminal - curl -X DELETE -i localhost:5000/person/66c09925-589a-43b6-9a5d-d1601cf53287
@app.route("/person/<uuid:id>", methods=['DELETE'])
def delete_by_uuid(id):
    for person in data:
        if person["id"] == str(id):
            data.remove(person)
            return {"message": f"id of person {id} has been deleted"}, 200
    return {"message": "person not found"}, 404


#Parse JSON from Request body
#add user into the data with post request, the user data must be JSON
@app.route("/person" ,methods=['POST'])
def add_by_uuid():
    new_person = request.get_json()
    if not new_person:
        return {"message" : "invalid input parameter"}, 422
    
    data.append(new_person)
    return {"message" : f"{new_person['id']}"}, 200



"""
Command to add user by inserting JSON data into the data

curl -X POST -i -w '\n' \
  --url http://localhost:5000/person \
  --header 'Content-Type: application/json' \
  --data '{
        "id": "4e1e61b4-8a27-11ed-a1eb-0242ac120002",
        "first_name": "John",
        "last_name": "Horne",
        "graduation_year": 2001,
        "address": "1 hill drive",
        "city": "Atlanta",
        "zip": "30339",
        "country": "United States",
        "avatar": "http://dummyimage.com/139x100.png/cc0000/ffffff"
}'

"""

# start flask app : flask --app server --debug run
# retrieve data from app for the particular app route : curl -X GET -i -w "\n" localhost:5000/{route url}     