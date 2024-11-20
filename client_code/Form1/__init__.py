from ._anvil_designer import Form1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    # Any code you write here will run before the form opens.
    self.gefaengnisse_drop_down.items = anvil.server.call('get_gefaengnisse')
    self.label_direktor.text = "Direktor TODO" 
    self.label_freie_zellen.text = "Freie Zellen TODO"
    self.repeating_zellen.items = [{'zellennummer': 'TODO', 'anzahl_häftlinge': 'TODO'}, 
                                   {'zellennummer': 'TODO', 'anzahl_häftlinge': 'TODO'}]

  def gefaengnisse_drop_down_change(self, **event_args):
    Name = self.gefaengnisse_drop_down.selected_value
    data = anvil.server.call('get_gefaengis_data', Name)
    self.label_direktor.text = data[0]
    self.label_freie_zellen.text = data[1]
    
    zellennummer_data = anvil.server.call('get_zelle_data', Name)
    
    zelle_data = [(Zellennummer[0], anvil.server.call("get_anzahl_haeftlinge_zelle", Name, Zellennummer)[0]) for Zellennummer in zellennummer_data]
    print(zelle_data)
    
    self.repeating_zellen.items = [{'zellennummer': zellennummer, 'anzahl_häftlinge': anzahl_haeftlinge} for zellennummer, anzahl_haeftlinge in zelle_data]
    
    


 



  
 
