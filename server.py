from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)


@app.route('/')
def get_index():
    return render_template('index.html')


@app.route('/<string:page_name>')
def get_page(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'Did not save to db!'
    else:
        return 'something wrong'

# Using txt file
# def write_to_file(data):
#     with open('database.txt', mode='a') as db:
#         email = data['email']
#         subject = data['subject']
#         message = data['message']
#         file = db.write(
#             f'\nEmail: {email},\nSubject: {subject},\nMessage: {message}')


def write_to_csv(data):
    with open('db.csv', newline='', mode='a') as db:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(
            db, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])
