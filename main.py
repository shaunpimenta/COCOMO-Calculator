from flask import Flask,render_template,request
from flaskwebgui import FlaskUI
import json
import random
app=Flask(__name__)
# ui = FlaskUI(app, width=500, height=500)
vali=[]
interval=[[0.75,	0.88,	1,	1.15,	1.4],[0.9,0.94,1,	1.08,1.16],[0.7,0.85,1,1.15,1.3],
          [1.46,	1.19,	1,	0.86,	0.71],[1.29,	1.13,1,	0.91,	0.82],
          [1.42	,1.17,1,	0.86,	0.7],[1.21,	1.1,1,	0.9,	0.8],[1.14,	1.07,1,	0.95,0.9],[1.24	,1.1,	1,	0.91,0.82],
          [1.24	,1.1,1,	0.91,	0.83],[1.23,	1.08,1,	1.04,	1.1]]
fp={"C":128,"Java":53,"Python":64}
def fploc(lang,fpoint):
    pt=int(fp[lang])
    return fpoint*pt
def application(NAP,reuse,PROD):
    PM = (NAP * (1 - reuse / 100)) / PROD
    return  PM
def early(A,Size,EAF,b=1):
    PM = A * Size**b * EAF
    return PM
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
    # return render_template('form.html')


@app.route('/inter', methods=['GET','POST'])
def processinter():
    # if request.method=="POST":
    # content=request.content_type
    # if content =='application/json':

    # for i in range(1, 12):
    #     a = f'rb-{i}'
    #     val.append(request.form.get(a))
    a=request.get_data()
    # val = [a[i][0] for i in range(len(a))]
    print(a)

    vals=a.decode()

    val=eval(vals)
    print(type(val[0]))
    # print(request.get_json())

    # print(val)
    # print(1)
    # values=[interval[i][val[i]-1] for i in range(12)]
    values=[]
    for i in range(11):
        values.append(interval[i][val[i]-1])
    print(values)
    # print(values)
    # values = []
    kloc = random.uniform(1, 5)
    # for i in range(12):
    #     values.append(random.uniform(0.5, 1.4))
    ans = inter(values, vali[0], vali[1], vali[2], vali[3], kloc)
    # return render_template('index.html')
    return render_template('basic.html', mode="Intermediate COCOCMO I", effort=ans[0], time=ans[1], person=ans[2])
    # else:
    #     render_template('intermediate.html')
@app.route('/cocomo2')
def cocomo2():
    global vali
    model = request.form.get('model')
    mode = request.form.get('mode')
    val = json.loads(mode)
    kloc = request.form.get('kloc')
    if kloc == '':
        return render_template('form.html', msg="alert('Please choose a model to continue');")
    print(mode)
    if model == "Post":
        ans = organic(val[0], val[1], val[2], val[3], int(kloc))
        return render_template('basic.html', mode="Basic Organic", effort=ans[0], time=ans[1], person=ans[2])
    elif model == "Early":
        # if request.method=='POST':
        vali = val
        # print(request.ge['rb-1'])
        # for i in range(12):
        #     val.append(req)

        return render_template('intermediate.html')
    elif model == "Application":
        vali = val
        return render_template('advanced.html')
    elif model == "Reuse":
        vali = val
        return render_template('advanced.html')
    else:
        print('Hi')
    render_template('form2.html')
@app.route('/adv')
def processadv():
    values = []
    kloc=random.uniform(1,5)
    for i in range(15):
        values.append(random.uniform(0.5,1.4))
    ans=inter(values, vali[0], vali[1], vali[2], vali[3], kloc)
    return render_template('basic.html',mode="Advanced COCOMO I",effort=ans[0],time=ans[1],person=ans[2])

# from flaskwebgui import FlaskUI
# from main import app
print("Hello2")
if __name__=="__main__":
    # ui.run()
    FlaskUI(app, width=1300, height=900, close_server_on_exit=False).run()
    FlaskUI(app)
    print('Hello1')
# FlaskUI.keep_server_running(FlaskUI(app))
FlaskUI.stop_webserver(FlaskUI(app))
    # app.run(debug=True)