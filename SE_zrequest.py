import urllib.request
import threading

class ZRequest(threading.Thread):

	def __init__(self, url,  callback, headers={},meta={}):
		threading.Thread.__init__(self)
		self.url = url
		self.callback = callback
		self.headers = headers
		self.meta = meta

	def run(self):
		self.GET()

	def GET(self):
		request = urllib.request.Request(url=self.url, headers=self.headers)
		response = urllib.request.urlopen(request)
		self.callback(response, self.meta)
