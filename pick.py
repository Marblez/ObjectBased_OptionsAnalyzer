import wx

choice = None


def onButton():
    app = wx.App()
    frame = wx.Frame(None, -1, 'win.py')
    frame.SetSize(wx.Size(200, 50))
    dlg = wx.TextEntryDialog(frame, 'Enter a Stock Ticker', 'Text Entry')
    dlg.SetValue("AMD")
    if dlg.ShowModal() == wx.ID_OK:
        return dlg.GetValue()
    dlg.Destroy()


def pickStrikePrice(choices):

    class MyFrame(wx.Frame):
        def __init__(self, parent, title):
            super(MyFrame, self).__init__(parent, title=title, size=(400, 200))
            self.panel = MyPanel(self)

    class MyPanel(wx.Panel):
        def __init__(self, parent):
            super(MyPanel, self).__init__(parent)
            self.label = wx.StaticText(
                self, label="Pick a Strike Date:", pos=(50, 30))
            languages = choices
            self.combobox = wx.ComboBox(self, choices=languages, pos=(50, 50))
            self.label2 = wx.StaticText(self, label="", pos=(50, 80))
            self.Bind(wx.EVT_COMBOBOX, self.OnCombo)

        def OnCombo(self, event):
            self.label2.SetLabel("You picked " + self.combobox.GetValue())
            global choice
            choice = self.combobox.GetValue()
            app.ExitMainLoop()

    class MyApp(wx.App):
        def OnInit(self):
            self.frame = MyFrame(parent=None, title="Strike Picker")
            self.frame.Show()
            return True

    app = MyApp()
    app.MainLoop()


def returnChoice():
    global choice
    return choice
    