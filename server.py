from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        fullname = data['fullname']
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{fullname},{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv', mode='a', newline='\n') as database2:
        fullname = data['fullname']
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([fullname, email, subject, message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        # data_name = request.form['fullname']
        # data_email = request.form['email']
        # data_subject = request.form['subject']
        # data_message = request.form['message']
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return 'something went wrong. Try again!'

# @app.route('/index.html')
# @app.route('/')
# def my_home():
#     return render_template('index.html')

# @app.route('/about.html')
# def about():
#     return render_template('about.html')

# @app.route('/pricing.html')
# def pricing():
#     return render_template('pricing.html')

# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')
