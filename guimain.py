import wx
import guiinput
import guioutput
import guiimport

# Main Notebook
class MainNotebook(wx.Notebook):
    def __init__(self, parent):
        """
        Constructor
        """
        wx.Notebook.__init__(self, parent, id=wx.ID_ANY, style=wx.BK_DEFAULT)
 
        inputTab = guiinput.InputTab(self)
        outputTab = guioutput.OutputTab(self)
        importTab = guiimport.ImportTab(self)
 
        self.AddPage(inputTab, "Input")
        self.AddPage(outputTab, "Output")
        self.AddPage(importTab, "Import")
        
        self.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGED, self.OnPageChanged)
        self.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGING, self.OnPageChanging)
 
    def OnPageChanged(self, event):
        old = event.GetOldSelection()
        new = event.GetSelection()
        sel = self.GetSelection()
        event.Skip()
 
    def OnPageChanging(self, event):
        old = event.GetOldSelection()
        new = event.GetSelection()
        sel = self.GetSelection()
        event.Skip()
 
# The Main Window
class MainFrame(wx.Frame):
    
    def __init__(self):
        """
        Constructor
        """
        wx.Frame.__init__(self, None, wx.ID_ANY, "<Application Name>", size=(800,600))
        panel = wx.Panel(self)
 
        notebook = MainNotebook(panel)
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(notebook, 1, wx.ALL|wx.EXPAND, 5)
        panel.SetSizer(sizer)
        self.Layout()
 
        self.Show()

# Main 
if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = MainFrame()
    app.MainLoop()
