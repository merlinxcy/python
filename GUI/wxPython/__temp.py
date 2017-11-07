#Step 1
'''
import wx
class Frame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self,None,-1,"123",size=(1000,100))

	def OnMove(self,Event):
		pass

if __name__=='__main__':
	a=wx.PySimpleApp()
	frame=Frame()
	frame.Show(True)
	a.MainLoop()
'''

#Step 2
'''
import wx
class Frame(wx.Frame):
	pass

class App(wx.App):
	def OnInit(self):
		frame=Frame(None,-1)
		frame.Show(True)
		return True

if __name__=='__main__':
	a=App()
	a.MainLoop()
'''

