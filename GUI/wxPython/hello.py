import wx

class Frame(wx.Frame):
	def __init__(self,image,parent=None,id=-1,pos=wx.DefaultPosition,size=(1000,1000),title='hello world'):
		temp=image.ConvertToBitmap()
		size=temp.GetWidth(),temp.GetHeight()
		wx.Frame.__init__(self,parent,id,title,pos,size)
		self.bmp=wx.StaticBitmap(parent=self,bitmap=temp)

class App(wx.App):
	def OnInit(self):
		image=wx.Image('1.png',wx.BITMAP_TYPE_PNG)
		self.frame=Frame(image)
		self.frame.Show(True)
		self.SetTopWindow(self.frame)
		return True

def main():
	app=App()
	app.MainLoop()

if __name__=='__main__':
	main()