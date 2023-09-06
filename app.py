from flask import Flask,render_template,request,jsonify
app = Flask(__name__)

@app.route('/',methods=['POST'])
def calculate():
    
    data = request.get_json()
    a_val = int(dict(data)['a'])
    b_val = int(dict(data)['b'])
    
    return jsonify(a_val+b_val)



if __name__=='__main__':
    app.run(debug=True)