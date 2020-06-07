from flask import render_template
import config

# Get the application instance
connex_app = config.connex_app

# Read the swagger.yml file to configure the endpoints
connex_app.add_api("swagger.yml")


@connex_app.route('/')
def home():
    return render_template('home.html')


@connex_app.route('/create')
def create():
    return render_template('create.html')


@connex_app.route('/update')
def update():
    return render_template('update.html')


@connex_app.route('/delete')
def delete():
    return render_template('delete.html')



if __name__ == '__main__':
    connex_app.run(host='127.0.0.1', port=5000, debug=True)