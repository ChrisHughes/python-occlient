#! /usr/bin/env python
# deps for building
# scons gettext build-essential swig python-dev libpng12-dev libglib2.0-dev 
import pygtk
pygtk.require('2.0')
import gtk, gobject, os, sys, time, math, array
sys.path.append('/home/qb89dragon/Desktop/lib')

# MyPaint Elements
from brush import Brush, BrushInfo
from tiledsurface import Surface
from document import Document
from stroke import Stroke
from tileddrawwidget import TiledDrawWidget
import command

# Libraries used internally
import struct as st
import array as ar
import numpy as np

# Import Twisted Networking Elements
from twisted.internet import glib2reactor
glib2reactor.install()
from twisted.internet import reactor, protocol
from twisted.internet.endpoints import TCP4ClientEndpoint


brushdata = """version 2
opaque 1.00 | pressure (0.000000 -0.989583), (0.382530 -0.593750), (0.656627 0.041667), (1.000000 1.000000)
opaque_multiply 0.0 | pressure (0.000000 0.000000), (0.015000 0.000000), (0.069277 0.937500), (0.250000 1.000000), (1.000000 1.000000)
opaque_linearize 0.29
radius_logarithmic 0.92 | pressure (0.000000 -0.787500), (0.237952 -0.600000), (0.500000 -0.150000), (0.765060 0.600000), (1.000000 0.900000)
hardness 0.95
"""



