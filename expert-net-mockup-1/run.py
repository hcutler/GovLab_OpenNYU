from jinja2 import Environment, FileSystemLoader
from yaml import load, Loader
import shutil
import string

import os

env = Environment(loader=FileSystemLoader("templates"))

try:
	os.mkdir('output')
except OSError:
	pass

# def render_landing():
# 	with open("people-list-maker.py", 'r') as data_file:
# 		data = load(data_file, Loader=Loader)

# 	template = env.get_template("links.html")
# 	landing = template.render(data)

# 	with open("output/sample-landing.html", 'w') as output_file:
# 		output_file.write(landing)
people_files = ['David Clark.yaml','David W. Hogg.yaml','Foster Provost.yaml','Jennifer Hill.yaml','Juliana Freire.yaml','Mik Laver.yaml','Rebecca Liebe.yaml','Roy Lowrance.yaml','S. R. Srinivasa Varadhan.yaml','Torsten Suel.yaml','Yann LeCun.yaml']
# pages = ['index', 'links']
people_list = "people-list copy.yaml"

# function must have a template name
def render_profile(filename):
	# data_file = open("data.yaml", 'r')
	# render_template('template.html', **data)
	# data_file.close()

	# with open("data.yaml", 'r') as data_file:
	with open(filename, 'r') as data_file:		#not correct here!
		template_data = load(data_file, Loader=Loader)

		#-------------profile pages
		template = env.get_template("index.html")
		profile = template.render(template_data)
		output_name = filename.replace(".yaml","")


	with open("output/" + output_name + ".html", 'w') as output_file:
		output_file.write(profile.encode('utf8'))

def render_landing(filename):

	with open(filename, 'r') as data_file:		#not correct here!
		template_data = load(data_file, Loader=Loader)

		#-------------landing page
		landing = env.get_template("links.html")
		tblcontents = landing.render(template_data)
		output_name = "table-contents"


	with open("output/" + output_name + ".html", 'w') as output_file:
		output_file.write(tblcontents.encode('utf8'))

def copy_css():
	source = os.getcwd() + "/"
	dest = "/Users/Hannah-Cutler/Documents/Dev/GovLab_OpenNYU/expert-net-mockup-1/output/"
	for basename in os.listdir(source):
		if basename.endswith(".css"):
			# delete existing .css file in new directory
			shutil.copy2(basename,dest)

if __name__ == '__main__':

	render_landing(people_list)
	for p in people_files:
		render_profile(p)
	copy_css()
    # copy_links_file()


			# # main.css -> main_output.css
			# for char in basename:
			# 	i = len(basename) - 4
			# 	oldbase = basename[0:i]
			# 	newbase = basename[0:i] + '_output'
			# 	newname = basename.replace(oldbase, newbase)
			# 	basename = newname