from flask import Flask, render_template, request, redirect, url_for
import pandas as pd

raw = pd.read_csv("Engineering.csv")
data = {}
for i in range(len(raw)):
    data[i + 1] = raw.iloc[i].to_dict()

app = Flask(__name__)

results = {}

@app.route('/', methods=['GET', 'POST'])
def index():
    global results  # Declare results as a global variable to modify it
    if request.method == 'POST':
        user_id = int(request.form['user_id'])
        mobile = request.form['mobile']
        return redirect(url_for('details', id=user_id, mobile=mobile))
    return render_template('index.html')

@app.route('/details/<int:id>/<mobile>', methods=['GET', 'POST'])
def details(id, mobile):
    global results  # Declare results as a global variable to modify it
    user_details = data.get(id)
    if user_details is None:
        return "User not found."
    
    if mobile != user_details['phone_number']:
        return "Invalid mobile number"
    
    if request.method == 'POST':
        results[id] = "Registered"
        # Write to CSV inside the POST method
        results_df = pd.DataFrame(results.items(), columns=['id', 'status'])
        results_df.to_csv("results.csv", mode='a',index=False,header=False)
        return redirect(url_for('thank', name=user_details['student_name']))
    
    return render_template('details.html', user=user_details)

@app.route('/thank/<name>')
def thank(name):
    return render_template('thank.html', username=name)

if __name__ == '__main__':
    app.run(debug=True)
