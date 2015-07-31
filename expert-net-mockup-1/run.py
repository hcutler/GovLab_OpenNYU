# -*- coding: utf-8 -*-

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

people_files = ['S. R. Srinivasa Varadhan.yaml', 'David W. Hogg.yaml', 'Juliana Freire.yaml','Roy Lowrance.yaml', 
'Rebecca Liebe.yaml', 'David Clark.yaml', 'Jennifer Hill.yaml', 'Mik Laver.yaml', 'Yann LeCun.yaml', 
'Foster Provost.yaml', 'Claudio Silva.yaml', 'Eero Simoncelli.yaml', 'David Sontag.yaml', 'Karen Adolph.yaml',
 'Constantin Aliferis.yaml', 'Neal Beck.yaml', 'Juan Bello.yaml',
'Michael Blanton.yaml', 'Jan Blustein.yaml', 'Richard Bonneau.yaml', 'Adam Brandenburger.yaml', 'David Cai.yaml', 
'Andrew Caplin.yaml', 'Xi Chen.yaml', 'Gloria Coruzzi.yaml', 'Kyle Cranmer.yaml', 'Nathaniel Daw.yaml',
'Vasant Dhar.yaml', 'Dustin T. Duncan.yaml', 'Rob Fergus.yaml', 'Halina Frydman.yaml',
'Judith D. Goldberg.yaml', 'Jonathan Goodman.yaml', 'Leslie Greengard.yaml', 'Sinan Gunturk.yaml', 
'Todd Gureckis.yaml', 'Peter Halpin.yaml', 'Daphna Harel.yaml', 'David Heeger.yaml',  
'Ming Hu.yaml', 'Clifford M. Hurvich.yaml', 'Panos Ipeirotis.yaml', 'Srikanth Jagabathula.yaml', 
'John Jost.yaml', 'Robert Kohn.yaml', 'Petter Kolm.yaml', 'Peter Lakner.yaml', 
'Jinyang Li.yaml', 'Mengling Liu.yaml', 'Alessandro Lizzeri.yaml', 'Ying Lu.yaml', 
'Andrew Majda.yaml', 'Suzanne McIntosh.yaml', 'Edward Melnick.yaml', 'Joel Middleton.yaml', 'Bud Mishra.yaml',
'Chuck Newman.yaml', 'Patrick Perry.yaml', 'Bijan Pesaran.yaml', 'Michael Purugganan.yaml', 'Keith Ross.yaml', 
'Marc Scott.yaml', 'Youngzhao Shao.yaml', 'Dennis Shasha.yaml', 'Jeff Simonoff.yaml',
'Alexander Statnikov.yaml', 'Lakshminarayanan Subramanian.yaml','Torsten Suel.yaml', 'Arun Sundararajan.yaml', 
'Esteban Tabak.yaml', 'Aaron Tennebein.yaml', 'Eric Vanden-Eijnden.yaml', 'Sharon Weinberg.yaml',
'Margaret Wright.yaml', 'Laura Noren.yaml', 'Brian McFee.yaml', 'Brenden Lake.yaml',
'Daniela Huppenkothen.yaml']
# 'andreas_muller.yaml']


# u'Gérard Ben Arous.yaml', 
# u'Rohit Deo.yaml', 
#  u'Steven Koonin.yaml',
#  u'John Leahy.yaml', 
#  u'Lisa Hellerstein.yaml',
#  u'Andreas Müller.yaml',

# pages = ['index', 'links']
people_list = "people-list.yaml"
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
		output_file.write(profile.encode('utf-8'))

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