class OC11NetworkProtocol(protocol.Protocol,gobject.GObject):
	__gsignals__ = {"canvas-ready"	: (gobject.SIGNAL_RUN_FIRST, gobject.TYPE_NONE, [gobject.TYPE_INT, gobject.TYPE_INT]),
					"update-users"	: (gobject.SIGNAL_RUN_FIRST, gobject.TYPE_NONE, ()),
					"ready"	: (gobject.SIGNAL_RUN_FIRST, gobject.TYPE_NONE, ()),
					"clear-layer"	: (gobject.SIGNAL_RUN_FIRST, gobject.TYPE_NONE, [gobject.TYPE_INT]),
					"undo-request"	: (gobject.SIGNAL_RUN_FIRST, gobject.TYPE_NONE, [gobject.TYPE_INT]),
					"draw"	: (gobject.SIGNAL_RUN_FIRST, gobject.TYPE_NONE, [gobject.TYPE_INT, gobject.TYPE_PYOBJECT, gobject.TYPE_PYOBJECT]),
					"message" : (gobject.SIGNAL_RUN_FIRST, gobject.TYPE_NONE, [gobject.TYPE_INT, gobject.TYPE_STRING])}

	def __init__(self, username, password):
		gobject.GObject.__init__(self)
		self.handshake_sent = False
		self.user_list = []
		self.canvas_size = [0,0]
		self.layer_count = 0
		self.total_layer_count = 0
		self.uid = None;
		self.username = username
		self.password = password
		self.handshake = ''.join(["\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x20\x00\x00\x00"] + [self.username] + ['\x00'] * (16 - len(self.username)) + [self.password] + ['\x00'] * (16 - len(self.password)))

	def connectionMade(self):
		self.local_host = self.transport.getHost().host
		self.remote_host = self.transport.getPeer().host
		self.port = self.transport.getHost().port
				
	def dataReceived(self, data):
		# Send data at points in the connection process
		if not self.handshake_sent:
			print "Sent handshake"
			self.transport.write(self.handshake)
			self.handshake_sent = True
		
		# Parse incoming messages by type
		message_type = st.unpack_from("<B", data, 0)[0]
		print "Message Type", message_type
		if message_type == 0:
			# Canvas properties / drawing
			data_length = st.unpack_from("<B", data, 12)[0]
			function = st.unpack_from("<H", data, 16)[0]
			print "Type zero function call ", function
			if function == 10007:
				# Canvas Properties
				x = st.unpack_from("<I", data, 56)[0]
				y = st.unpack_from("<I", data, 76)[0]
				self.canvas_size = [x,y]
				self.layer_count = st.unpack_from("<I", data, 116)[0]
				self.total_layer_count = self.layer_count * len(self.user_list)	# This is wrong
				self.emit('ready')
			elif function == 292:
				# Erase layer
				layer_number = st.unpack_from("<B", data, 18)[0]
				self.emit('clear-layer', layer_number)
			elif function == 272:
				# Undo last action from user
				user = st.unpack_from("<B", data, 4)[0]
				layer_number = st.unpack_from("<B", data, 18)[0]
				self.emit('undo-request', layer_number)
			elif function == 0:
				# Pixel setting
				pixel_data = data[35:]

				layer_number = st.unpack_from("<B", data, 18)[0]
				brush = {'size':float(st.unpack_from("<B", data, 25)[0]) / 256 + st.unpack_from("<B", data, 26)[0],
						 'color':st.unpack_from("<BBB", data, 19),
						 'pressure_correct':float(st.unpack_from("<B", data, 27)[0]) / 255 + st.unpack_from("<B", data, 28)[0]}
				 
				points = []
				for stroke in range((len(pixel_data) - 2) / 6):
					if stroke == 0:
						subdata = pixel_data[0:8]
						print 'unk pt byte 2', st.unpack_from("<B", subdata, 5)
					else:
						subdata = pixel_data[stroke*6+2:stroke*6+8]
					points.append(st.unpack_from("<hhH", subdata, 0))
				self.emit('draw', layer_number, brush, points)
		elif message_type == 1:
			# Initial connection
			pass
		elif message_type == 4:
			# Status update
			
			# Get user list (always included)
			usr_data = map(lambda s: s.replace('\x00', ''), [data[16+i*16:32+i*16] for i in range(16)])
			usr_data = zip(usr_data[0::2], usr_data[1::2], range(8))
			usr_data = filter(lambda t: t[0]!='' or t[1]!='', usr_data)
			self.user_list = usr_data
			for user in self.user_list:
				if user[0] == self.username and user[1] == self.local_host:
					self.uid = user[2]
			self.total_layer_count = self.layer_count * len(self.user_list)
			self.emit('update-users')
			#self.canvas_size = st.unpack_from("<QQQQ", data, 328)
			#print self.canvas_size
		elif message_type == 5:
			# Chat message
			uid = ord(data[4])
			print uid
			message = data[16:].replace('\x00', '')
			self.emit('message', uid, message)
	
	def send_strokes(self, layer_number, brush_settings, points):
		message = array.array('c', ['\x00'] * 19)
		st.pack_into('<B', message, 2, layer_number)
		st.pack_into('<B', message, 3, 166)
		st.pack_into('<B', message, 4, 115)
		st.pack_into('<B', message, 5, 149)
		st.pack_into('<B', message, 6, 1)
		st.pack_into('<B', message, 8, 95)
		st.pack_into('<B', message, 10, 12)
		st.pack_into('<B', message, 11, 93)
		st.pack_into('<B', message, 12, 11)
		first_message = True
		for point in points:
			pressure = point[2]
			if pressure == 0: pressure = 4
			message.extend(array.array('c', st.pack('<hh', point[0], point[1]) + st.pack('<H', pressure)))
			if first_message:
				first_message = False
				message.extend(array.array('c', ['\x00', '\x04']))
		self.uid = 0
		data = st.pack('<I', 0) + st.pack('<I', self.uid) + '\xFF\xFF\xFF\xFF' + st.pack('<I', len(message)) + message.tostring()
		print map(ord, data);
		self.transport.write(data)
			
	def send_chat_message(self, message):
		data = st.pack('<I', 5) + st.pack('<I', self.uid) + '\xFF\xFF\xFF\xFF' + st.pack('<I', len(message)) + message
		self.transport.write(data)
	
	def disconnect(self):
		self.transport.loseConnection()

