import wx
from wx import StaticText
from wx.lib.wordwrap import wordwrap

# Default Tab - all other tabs should inherit this
class DefaultTab(wx.Panel):
    def __init__(self, parent):
        """
        Constructor
        """
        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)
 

# Helper class copied from wx internals
class AutoWrapStaticText(StaticText): 
    """ 
    A simple class derived from :mod:`lib.stattext` that implements auto-wrapping 
    behaviour depending on the parent size. 
 
    .. versionadded:: 0.9.5 
    """ 

    def __init__(self, parent, id, label): 
        """ 
        Default class constructor. 
 
        :param Window parent: a subclass of :class:`Window`, must not be ``None``; 
        :param string `label`: the :class:`AutoWrapStaticText` text label. 
        """ 
        StaticText.__init__(self, parent, id, label, style=wx.ST_NO_AUTORESIZE) 
        self.label = label 
        self.Bind(wx.EVT_SIZE, self.OnSize) 

    def OnSize(self, event): 
        """ 
        Handles the ``wx.EVT_SIZE`` event for :class:`AutoWrapStaticText`. 
 
        :param `event`: a :class:`SizeEvent` event to be processed. 
        """ 
        event.Skip() 
        StaticText.Wrap(self, event.GetSize().width)

#    def Wrap(self, width): 
#        """ 
#        This functions wraps the controls label so that each of its lines becomes at 
#        most `width` pixels wide if possible (the lines are broken at words boundaries 
#        so it might not be the case if words are too long). 
# 
#        If `width` is negative, no wrapping is done. 
# 
#        :param integer `width`: the maximum available width for the text, in pixels. 
# 
#        :note: Note that this `width` is not necessarily the total width of the control, 
#         since a few pixels for the border (depending on the controls border style) may be added. 
#        """ 
#        if width < 0: 
#            return 
#        self.Freeze() 
#
#        dc = wx.ClientDC(self) 
#        dc.SetFont(self.GetFont()) 
#        text = wordwrap(self.label, width, dc) 
#        self.SetLabel(text, wrapped=True) 
#
#        self.Thaw() 
#
#    def SetLabel(self, label, wrapped=False): 
#        """ 
#        Sets the :class:`AutoWrapStaticText` label. 
# 
#        All "&" characters in the label are special and indicate that the following character is 
#        a mnemonic for this control and can be used to activate it from the keyboard (typically 
#        by using ``Alt`` key in combination with it). To insert a literal ampersand character, you 
#        need to double it, i.e. use "&&". If this behaviour is undesirable, use :meth:`~Control.SetLabelText` instead. 
# 
#        :param string `label`: the new :class:`AutoWrapStaticText` text label; 
#        :param bool `wrapped`: ``True`` if this method was called by the developer using :meth:`~AutoWrapStaticText.SetLabel`, 
#         ``False`` if it comes from the :meth:`~AutoWrapStaticText.OnSize` event handler. 
#          
#        :note: Reimplemented from :class:`Control`. 
#        """ 
#        if not wrapped: 
#            self.label = label 
#        StaticText.SetLabel(self, label) 

## Helper class copied from wx internals
#class AutoWrapStaticText(wx.PyControl): 
#    def __init__(self, parent, id=wx.ID_ANY, label="", 
#                 pos=wx.DefaultPosition, size=wx.DefaultSize, 
#                 style=0, name="wrapStatText"): 
#        wx.PyControl.__init__(self, parent, id, pos, size, wx.NO_BORDER, 
#                              wx.DefaultValidator, name) 
#        self.st = wx.StaticText(self, -1, label, style=style) 
#        self._label = label # save the unwrapped text 
#        self._Rewrap() 
#        self.Bind(wx.EVT_SIZE, self.OnSize) 
#        
#
#    def SetLabel(self, label): 
#        self._label = label 
#        self._Rewrap() 
#    def GetLabel(self): 
#        return self._label 
#
#    def SetFont(self, font): 
#        self.st.SetFont(font) 
#        self._Rewrap() 
#    def GetFont(self): 
#        return self.st.GetFont() 
#
#
#    def OnSize(self, evt): 
#        self.st.SetSize(self.GetSize()) 
#        self._Rewrap() 
#
#    def _Rewrap(self): 
#        self.st.Freeze() 
#        self.st.SetLabel(self._label) 
#        self.st.Wrap(self.GetSize().width) 
#        self.st.Thaw() 
#
#    def DoGetBestSize(self): 
#        # this should return something meaningful for what the best 
#        # size of the widget is, but what that size should be while we 
#        # still don't know the actual width is still an open 
#        # question...  Just return a dummy value for now. 
#        return wx.Size(100,100)
