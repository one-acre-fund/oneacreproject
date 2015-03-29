import wx
import guidefault

# Input Tab
class InputTab(guidefault.DefaultTab):
    def __init__(self, parent):
        guidefault.DefaultTab.__init__(self, parent)
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        
        title = wx.StaticText(self, wx.ID_ANY, "Input")
        titleFont = wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        title.SetFont(titleFont)
        
        descriptionSizer = wx.BoxSizer(wx.HORIZONTAL)
        description = guidefault.AutoWrapStaticText(self, wx.ID_ANY,
                "Use this load and change saved input data, and press \"Solve\"" 
                " when you are ready. Output will be displayed in the \"Output\" tab.")
        #description =  wx.StaticText(self, wx.ID_ANY, "Blah very long text blah blah blah blahkdsfklsajf dkjflsa")
        #description.Wrap(200)

        mainSizer.Add(title, 0, wx.CENTER, 5)
        mainSizer.Add(descriptionSizer, 0, wx.ALL, 5)
        mainSizer.Add(wx.StaticLine(self), 0, wx.ALL|wx.EXPAND, 5)

        self.SetSizer(mainSizer)
