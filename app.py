from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route('/')
def welcome():
    #return "Welcome to Flask, Hurray, we are going to have lot of learning"
    return render_template('index.html')
@app.route('/success/<int:score>')   
def success(score):
    #return "You are passed and your marks are : " + str(score)
    return render_template('success.html',value=score)

@app.route('/fail/<int:score>')  
def fail(score):
    #return "You are failed and your marks are : " + str(score)
    return render_template('fail.html',value=score)

#@app.route('/result/<int:score>')  
'''def result(score):
    if score>=50:
        return " Pass and your marks are : " + str(score)
    else:
        return " Fail and your marks are : " + str(score)'''

@app.route('/result/<int:score>')  
def result(score):
    result = " "
    if score>=50:
        result='success'
    else:
        result = 'fail'
    return redirect(url_for(result,score=score))


@app.route('/submit', methods=['POST','GET'])  
def submit():
    total_score=0
    if request.method=='POST':
        DL=float(request.form['DL'])
        ML=float(request.form['ML'])
        Python=float(request.form['Python'])
        total_score=(DL+ML+Python)/3
        if total_score>=50:
            result='success'
        else:
            result = 'fail'
    return redirect(url_for(result,score=total_score))
    #return redirect(url_for(result,score=score))



# result checker
if __name__=='__main__':
    app.run(debug=True)
