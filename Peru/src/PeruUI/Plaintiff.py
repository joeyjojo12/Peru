import wx
import PeruConstants

def getPlaintiffInfo(self, plaintiffPage):
    output = []
    
    for i in range(0,plaintiffPage.nestedNotebook.GetPageCount()):
        currentPage = plaintiffPage.nestedNotebook.GetPage(i)
        output.append([str(currentPage.FirstName.GetValue()),
                       str(currentPage.LastName.GetValue()),
                       str(currentPage.Location.GetValue()),
                       str(currentPage.Region.GetValue(),
                       str(currentPage.Gender.GetValue()),
                       int(currentPage.Age.GetValue()),
                       int(currentPage.AgeRange.GetValue()),
                       str(currentPage.Religion.GetValue()),
                       str(currentPage.Notes.GetValue()))])
    
    return output

class PlaintiffPanel(wx.Panel):
    def __init__(self, parent):

        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)

        label1 = wx.StaticText(self, label="First Name :")
        FirstName = self.FirstName = wx.TextCtrl(self, size=(400,-1))
        label2 = wx.StaticText(self, label="Last Name :")
        LastName = self.LastName = wx.TextCtrl(self, size=(400,-1))
        label3 = wx.StaticText(self, label="Location :")
        Location = self.Location = wx.TextCtrl(self, size=(400,-1))
        label4 = wx.StaticText(self, label="Region :")
        Region = self.Region = wx.ComboBox(self, 500, PeruConstants.DEFAULT_REGION, (90, 50), (150, -1), PeruConstants.REGION_LIST, wx.CB_DROPDOWN | wx.TE_PROCESS_ENTER )
        label5 = wx.StaticText(self, label="Gender :")
        Gender = self.Gender = wx.ComboBox(self, 500, PeruConstants.DEFAULT_GENDER, (90, 50), (50, -1), PeruConstants.GENDER_LIST, wx.CB_DROPDOWN | wx.TE_PROCESS_ENTER )
        label6 = wx.StaticText(self, label="Age :")
        Age = self.Age = wx.TextCtrl(self, size=(50,-1))
        label7 = wx.StaticText(self, label="Age Range :")
        AgeRange = self.AgeRange = wx.ComboBox(self, 500, PeruConstants.AGE_RANGE_DEFAULT, (90, 50), (70, -1), PeruConstants.AGE_RANGE_LIST, wx.CB_DROPDOWN | wx.TE_PROCESS_ENTER )
        label8 = wx.StaticText(self, label="Religion :")
        Religion = self.Religion = wx.TextCtrl(self, value="Catholic", size=(400,-1))
        label9 = wx.StaticText(self, label="Notes :")
        Notes = self.Notes = wx.TextCtrl(self, -1, style=wx.TE_MULTILINE)
        
        self.Bind(wx.EVT_TEXT, self.EvtText, Age)

        space = 6
        infoSizer = wx.GridBagSizer(hgap=space, vgap=space)
        infoSizer.Add(label1,   (1,0))
        infoSizer.Add(FirstName,(1,1))
        infoSizer.Add(label2,   (2,0))
        infoSizer.Add(LastName, (2,1))
        infoSizer.Add(label3,   (3,0))
        infoSizer.Add(Location, (3,1))
        infoSizer.Add(label4,   (4,0))
        infoSizer.Add(Region,   (4,1))
        infoSizer.Add(label5,   (5,0))
        infoSizer.Add(Gender,   (5,1))
        infoSizer.Add(label6,   (6,0))
        infoSizer.Add(Age,      (6,1))
        infoSizer.Add(label7,   (7,0))
        infoSizer.Add(AgeRange, (7,1))
        infoSizer.Add(label8,   (8,0))
        infoSizer.Add(Religion, (8,1))
        infoSizer.Add(label9,   (9,0))
        infoSizer.Add(Notes,    (9,1), (5,20), flag=wx.EXPAND)
        
        self.buttonSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.savePlaintiffButton = wx.Button(self, -1, "Save Single Plaintiff")
        self.readPlaintiffButton = wx.Button(self, -1, "Read Single Plaintiff")        
        self.buttonSizer.Add(self.savePlaintiffButton, 0, wx.ALIGN_RIGHT)
        self.buttonSizer.Add(self.readPlaintiffButton, 0, wx.ALIGN_RIGHT)
            
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(infoSizer, 1, wx.EXPAND)
        sizer.Add(self.buttonSizer, 0, wx.ALIGN_RIGHT)
                
        self.SetSizer(sizer)
        
    def EvtText(self, event):
        if event.GetString() == "":
            self.AgeRange.SetSelection(0)
            return
        
        age = int(event.GetString())
        if age > 99:
            self.AgeRange.SetSelection(10)
        else:
            self.AgeRange.SetSelection(age/10)
        
class NestedPlaintiffPanel(wx.Panel):
    """
    Panel contains multiple 'Plaintiff' tabs
    """
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)
        self.oldNumPlaintiffs = 1
        
        nestedNotebook = self.nestedNotebook = wx.Notebook(self, wx.ID_ANY)
        
        label1 = wx.StaticText(self, label="Number of Plaintiffs: ")
        numPlaintiffs = self.numPlaintiffs = wx.ComboBox(self, 500, "1", (90, 50), (50, -1), PeruConstants.TAB_NUMBER_LIST, wx.CB_DROPDOWN | wx.TE_PROCESS_ENTER )
        
        self.Bind(wx.EVT_COMBOBOX, self.EvtComboBox, numPlaintiffs)
        
        topSizer = self.topSizer = wx.BoxSizer(wx.HORIZONTAL)
        
        topSizer.Add(label1, 0, wx.ALIGN_LEFT) 
        topSizer.Add(numPlaintiffs, 0, wx.ALIGN_LEFT)

        #for i in range(1,self.numPlaintiffs.GetValue()+1):
        nestedNotebook.AddPage(PlaintiffPanel(nestedNotebook), "Plaintiff 1")
            
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(topSizer, 0, wx.ALIGN_LEFT)
        sizer.Add(nestedNotebook, 1, wx.ALL|wx.EXPAND, 5)

        self.SetSizer(sizer)
        
    # When the user selects something, we go here.
    def EvtComboBox(self, evt):
        newNumPlaintiffs = int(self.numPlaintiffs.GetValue())
        oldNumPlaintiffs = int(self.oldNumPlaintiffs)
        
        if newNumPlaintiffs == oldNumPlaintiffs:
            return
        elif newNumPlaintiffs < oldNumPlaintiffs:
            for i in range(oldNumPlaintiffs-1,newNumPlaintiffs-1,-1):
                self.nestedNotebook.DeletePage(i)
        else:
            for i in range(oldNumPlaintiffs+1,newNumPlaintiffs+1):
                self.nestedNotebook.AddPage(PlaintiffPanel(self.nestedNotebook), "Plaintiff " + str(i))
        
        self.oldNumPlaintiffs = newNumPlaintiffs
        
        