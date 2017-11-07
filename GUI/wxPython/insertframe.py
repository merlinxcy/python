import wx

class InsertFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self,None,-1,'frame with button',size=(300,100))
		panel=wx.Panel(self)#hua ban
		button=wx.Button(panel,label='close',pos=(125,10),size=(50,50))
		self.Bind(wx.EVT_BUTTON,self.OnCloseMe,button)
		self.Bind(wx.EVT_CLOSE,self.OnCloseWindow)

	def OnCloseMe(self,event):
		self.Close(True)

	def OnCloseWindow(self,event):
		self.Destroy()

if __name__=='__main__':
	app=wx.PySimpleApp()
	frame=InsertFrame()
	frame.Show(True)
	app.MainLoop()
