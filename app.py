# from flask import Flask

# app =Flask(__name__)

# @app.route('/')
# def hello():
#     return 'hello world for azure'
# # @app.route('/first')
# # def first():
# #     # if(request.method == 'GET'):
# #     #     data = {
# #     #         "Modules" : 15,
# #     #         "Subject" : "Data Structures and Algorithms",
# #     #     }
# #     #     return jsonify(data)
    
# @app.route('/webhook')
# def webhook():
#    return 'webhook'
        
# if __name__=='__main__':
#     app.run()

from flask import Flask,request,abort,jsonify

app =Flask(__name__)

@app.route('/')
def hello():
    return 'hello world'
@app.route('/first')
def first():
    if(request.method == 'GET'):
        data = {
            "Modules" : 15,
            "Subject" : "Data Structures and Algorithms",
        }
        return jsonify(data)
    
@app.route('/webhook',methods =['GET','POST'])
def webhook():
    if request.method=='POST':
        print(request.json)
        data = request.json
        return 'success'
        
if __name__=='__main__':
    app.run()
