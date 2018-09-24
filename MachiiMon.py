import sublime
import sublime_plugin
import os
	
#Form a dictionary of all mach-ii*.xml files
machiiDict = []
scanDir = [i for i in os.walk(sublime.windows()[0].folders()[0])]
for allFiles in scanDir:
	for file in allFiles[2]:
		if 'mach' in file and 'xml' in file and 'coldspring' not in file:
			machiiDict.append(allFiles)
class MachiimonitorCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.insert(edit, 0, "\n")


class MachiimonitorEventListener(sublime_plugin.EventListener):
	def on_post_save(self , view):
		locateMachii = 0
		#Locate if mach-ii.xml is open in any views
		for windowViews in sublime.windows():	
			for indvidualView in windowViews.views():
				if "mach-ii" in indvidualView.file_name() and indvidualView.id() != view.id():
					indvidualView.run_command('machiimonitor')
					# print(view.file_name())
					indvidualView.run_command('save')
					locateMachii = 1	

		if not locateMachii:
			print(view.file_name())
			print(machiiDict)