class OCCanvas(Document):
	def __init__(self, canvas_size, layers):
		default_brush_style = BrushInfo(brushdata)
		Document.__init__(self, default_brush_style)
		self.canvas_size = canvas_size
		self.layer_count = layers
		
		tile_size = (canvas_size[0] + 64 - (canvas_size[0] % 64), canvas_size[1] + 64 - (canvas_size[1] % 64))
		self.set_frame(0, 0, *tile_size)
		
		for layer in range(layers):
			self.add_layer(layer)
			
	def clear_layer(self, layer):
		self.select_layer(layer)
		layer = self.get_current_layer()
		layer.clear()
	
	def undo_layer_action(self, layer):
		# Undo handler
		# FixMe: Cap local buffer to match OC
		self.split_stroke()
		if not self.command_stack.undo_stack: return
        
		previous_stroke_command = None
		for command_instance in reversed(self.command_stack.undo_stack):
			if isinstance(command_instance, command.Stroke):
				previous_stroke_command = command_instance
			elif isinstance(command_instance, command.SelectLayer):
				if command_instance.idx == layer:
					if previous_stroke_command:
						# Last event on layer found, undo it
						for f in self.command_stack.call_before_action: f()
						self.command_stack.undo_stack.remove(previous_stroke_command)
						self.select_layer(layer)
						previous_stroke_command.undo()
						self.command_stack.redo_stack.append(previous_stroke_command)
						self.command_stack.notify_stack_observers()
						break        					
	
	def draw_points(self, layer_number, style, points):
		# Corrective constants to match characteristics of OpenCanvas 1.1 brushes
		pressure_correction_weight = 1.0
		brush_size_weight = 0.7
		brush_velocity = 0.03
		
		print "Drawing on layer ", layer_number
		self.select_layer(layer_number)
		
		layer = self.get_current_layer()

		brush_style = BrushInfo(brushdata)

		# Set color
		rgb = map(lambda c: float(c) / 255.0, style['color'])
		brush_style.set_color_rgb(rgb)

		# Set size adjustments and calculate pressure curve
		size = style['size']
		pressure_correct = style['pressure_correct']
		x_points = (0.000000, 0.237952, 0.500000, 0.765060, 1.000000)
		y_points = map(lambda x: (x**pressure_correct) * pressure_correction_weight - pressure_correction_weight / 2.0, x_points)
		pressure_curve = zip(x_points, y_points)
		brush_style.set_setting('radius_logarithmic', [math.log(size*brush_size_weight), {'pressure': pressure_curve}])

		brush = Brush(brush_style)
		
		stroke = Stroke()
		stroke.start_recording(brush)
		tdelta = 0
		lx, ly, lp = points[0]
		for point in points:
			lx = (lx + point[0]) / 2
			ly = (ly + point[1]) / 2
			lp = float(point[2]) / 1024.0	# Pressure
			stroke.record_event(tdelta, lx, ly, lp, 0, 0)
			tdelta += brush_velocity
		stroke.stop_recording()
		
		# Render stroke and save undo information
		snapshot_before = layer.save_snapshot()
		stroke.render(layer._surface)
		self.do(command.Stroke(self, stroke, snapshot_before))
        
		
