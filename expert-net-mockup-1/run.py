from flask import Flask, render_template, abort

app = Flask(__name__)

# establishing the route /, which renders the template 
# template.html via the function render_template()
@app.route("/")


# function must have a template name
def template_test():
    return render_template('template.html', my_string="Wheeeee!", my_list=[0,1,2,3,4,5])


if __name__ == '__main__':
    app.run(debug=True)