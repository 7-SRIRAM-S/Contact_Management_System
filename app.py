from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)



# This dictionary will store our contacts
contacts = {}


@app.route('/')
def index():
    return render_template('index.html', contacts=contacts)





@app.route('/add', methods=['GET', 'POST'])
def add_contact():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']
        city = request.form['city']

        # Add the contact to the contacts dictionary
        contacts[name] = {'phone': phone, 'email': email, 'city': city}

        return redirect(url_for('index'))
    return render_template('add_contact.html')


@app.route('/delete/<contact_name>')
def delete_contact(contact_name):
    if contact_name in contacts:
        del contacts[contact_name]

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)