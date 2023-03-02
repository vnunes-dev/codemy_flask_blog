from content import app
from flask import render_template
from content.forms import FormEntryName

# Create a route for HOME page: 
@app.route('/')
def home():
    return render_template('home.html')

# Create a route for USER page:
@app.route('/user/<name>')
def user(name):
    return render_template('user.html', user_name=name)

# Create a NAME page:
@app.route('/name', methods=['GET', 'POST'])
def name():
    name = None
    form = FormEntryName()
    # Validate form
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        
    return render_template('name.html', name=name, form=form)

#region  ----------------------  Create error pages  ---------------------------------------

# Invalid URL:
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Internal server error:
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
#endregion