import wx

class Frame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self,None,-1,'1',(300,200))
		panel=wx.Panel(self)
		panel.SetBackgroundColour('White')
		statusBar=self.CreateStatusBar()
		#toolBar=self.CreateToolBar()

		#toolBar.AddSimpleTool(wx.NewId(),wx.EmptyBitmap(1,1),'new','l')
		#toolBar.Realize()
		menuBar=wx.MenuBar()
		menu1=wx.Menu()
		menuBar.Append(menu1,'file')
		menu2=wx.Menu()
		menu2.Append(-1,'copy','copy')
		menu2.Append(-1,'cut','')
		menu2.AppendSeparator()
		menu2.Append(-1,'options','d')
		menuBar.Append(menu2,'edit')
		self.SetMenuBar(menuBar)

if __name__=='__main__':
	app=wx.PySimpleApp()
	frame=Frame()
	frame.Show(True)
	app.MainLoop()
