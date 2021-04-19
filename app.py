from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

app.secret_key ="quasiplexus" 

@app.route("/")
def contador():
    try: 
        session['contador']+=1
    except:
        session['contador']=1
    # session['contador']=1
    return render_template("index.html")

@app.route('/masdos', methods=['POST'])
def sumados():
    session['contador']+=1
    return redirect('/')

@app.route('/reseteo', methods=['POST'])
def reset():
    session['contador']=0
    return redirect('/')


if __name__=='__main__':
    app.run(debug=True)