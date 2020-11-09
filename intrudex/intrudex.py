# -*- coding: UTF-8 -*-

# Standard imports
from burp import IBurpExtender, ITab, IContextMenuFactory
from java.util import ArrayList
from jarray import array
import re

# UI stuff
from javax.swing import JPanel, JButton, JScrollPane, JTextArea, JTextField, JMenuItem
from java.awt import Dimension, GridBagConstraints, GridBagLayout

# DEBUG for https://github.com/securityMB/burp-exceptions
#from exceptions_fix import FixBurpExceptions # DEBUG
#import sys # DEBUG

class BurpExtender(IBurpExtender, ITab, IContextMenuFactory):
	def registerExtenderCallbacks(self, callbacks):
		self._callbacks = callbacks
		self._helpers = callbacks.getHelpers()
		#sys.stdout = callbacks.getStdout() # DEBUG
		callbacks.setExtensionName('IntRudeX')
		callbacks.addSuiteTab(self)
		callbacks.registerContextMenuFactory(self)
		return
	
	def createMenuItems(self, inv):
		def clicked(self):
			print("Clicked")
		if (inv.getInvocationContext() == inv.CONTEXT_MESSAGE_VIEWER_REQUEST):
			menuItems = ArrayList()
			menuItem = JMenuItem("Send to IntRudeX", actionPerformed=clicked)
			menuItems.add(menuItem)
			return menuItems
		return None

	def getTabCaption(self):
		return "IntRudeX"

	def getUiComponent(self):
		#
		# Button functions
		#
		
		# Apply regex and preview
		def regexify(event):
			withSect = re.sub(regexBox.getText(), lambda m: unichr(167) + m.group(0) + unichr(167), contentBox.getText(), flags = re.M)
			resultsBox.setText(withSect)
			resultsBox.requestFocusInWindow()
			return

		# Actually send to Intruder
		def sendToIntruder(event):
			# TODO Parse host, port, and SSL
			offsets = ArrayList()
			p = re.compile(regexBox.getText())
			for m in p.finditer(contentBox.getText()):
				offsets.add(array((m.start(), m.end()), 'i'))
			self._callbacks.sendToIntruder("www.example.com", 80, False, contentBox.getText(), offsets)
			return
			

		# HTML body box
		body = """POST /example?p1=p1val&p2=p2val HTTP/1.0
Cookie: c=cval
Content-Length: 17

p3=p3val&p4=p4val&asdf=1234&qwer=123

<b>test</b>

<xml body:something tag='asdf'>
</xml>

&sect;"""
		# HTTP request box
		contentBox = JTextArea(body, 10, 80)
		contentBoxScroll = JScrollPane(contentBox)

		# Regex box
		regexBox = JTextField("[0-9]{3}", 40)

		# Buttons
		btnRegexify = JButton("Regexify", actionPerformed=regexify)
		btnSendToIntruder = JButton("Send to Intruder", actionPerformed=sendToIntruder)

		# Results box
		resultsBox = JTextArea("Results will be shown here", 10, 80)
		resultsBoxScroll = JScrollPane(resultsBox)        

		# Main panel
		mainPanel = JPanel(GridBagLayout())
		gbc = GridBagConstraints()
		gbc.gridx = 0
		gbc.gridy = 0
		gbc.weightx = 0.8
		contentBoxScroll.setPreferredSize(Dimension(1000, 300))
		mainPanel.add(contentBoxScroll, gbc)
		gbc.gridx = 1
		gbc.gridy = 0
		gbc.weightx = 0.1
		mainPanel.add(regexBox, gbc)
		gbc.gridx = 1
		gbc.gridy = 1
		gbc.weightx = 0.1
		mainPanel.add(btnRegexify, gbc)
		gbc.gridx = 1
		gbc.gridy = 3
		gbc.weightx = 0.1
		mainPanel.add(btnSendToIntruder, gbc)
		gbc.gridx = 0
		gbc.gridy = 2
		gbc.weightx = 1
		gbc.weighty = 1
		resultsBoxScroll.setPreferredSize(Dimension(1000, 300))
		mainPanel.add(resultsBoxScroll, gbc)

		return mainPanel

#FixBurpExceptions() # DEBUG
