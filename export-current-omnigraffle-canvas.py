#!/usr/bin/env python

# Exports a current omnigraffle canvas into a file.
#
# A file `.<DocumentName>.omnigraffle_export` placed next to the
# `<DocumentName>.omnigraffle`, can contain a directory relative to the document
# directory where the exports should be saved. If no such a file is found it
# will always prompt for a location.

import os
import sys
import omnigraffle_export.omnigraffle as omnigraffle

from AppKit import NSURL, NSApplication, NSAutoreleasePool, NSApp, NSSavePanel, NSFileHandlingPanelOKButton
import objc

log = None

def log_growl(msg):
	import gntp.notifier
	try:
		gntp.notifier.mini(description=msg, applicationName='OmniGraffle', title='OmniGraffe Export')
	except Exception:
		log_std(msg)

def log_std(msg):
	from AppKit import NSAlert, NSInformationalAlertStyle, NSRunningApplication, NSApplicationActivateIgnoringOtherApps

	# initialize
	# tip from: http://graphicsnotes.blogspot.fr/2010/01/programmatically-creating-window-in-mac.html
	NSApplication.sharedApplication()
	NSRunningApplication.currentApplication().activateWithOptions_(NSApplicationActivateIgnoringOtherApps);

	alert = NSAlert.alloc().init()
	alert.autorelease()
	alert.setAlertStyle_(NSInformationalAlertStyle)
	alert.setMessageText_(msg)
	alert.runModal()

try:
	# using Growl to notify about the results
	# requires gntp
	# install using pip install gntp
	import gntp.notifier
	log = log_growl
except Exception:
	# otherwise notify using 
	log = log_std

og = omnigraffle.OmniGraffle()
schema = og.active_document()
if schema == None:
	sys.exit(0)

schema_path = schema.path
if schema_path == None:
	schema_path = "Untitled"

schema_fname = os.path.basename(schema_path)
schema_dir = os.path.dirname(schema_path)

target_path = None
format = 'pdf'
canvas_name = schema.active_canvas_name()

# Try to look for a file .<DocumentName>.omnigraffle_export
export_info_fname = "Untitled"
if schema_fname.rfind('.') != -1:
  os.path.join(schema_dir, '.' + schema_fname[0:schema_fname.rindex('.')] + '.omnigraffle_export')

if os.path.exists(export_info_fname):
	# if it exists it should contain one line that gives a relative path to a
	# directory where to export
	with open(export_info_fname) as f:
		target_dir = f.read().strip()
	target_dir = os.path.join(schema_dir, target_dir)
	target_dir = os.path.normpath(target_dir)
	target_path = os.path.join(target_dir, canvas_name + '.' + format)
else:
	# otherwise ask for a path
	savePanel = NSSavePanel.savePanel()
	savePanel.setTitle_("Save %s as" % canvas_name)
	savePanel.setDirectoryURL_(NSURL.fileURLWithPath_(schema_dir))
	savePanel.setCanCreateDirectories_(True)
	savePanel.setExtensionHidden_(False)
	savePanel.setNameFieldStringValue_(canvas_name+'.pdf')
	NSApplication.sharedApplication().activateIgnoringOtherApps_(True);

	if savePanel.runModal() == NSFileHandlingPanelOKButton:
	    target_path = savePanel.URL().path()
	    format = target_path[target_path.rindex('.')+1:]

if not target_path:
	sys.exit(0)

try:
	schema.export(canvas_name, target_path, format=format)
	log("Exported %s to: %s as: %s" % (canvas_name, target_path, format))
except Exception as e:
	log("Unable to export: %s to %s. %s" % (canvas_name, target_path, e.message))

NSApplication.sharedApplication().terminate_(None)
