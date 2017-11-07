import wx
class App(wx.App):
	def OnInit(self):
		frame=wx.Frame(parent=None,title='s')
		frame.Show()
		return Ture()

app=App()
app.MainLoop()