class DrawGUI:
	remote_host = "127.0.0.1"
	remote_port = 9001
	canvas = None
	
	def __init__(self):
		self.netobj = None
		self.build_gui()
		self.connect()
	
	def connect(self):
		# Do connection
		factory = self.ClientFactory(self.on_connect, "Python OC", "")

		reactor.connectTCP(self.remote_host, self.remote_port, factory)			
		reactor.run()

	def on_connect(self, netobj):
		self.netobj = netobj
		self.netobj.connect('update-users', self.on_userlist_change)
		self.netobj.connect('ready', self.build_canvas)
		self.netobj.connect('message', self.on_message)

	def send_chat_message(self):
		tb = self.wTree.get_object('chat_typing_area')
		message = tb.get_text()
		tb.set_text('')
		tb.grab_focus()
		if self.netobj:
			self.netobj.send_chat_message(message)
			cb = self.wTree.get_object("chat_text_buffer")
			cb.insert(cb.get_end_iter(), '['+self.netobj.username+'] '+message+"\n")

	def build_gui(self):
		self.wTree = gtk.Builder()
		self.wTree.add_from_file("oc.glade")
		self.wTree.get_object("main_window").connect('destroy', lambda a: sys.exit())
		self.wTree.get_object("chat_send_button").connect('clicked', lambda w:self.send_chat_message())
		self.wTree.get_object("main_window").show_all()
		self.update_input_devices()

	def build_canvas(self, e):
		self.document = OCCanvas(self.netobj.canvas_size, self.netobj.total_layer_count)
		self.canvas = TiledDrawWidget(document = self.document)

		self.wTree.get_object("drawingviewport").add(self.canvas)
		# Connect network -> local_viewport
		self.netobj.connect('draw', lambda e,l,b,p: self.document.draw_points(l,b,p))
		self.netobj.connect('clear-layer', lambda e,l: self.document.clear_layer(l))
		self.netobj.connect('undo-request', lambda e,l: self.document.undo_layer_action(l))
		
		# Connect local_viewport -> network
		self.document.stroke_observers.append(self.on_stroke)
		self.canvas.show()

	def on_stroke(self, stroke, brush):
		points = []
		brush_settings = {
			'size': 1,
			'color': 0,
			'pressure_correct': 1.0
			}
		layer_number = 3
		
		version, data = stroke.stroke_data[0], stroke.stroke_data[1:]
		assert version == '2'
		data = np.fromstring(data, dtype='float64')
		data.shape = (len(data)/6, 6)

		lx, ly = data[0][1:3]
		for dtime, x, y, pressure, xtilt, ytilt in data[1:]:
			ox = 2 * x - lx
			oy = 2 * y - ly
			points.append([ox, oy, pressure * 1024.0])

		self.netobj.send_strokes(layer_number, brush_settings, points)

	def on_userlist_change(self, e):
		ls = self.wTree.get_object("user_list").get_model()
		ls.clear()
		[ls.append([user[0]]) for user in self.netobj.user_list]
		
	def on_message(self, e, uid, message):
		name = filter(lambda u: u[2]==uid,self.netobj.user_list)[0][0]
		cb = self.wTree.get_object("chat_text_buffer")
		cb.insert(cb.get_end_iter(), '['+name+'] '+message+"\n")

	def update_input_devices(self):
		# init extended input devices
		self.pressure_devices = []
		for device in gtk.gdk.devices_list():
			#print device.name, device.source

			#if device.source in [gdk.SOURCE_PEN, gdk.SOURCE_ERASER]:
			# The above contition is True sometimes for a normal USB
			# Mouse. https://gna.org/bugs/?11215
			# In fact, GTK also just guesses this value from device.name.

			last_word = device.name.split()[-1].lower()
			if last_word == 'pad':
				# Setting the intuos3 pad into "screen mode" causes
				# glitches when you press a pad-button in mid-stroke,
				# and it's not a pointer device anyway. But it reports
				# axes almost identical to the pen and eraser.
				#
				# device.name is usually something like "wacom intuos3 6x8 pad" or just "pad"
				print 'Ignoring "%s" (probably wacom keypad device)' % device.name
				continue
			if last_word == 'touchpad':
				# eg. "SynPS/2 Synaptics TouchPad"
				# Cannot paint at all, cannot select brushes, if we enable this one.
				print 'Ignoring "%s" (probably laptop touchpad which screws up gtk+ if enabled)' % device.name
				continue
			if last_word == 'cursor':
				# this is a "normal" mouse and does not work in screen mode
				print 'Ignoring "%s" (probably wacom mouse device)' % device.name
				continue

			for use, val_min, val_max in device.axes:
				# Some mice have a third "pressure" axis, but without
				# minimum or maximum. https://gna.org/bugs/?14029
				if use == gtk.gdk.AXIS_PRESSURE and val_min != val_max:
					if 'mouse' in device.name.lower():
						# Real fix for the above bug https://gna.org/bugs/?14029
						print 'Ignoring "%s" (probably a mouse, but it reports extra axes)' % device.name
						continue

					self.pressure_devices.append(device.name)
					modesetting = 'screen'
					mode = getattr(gtk.gdk, 'MODE_' + modesetting.upper())
					if device.mode != mode:
						print 'Setting %s mode for "%s"' % (modesetting, device.name)
						device.set_mode(mode)
					break


	class ClientFactory(protocol.ClientFactory):
		protocol = OC11NetworkProtocol

		def __init__(self, on_create, *args, **kwargs):
			self.args = args
			self.kwargs = kwargs
			self.on_create = on_create # Callback for factory creation

		def buildProtocol(self, address):
			p = self.protocol(*self.args, **self.kwargs)
			p.factory = self
			if self.on_create: self.on_create(p)
			return p

		def clientConnectionFailed(self, connector, reason):
			print "Connection failed, disconnecting."
			reactor.stop()
		
		def clientConnectionLost(self, connector, reason):
			print "Connection lost."
			reactor.stop()

if __name__ == '__main__':
	DrawGUI()
