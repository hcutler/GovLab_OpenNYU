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

# function must have a template name
def render():
	# data_file = open("data.yaml", 'r')
	# render_template('template.html', **data)
	# data_file.close()

	with open("data.yaml", 'r') as data_file:
		data = load(data_file, Loader=Loader)

	template = env.get_template("index.html")
	profile = template.render(data)

	with open("output/sample.html", 'w') as output_file:
		output_file.write(profile)

def copy_css():
	source = os.getcwd() + "/"
	dest = "/Users/hannahcutler/Documents/Dev/ENV/GovLab_OpenNYU/expert-net-mockup-1/output/"
	for basename in os.listdir(source):
		if basename.endswith(".css"):
			# delete existing .css file in new directory
			shutil.copy2(basename,dest)
			
			# # main.css -> main_output.css
			# for char in basename:
			# 	i = len(basename) - 4
			# 	oldbase = basename[0:i]
			# 	newbase = basename[0:i] + '_output'
			# 	newname = basename.replace(oldbase, newbase)
			# 	basename = newname






if __name__ == '__main__':
    render()
    copy_css()