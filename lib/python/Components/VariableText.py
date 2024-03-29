# -*- coding: utf-8 -*-
class VariableText:
	"""VariableText can be used for components which have a variable text, based on any widget with setText call"""

	def __init__(self):
		object.__init__(self)
		self.message = ""
		self.instance = None
		self.onChanged = []

	def setText(self, text):
		self.message = text
		if self.instance:
			self.instance.setText(str(self.message) or "")
		for x in self.onChanged:
			x()

	def setMarkedPos(self, pos):
		if self.instance:
			self.instance.setMarkedPos(int(pos))

	def getText(self):
		return self.message

	text = property(getText, setText)

	def postWidgetCreate(self, instance):
		instance.setText(str(self.message) or "")
