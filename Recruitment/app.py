from flask import Flask, render_template, request, redirect, url_for
import pandas as pd

raw = pd.read_csv("Engineering.csv")
codes = pd.read_csv("Empolyer_preprocessed.csv")
data = {}
results ={}
for i in range(len(raw)):
    data[i + 1] = raw.iloc[i].to_dict()

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_id = int(request.form['user_id'])
        code = request.form['code']
        return redirect(url_for('details', id=user_id, code=code))
    return render_template('index.html')
@app.route('/details/<int:id>/<code>', methods=['GET', 'POST'])
def details(id, code):
    user_details = data.get(id)
    if user_details is None:
        return "User not found."
    for i in range(len(codes['id'])):
        if(str(codes['id'][i])==code):
            name = codes['name'][i] 
    results[id]={name,request.form['role'],request.form['role_type']}
    results_df = pd.DataFrame(results.items(), columns=['Company name', 'Role','Package'])
    results_df.to_csv("results.csv", mode='a',index=False,header=False)
    if request.method == 'POST': 
        return redirect(url_for('thank', name=user_details['student_name']))
    
    return render_template('details.html', user=user_details,company_name=name)

@app.route('/thank/<name>')
def thank(name):
    return render_template('thank.html', username=name)

if __name__ == '__main__':
    app.run(debug=True)
