import wx

class Frame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self,None,-1,'1')
		panel=wx.Panel(self)
		panel.SetBackgroundColour('White')
		m=wx.MessageDialog(None,'1','1')
		a=m.ShowModal()
		print wx.ID_OK
		print a
		text=wx.TextEntryDialog(None,'1','1')
		if text.ShowModal()==wx.ID_OK:
			print text.GetValue()
		choice=wx.SingleChoiceDialog(None,'12','2',['1','12'])
		choice.ShowModal()
		print choice.GetStringSelection()
		#
		#self.Bind(wx.EVT_CLOSE,self.Destroy)

	
class App(wx.App):
	def OnInit(self):
		f=Frame()
		f.Show(True)
		return True


if __name__=='__main__':
	a=App()
	a.MainLoop()