# web framework
import cherrypy


# our stuff
from tools.db import objects
from tools import config
from base_webpage import BaseWebPage



class SensorsPage(BaseWebPage):
	
	def __init__(self):
		super(SensorsPage, self).__init__(objects.Sensor)
		self.fields['id'] = 'ID'
		self.fields['name'] = 'Name'
		self.fields['description'] = 'Description'
		self.fields['gpio_pin'] = 'GPIO Pin'
		self.fields['zone_id'] = 'Zone ID'


	@cherrypy.expose
	def index(self, flash_message=None):
		tmpl = self.lookup.get_template("sensors.mako")
		return tmpl.render(page_title="Sensors", flash_message=flash_message)




