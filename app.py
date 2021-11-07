from flask import Flask
"data":[
    {
        "contact":"9987644456",
        "name":"raju",
        "done":"false",
        "id": 1
    },
    {
        "contact":"9876543222",
        "name":"rahul",
        "done":"false",
        "id": 2
    }
]

@app.route("/add-data",methods=["POST"])
def add_task():
    if not request.json:
        "status":"error",
        "message":"plese provide the data!"
        },400)

contact={
    "id":tasks[-1]['id'] + 1,
    "name":request.jsonp['name'],
    "contact":request.json.get('contact',""),
    "done":false
}