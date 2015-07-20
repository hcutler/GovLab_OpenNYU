

from jinja2 import Environment
env = Environment(loader=FileSystemLoader("templates"))

# create and render template
template = env.get_template("cv.html")
cv = template.render(entries=data, templates_folder="templates")