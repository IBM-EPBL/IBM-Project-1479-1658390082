3. Create sample program for Flask HTTP methods (list or map and perform operations of PUT,GET,DELETE and POST).


from flask import Flask,request,json

app=Flask(__name__)

fruits={"1":"Apple", "2":"Orange" , "3":"Guava" , "4":"Grape" , "5":"Cherries", "6":"Melon" ,"7":"Blueberries"}

@app.route('/data' ,methods=['GET','POST'])
def api():
    if request.method=='GET':
        return fruits
    if request.method=='POST':
        data=request.json
        fruits.update(data)
        return 'data got inserted'

@app.route("/data/<id>",methods=['PUT'])
def update(id):
    data=request.form['items']
    fruits[str(id)]=data
    return 'data updated'

@app.route("/data/<id>",methods=["DELETE"])
def deleteoperation(id):
    fruits.pop(str(id))
    return 'data deleted'

if__name__=='__main__':
   app.run(debug=True)


