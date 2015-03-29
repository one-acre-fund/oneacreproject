import guidefault

# Import Tab
class ImportTab(guidefault.DefaultTab):
    def __init__(self):
        guidefault.DefaultTab.__init__(self)
#        mainSizer = wx.BoxSizer(wx.VERTICAL)
#        
#        title = wx.StaticText(self, wx.ID_ANY, "Import")
#        titleFont = wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.BOLD)
#        title.SetFont(titleFont)
#
#        description = wx.StaticText(self, wx.ID_ANY,
#                "Use this to import input data not already saved into the application.")
#
#        districtSizer = wx.BoxSizer(wx.HORIZONTAL)
#        districtLabel = wx.StaticText(self, wx.ID_ANY, "District:")
#        districtText = wx.TextCtrl(self, wx.ID_ANY, "")
#        districtSizer.Add(districtLabel, 0, wx.ALL, 5)
#        districtSizer.Add((0,0), 1, wx.EXPAND)
#        districtSizer.Add(districtText, 0, wx.ALL, 5)
#
#        warehouseSizer = wx.BoxSizer(wx.HORIZONTAL)
#        warehouseLabel = wx.StaticText(self, wx.ID_ANY, "Warehouse:")
#        warehouseText = wx.TextCtrl(self, wx.ID_ANY, '')
#        warehouseSizer.Add(warehouseLabel, 0, wx.ALL, 5)
#        warehouseSizer.Add((0,0), 1, wx.EXPAND)
#        warehouseSizer.Add(warehouseText, 0, wx.ALL|wx.EXPAND, 5)
#        
#        destinationSizer = wx.BoxSizer(wx.HORIZONTAL)
#        destinationLabel = wx.StaticText(self, wx.ID_ANY, "Destinations/Truck:")
#        destinationText = wx.TextCtrl(self, wx.ID_ANY, '')
#        destinationSizer.Add(destinationLabel, 0, wx.ALL, 5)
#        destinationSizer.Add((0,0), 1, wx.EXPAND)
#        destinationSizer.Add(destinationText, 0, wx.ALL|wx.EXPAND, 5)
#        
#        maxSizer = wx.BoxSizer(wx.HORIZONTAL)
#        maxLabel = wx.StaticText(self, wx.ID_ANY, "Max Trucks/Warehouse/Day:")
#        maxText = wx.TextCtrl(self, wx.ID_ANY, '')
#        maxSizer.Add(maxLabel, 0, wx.ALL, 5)
#        maxSizer.Add((0,0), 1, wx.EXPAND)
#        maxSizer.Add(maxText, 0, wx.ALL|wx.EXPAND, 5)
#        
#        distanceSizer = wx.BoxSizer(wx.HORIZONTAL)
#        upDistanceButton = wx.Button(self, wx.ID_ANY, "Upload Distance Matrix", size=(200,-1))
#        viewDistanceButton = wx.Button(self, wx.ID_ANY, "View")
#        distanceLabel = wx.StaticText(self, wx.ID_ANY, "None uploaded.")
#        distanceSizer.Add(upDistanceButton, 0, wx.ALL, 5)
#        distanceSizer.Add(viewDistanceButton, 0, wx.ALL, 5)
#        distanceSizer.Add((0,0), 1, wx.EXPAND)
#        distanceSizer.Add(distanceLabel, 0, wx.ALL, 5)
#        
#        weightSizer = wx.BoxSizer(wx.HORIZONTAL)
#        upWeightButton = wx.Button(self, wx.ID_ANY, "Upload Site Weights", size=(200,-1))
#        viewWeightButton = wx.Button(self, wx.ID_ANY, "View")
#        weightLabel = wx.StaticText(self, wx.ID_ANY, "None uploaded.")
#        weightSizer.Add(upWeightButton, 0, wx.ALL, 5)
#        weightSizer.Add(viewWeightButton, 0, wx.ALL, 5)
#        weightSizer.Add((0,0), 1, wx.EXPAND)
#        weightSizer.Add(weightLabel, 0, wx.ALL, 5)
#        
#        costSizer = wx.BoxSizer(wx.HORIZONTAL)
#        upCostButton = wx.Button(self, wx.ID_ANY, "Upload Cost Matrix", size=(200,-1))
#        viewCostButton = wx.Button(self, wx.ID_ANY, "View")
#        costLabel = wx.StaticText(self, wx.ID_ANY, "None uploaded.")
#        costSizer.Add(upCostButton, 0, wx.ALL, 5)
#        costSizer.Add(viewCostButton, 0, wx.ALL, 5)
#        costSizer.Add((0,0), 1, wx.EXPAND)
#        costSizer.Add(costLabel, 0, wx.ALL, 5)
#        
#        saveButton = wx.Button(self, wx.ID_ANY, "Save")
#
#        mainSizer.Add(title, 0, wx.CENTER, 5)
#        mainSizer.Add(description, 0, wx.ALL, 5)
#        mainSizer.Add(wx.StaticLine(self), 0, wx.ALL|wx.EXPAND, 5)
#        mainSizer.Add(districtSizer, 0, wx.ALL|wx.EXPAND, 5)
#        mainSizer.Add(warehouseSizer, 0, wx.ALL|wx.EXPAND, 5)
#        mainSizer.Add(destinationSizer, 0, wx.ALL|wx.EXPAND, 5)
#        mainSizer.Add(maxSizer, 0, wx.ALL|wx.EXPAND, 5)
#        mainSizer.Add(distanceSizer, 0, wx.ALL|wx.EXPAND, 5)
#        mainSizer.Add(weightSizer, 0, wx.ALL|wx.EXPAND, 5)
#        mainSizer.Add(costSizer, 0, wx.ALL|wx.EXPAND, 5)
#        mainSizer.Add((0,0), 1, wx.EXPAND)
#        mainSizer.Add(saveButton, 0, wx.ALL|wx.CENTER, 5)
#
#        self.SetSizer(mainSizer)
