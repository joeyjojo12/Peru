import wx
import PeruConstants

def getDefendantInfo(self, DefendantPage):
    output = []
    
    for i in range(0,DefendantPage.nestedNotebook.GetPageCount()):
        currentPage = DefendantPage.nestedNotebook.GetPage(i)
        output.append([str(currentPage.FirstName.GetValue()),
                       str(currentPage.LastName.GetValue()),
                       str(currentPage.Location.GetValue()),
                       str(currentPage.Region.GetValue(),
                       str(currentPage.Gender.GetValue()),
                       int(currentPage.Age.GetValue()),
                       int(currentPage.AgeRange.GetValue()),
                       str(currentPage.Religion.GetValue()),
                       str(currentPage.Divination.GetValue()),
                       str(currentPage.Healing.GetValue()),
                       str(currentPage.Herbs.GetValue()),
                       str(currentPage.Psychology.GetValue()),
                       str(currentPage.Rituals.GetValue()),
                       str(currentPage.Sacrifices.GetValue()),
                       str(currentPage.Libations.GetValue()),
                       str(currentPage.Witchcraft.GetValue()),
                       str(currentPage.Other.GetValue()),
                       str(currentPage.Notes.GetValue()))])
    
    return output

class DefendantPanel(wx.Panel):
    def __init__(self, parent):

        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)

        label1 = wx.StaticText(self, label="First Name :")
        FirstName = self.FirstName = wx.TextCtrl(self, size=(400,-1),name="First Name")
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
        AgeRange = self.AgeRange = wx.ComboBox(self, 500, PeruConstants.AGE_RANGE_DEFAULT, (90, 50), (90, -1), PeruConstants.AGE_RANGE_LIST, wx.CB_DROPDOWN | wx.TE_PROCESS_ENTER )
        label8 = wx.StaticText(self, label="Religion :")
        Religion = self.Religion = wx.TextCtrl(self, value="Catholic", size=(400,-1))
        label9 = wx.StaticText(self, label="Notes :")
        Notes = self.Notes = wx.TextCtrl(self, -1, style=wx.TE_MULTILINE)
        
        label10 = wx.StaticText(self, label="Healing Classifications :")
        
        Societal = self.Societal = wx.CheckBox(self, -1, "Societal")
        Financial = self.Financial = wx.CheckBox(self, -1, "Financial/Success")
        Emotional = self.Emotional = wx.CheckBox(self, -1, "Emotional/Psychological")
        Spiritual = self.Spiritual = wx.CheckBox(self, -1, "Spiritual")
        Physical = self.Physical = wx.CheckBox(self, -1, "Physical")
        Curse = self.Curse = wx.CheckBox(self, -1, "Curse/Harm/Malintentions")
        
        label11 = wx.StaticText(self, label="Healing Methods :")
               
        Divination = self.Divination = wx.CheckBox(self, -1, "Divination")
        Rituals1 = self.Rituals1 = wx.CheckBox(self, -1, "Rituals (community)")
        Rituals2 = self.Rituals2 = wx.CheckBox(self, -1, "Rituals (per person/small group)")
        Libations = self.Libations = wx.CheckBox(self, -1, "Libations")
        Protection = self.Protection = wx.CheckBox(self, -1, "Protection/Wards")
        Herbs = self.Herbs = wx.CheckBox(self, -1, "Herbs/Ethnomedicine")
        Prayers = self.Prayers = wx.CheckBox(self, -1, "Prayers/Chants/Words/Spells")
        Sacrifices = self.Sacrifices = wx.CheckBox(self, -1, "Sacrifices")
        Blood = self.Blood = wx.CheckBox(self, -1, "Blood Use")
        Surgery = self.Surgery = wx.CheckBox(self, -1, "Surgery")
        Repentance = self.Repentance = wx.CheckBox(self, -1, "Repentance/Redemption")
        Price = self.Price = wx.CheckBox(self, -1, "Price/Cost of Service")
        Clothing = self.Clothing = wx.CheckBox(self, -1, "Special Clothing Required")
        Music = self.Music = wx.CheckBox(self, -1, "Dance/Singing/Music")
        
        
        label12 = wx.StaticText(self, label="Other1 :")
        Other1 = self.Other1 = wx.TextCtrl(self, size=(150,-1))
        label13 = wx.StaticText(self, label="Other2 :")
        Other2 = self.Other2 = wx.TextCtrl(self, size=(150,-1))
        label14 = wx.StaticText(self, label="Other3 :")
        Other3 = self.Other3 = wx.TextCtrl(self, size=(150,-1))
        
        
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
        infoSizer.Add(Notes,    (9,1), (4,2), wx.EXPAND)
        
        infoSizer.Add(label10,   (1,3))        
        infoSizer.Add(Societal,  (1,4))
        infoSizer.Add(Financial, (2,4))
        infoSizer.Add(Emotional, (3,4))
        infoSizer.Add(Spiritual, (1,5))
        infoSizer.Add(Physical,  (2,5))
        infoSizer.Add(Curse,     (3,5))
        
        infoSizer.Add(label11,    (4,3))
        infoSizer.Add(Divination, (5,4))
        infoSizer.Add(Rituals1,   (6,4))
        infoSizer.Add(Rituals2,   (7,4))
        infoSizer.Add(Libations,  (8,4))
        infoSizer.Add(Protection, (9,4))
        infoSizer.Add(Herbs,      (10,4))
        infoSizer.Add(Prayers,    (11,4))
        
        infoSizer.Add(Sacrifices, (5,5))
        infoSizer.Add(Blood,      (6,5))
        infoSizer.Add(Surgery,    (7,5))
        infoSizer.Add(Repentance, (8,5))
        infoSizer.Add(Price,      (9,5))
        infoSizer.Add(Clothing,   (10,5))
        infoSizer.Add(Music,      (11,5))
        
        infoSizer.Add(label12,    (12,4))
        infoSizer.Add(Other1,     (12,5))
        infoSizer.Add(label13,    (13,4))
        infoSizer.Add(Other2,     (13,5))
        infoSizer.Add(label14,    (14,4))
        infoSizer.Add(Other3,     (14,5))
        
        
        
        self.buttonSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.saveDefendantButton = wx.Button(self, -1, "Save Single Defendant")
        self.readDefendantButton = wx.Button(self, -1, "Read Single Defendant")        
        self.buttonSizer.Add(self.saveDefendantButton, 0, wx.ALIGN_RIGHT)
        self.buttonSizer.Add(self.readDefendantButton, 0, wx.ALIGN_RIGHT)
            
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
        
