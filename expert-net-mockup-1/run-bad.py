from yaml import load, Loader
# load entries yaml
data = load(open("expert-net-mockup-1/entries.yaml"), Loader=Loader)

########


#render content into html object
from jinja2 import Environment
env = Environment(loader=FileSystemLoader("templates"))

# create and render template
template = env.get_template("profile.html")
profile = template.render(entries=data, templates_folder="templates")

{% for e in entries if e.details %}
        # {{ e.details.address }}
        {{e.skills.skill1}}
{% endfor %} 


def get_data():
    return {
        "entries": load(open("data/entries.yaml"), Loader=Loader),
        # "projects": load(open("data/projects.yaml"), Loader=Loader)
    }

if __name__ == "__main__":
    output_folder = "out"

    # remove out
    shutil.rmtree(output_folder, ignore_errors=True)

    renderer = Renderer(outpath=output_folder, contexts=[("index.html", get_data)])
    renderer.run(debug=True, use_reloader=False)

    # copy static folder (css and images)
    shutil.copytree("static", output_folder + "/static")


# import os
# import shutil
# from jinja2 import Environment, FileSystemLoader
# import ho.pisa as pisa
# import StringIO
# from datetime import date
# from yaml import load, Loader


# def render_html_to_pdf(html, filename):
#     pisa.showLogging()
#     pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("UTF-8")), file(filename, "wb"))
#     if pdf.err:
#         print "Error: " + pdf.err


# if __name__ == "__main__":
#     # setup yaml reader
#     templates_folder = "../" + "templates" + "/"
#     env = Environment(loader=FileSystemLoader(templates_folder))

#     # load settings if available
#     settings = {}
#     if os.path.exists(templates_folder + "settings.yaml"):
#         settings = load(open(templates_folder + "settings.yaml"), Loader=Loader)

#     # load entries yaml
#     data = load(open(templates_folder + "data.yaml"), Loader=Loader)

#     # create and render template
#     profile_template = settings.get("profile_template", "profile.html")
#     template = env.get_template(cv_template)
#     cv = template.render(entries=data, templates_folder=templates_folder)

#     # output
#     output_folder = "../" + settings.get("output_folder", "out") + "/"

#     # clean output folder
#     shutil.rmtree(output_folder)
#     os.mkdir(output_folder)

#     # # create pdf
#     # date_format = settings.get("file_name", "cv-%Y.%m")
#     # title = date.today().strftime(date_format) + ".pdf"
#     # render_html_to_pdf(cv, output_folder + title)

#     # success
#     print title + " created."