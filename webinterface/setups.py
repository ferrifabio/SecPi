# web framework
import cherrypy


# our stuff
from tools.db import objects
from tools import config
from base_webpage import BaseWebPage



class SetupsPage(BaseWebPage):
	
	def __init__(self):
		super(SetupsPage, self).__init__(objects.Zone)
		self.fields['id'] = 'ID'
		self.fields['name'] = 'Name'
		self.fields['description'] = 'Description'
		self.fields['active'] = 'Active'


	@cherrypy.expose
	def index(self, flash_message=None):
		tmpl = self.lookup.get_template("setups.mako")
		return tmpl.render(page_title="Setups", flash_message=flash_message)