class NestedDefendantPanel(wx.Panel):
    """
    Panel contains multiple 'Defendant' tabs
    """
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)
        self.oldNumDefendants = 1
        
        nestedNotebook = self.nestedNotebook = wx.Notebook(self, wx.ID_ANY)
        
        label1 = wx.StaticText(self, label="Number of Defendants: ")
        numDefendants = self.numDefendants = wx.ComboBox(self, 500, "1", (90, 50), (50, -1), PeruConstants.TAB_NUMBER_LIST, wx.CB_DROPDOWN | wx.TE_PROCESS_ENTER )
        
        self.Bind(wx.EVT_COMBOBOX, self.EvtComboBox, numDefendants)
        
        topSizer = self.topSizer = wx.BoxSizer(wx.HORIZONTAL)
        
        topSizer.Add(label1, 0, wx.ALIGN_LEFT) 
        topSizer.Add(numDefendants, 0, wx.ALIGN_LEFT)

        #for i in range(1,self.numDefendants.GetValue()+1):
        nestedNotebook.AddPage(DefendantPanel(nestedNotebook), "Defendant 1")
            
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(topSizer, 0, wx.ALIGN_LEFT)
        sizer.Add(nestedNotebook, 1, wx.ALL|wx.EXPAND, 5)

        self.SetSizer(sizer)
        
    # When the user selects something, we go here.
    def EvtComboBox(self, evt):
        newNumDefendants = int(self.numDefendants.GetValue())
        oldNumDefendants = int(self.oldNumDefendants)
        
        if newNumDefendants == oldNumDefendants:
            return
        elif newNumDefendants < oldNumDefendants:
            for i in range(oldNumDefendants-1,newNumDefendants-1,-1):
                self.nestedNotebook.DeletePage(i)
        else:
            for i in range(oldNumDefendants+1,newNumDefendants+1):
                self.nestedNotebook.AddPage(DefendantPanel(self.nestedNotebook), "Defendant " + str(i))
        
        self.oldNumDefendants = newNumDefendants