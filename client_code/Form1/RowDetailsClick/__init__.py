from ._anvil_designer import RowDetailsClickTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class RowDetailsClick(RowDetailsClickTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def Details_click(self, **event_args):
    """This method is called when the button is clicked"""
    # get Form1
    parent = self.parent.parent.parent.parent
    zellennummer = self.item['zellennummer']
    name = parent.gefaengnisse_drop_down.selected_value

    
    haeftlingsnummern = anvil.server.call("get_haeftlinge", name, zellennummer)
    
    einzug_auszug = [anvil.server.call('get_einzug_auszug', name, zellennummer, haeftlingsnummer) for haeftlingsnummer in haeftlingsnummern]

    haftdauer = [anvil.server.call('get_haftdauer', haeftlingsnummer) for haeftlingsnummer in haeftlingsnummern]

    
    alle_daten = []
    for i in range(haeftlingsnummern):
      alle_daten.append(haeftlingsnummern[i], einzug_auszug[i][0], einzug_auszug[i][1], haftdauer[i])

    print(alle_daten)
    
    parent.repeating_panel_zellendetails.items = [{'haeftlingsnummer': i, 'einzug': j, 'auszug': k, 'haftdauer': l} for i, j, k, l in alle_daten]
