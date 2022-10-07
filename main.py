from flask import Flask,render_template,request
from flaskwebgui import FlaskUI
import json
import random
app=Flask(__name__)
ui = FlaskUI(app, width=500, height=500)
vali=[]

def organic( a, b, c, d, KLOC=1):
    print(f"Hi a is {a}")
    E = a * ((KLOC) ** b)
    time = c * ((E) ** d)
    person = E / time
    print(person, time, E)
    return [E, time, person]

def inter(val,a,b,c,d,KLOC):
    eaf=1
    # global val
    for i in val:
        eaf*=i
    E = a * ((KLOC) ** b)*eaf
    time = c * ((E) ** d)
    person = E / time
    return [person, time, E]
    # return render_template('basic.html',mode="Basic Organic",effort=E,time=time,person=time)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/calculate', methods=['GET'])
def calculate():
    return render_template('calculate.html')

@app.route('/calculate')
def calculate_c():
    return render_template('calculate.html')

@app.route('/details')
def details():
    return render_template('details.html')

@app.route('/cocomo 1')
def cocomo1():
    return render_template('cocomo1.html')

@app.route('/form',methods=("GET","POST"))
def form():
    return render_template('form.html')

@app.route('/process',methods=("GET","POST"))
def processbasic():
    global vali
    model=request.form.get('model')
    mode=request.form.get('mode')
    val=json.loads(mode)
    kloc=request.form.get('kloc')
    if kloc=='':
        return render_template('form.html',msg="alert('Please choose a model to continue');")
    print(mode)
    if model=="Basic":
        ans=organic(val[0],val[1],val[2],val[3],int(kloc))
        return render_template('basic.html',mode="Basic Organic",effort=ans[0],time=ans[1],person=ans[2])
    elif model=="Inter":
        # if request.method=='POST':
        vali=val
            # print(request.ge['rb-1'])
            # for i in range(12):
            #     val.append(req)

        return render_template('intermediate.html')
    elif model=="Adv":
        vali=val
        return render_template('advanced.html')
    else:
        print('Hi')
        return render_template('form.html',msg="alert(1);")
    return render_template('form.html')

@app.route('/inter')
def processinter():
    values = []
    kloc=random.uniform(1,5)
    for i in range(12):
        values.append(random.uniform(0.5,1.4))
    ans=inter(values, vali[0], vali[1], vali[2], vali[3], kloc)
    return render_template('basic.html',mode="Intermediate COCOCMO I",effort=ans[0],time=ans[1],person=ans[2])

@app.route('/adv')
def processadv():
    values = []
    kloc=random.uniform(1,5)
    for i in range(15):
        values.append(random.uniform(0.5,1.4))
    ans=inter(values, vali[0], vali[1], vali[2], vali[3], kloc)
    return render_template('basic.html',mode="Advanced COCOMO I",effort=ans[0],time=ans[1],person=ans[2])
if __name__=="__main__":
    ui.run()
    # app.run()