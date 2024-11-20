import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.files
from anvil.files import data_files
import anvil.server
import sqlite3


@anvil.server.callable
def get_gefaengnisse():
  conn = sqlite3.connect(data_files['gefaengnis.db'])
  cursor = conn.cursor()
  res = list(cursor.execute("SELECT Name FROM Gefaengnis"))
  new_res = [(item[0], item[0]) for item in res]
  conn.close()
  return new_res

@anvil.server.callable
def get_gefaengis_data(Name):
  conn = sqlite3.connect(data_files['gefaengnis.db'])
  cursor = conn.cursor()
  res = list(cursor.execute(f"SELECT Direktor, Frei FROM Gefaengnis WHERE Name = '{Name}'"))
  conn.close()
  return res[0]

@anvil.server.callable
def get_zelle_data(Name):
  conn = sqlite3.connect(data_files['gefaengnis.db'])
  cursor = conn.cursor()
  res = list(cursor.execute(f"SELECT Zellennummer FROM Zelle WHERE GefaengnisName = '{Name}'"))
  conn.close()
  return res

@anvil.server.callable
def get_anzahl_haeftlinge_zelle(Name, Zellennummer):
  conn = sqlite3.connect(data_files['gefaengnis.db'])
  cursor = conn.cursor()
  res = list(cursor.execute(f"SELECT COUNT(*) FROM Zelle_Haeftling WHERE GefaengnisName = '{Name}' AND Zellennummer = '{Zellennummer}' AND Auszug IS NULL"))
  conn.close()
  return res[0]


@anvil.server.callable
def get_haeftlinge(Name, Zellennummer):
  conn = sqlite3.connect(data_files['gefaengnis.db'])
  cursor = conn.cursor()
  res = list(cursor.execute(f"SELECT Haeftlingsnummer FROM Zelle_Haeftling WHERE GefaengnisName = '{Name}' AND Zellennummer = '{Zellennummer}'"))
  conn.close()
  return res

@anvil.server.callable
def get_einzug_auszug(Name, Zellennummer, Haeftlingsnummer):
  conn = sqlite3.connect(data_files['gefaengnis.db'])
  cursor = conn.cursor()
  res = list(cursor.execute(f"SELECT EInzug, Auszug FROM Zelle_Haeftling WHERE GefaengnisName = '{Name}' AND Zellennummer = '{Zellennummer}' AND Haeftlingsnummer = '{Haeftlingsnummer}'"))
  conn.close()
  return res


@anvil.server.callable
def get_haftdauer(Haeftlingsnummer):
  conn = sqlite3.connect(data_files['gefaengnis.db'])
  cursor = conn.cursor()
  res = list(cursor.execute(f"SELECT Haftdauer FROM Haeftling WHERE Haeftlingsnummer = '{Haeftlingsnummer}'"))
  conn.close()
  return res