from flask import Flask , request

d ={
    "name":"bitue"
}

app = Flask(__name__)



@app.route('/', methods=['GET'])
def home ():
    return "welcome to flask bitue boss"

@app.route('/data', methods=['GET']) 
def data ():
    return d

@app.route('/create/', methods=['PUT']) 
def create ():
    key, value = list(request.args.items())[0]
    try :
        if d[key] :
            return f"already exists {key}"
    except :
        d[key]= value
        return f"success to added {key}"


@app.route('/delete/', methods=['DELETE']) 
def delete ():
    key, value = list(request.args.items())[0]
    try :
        d.pop(value)
        print(list(request.args.items()))
        return f"success to delete {value}"
    except :
        return f"value {value} is not found to delete"



@app.route('/update/', methods=['UPDATE']) 
def update ():
    key, value = list(request.args.items())[0]
    try :
        if d[key] : 
            d[key] = value 
            return f'success to update {key}'
    except :
        return f'not exist '
    
    


if __name__ == '__main__':
    app.run()
