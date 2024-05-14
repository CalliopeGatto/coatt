from django.db import models





class CodicientrataModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    Data_Validita = models.CharField(max_length=255)
    Codice_Entrata = models.CharField(max_length=255)
    Codice_Lingua = models.CharField(max_length=255)
    Denominazione_Entrata = models.CharField(max_length=255)
    Denominazione_Estesa = models.CharField(max_length=255)
    Data_Decorrenza = models.CharField(max_length=255)




class ListaentiModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    Data_Validita = models.CharField(max_length=255)
    Tipologia_Ente = models.CharField(max_length=255)
    Codice_Lingua = models.CharField(max_length=255)
    Descrizione_Tipologia = models.CharField(max_length=255)
    Data_Decorrenza = models.CharField(max_length=255)




class ListacaricoenticbModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    Data_Validita = models.CharField(max_length=255)
    Codice_Ente = models.CharField(max_length=255)
    Tipo_Ufficio = models.CharField(max_length=255)
    Codice_Ufficio = models.CharField(max_length=255)
    Tipo_Ente = models.CharField(max_length=255)
    Denominazione = models.CharField(max_length=255)
    Codice_catastale_comune_di_sede = models.CharField(max_length=255)
    Codice_indirizzam_ruoli_erariali = models.CharField(max_length=255)
    Data_Decorrenza = models.CharField(max_length=255)
    Ufficio_statale = models.CharField(max_length=255)




class CodicientrataModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    Data_Validita = models.CharField(max_length=255)
    Codice_Entrata = models.CharField(max_length=255)
    Codice_Lingua = models.CharField(max_length=255)
    Denominazione_Entrata = models.CharField(max_length=255)
    Denominazione_Estesa = models.CharField(max_length=255)
    Data_Decorrenza = models.CharField(max_length=255)




class EnticrbModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    Data_Validita = models.CharField(max_length=255)
    Codice_Ente = models.CharField(max_length=255)
    Tipo_Ufficio = models.CharField(max_length=255)
    Codice_Ufficio = models.CharField(max_length=255)
    Tipo_Ente = models.CharField(max_length=255)
    Denominazione = models.CharField(max_length=255)
    Codice_catastale_comune_di_sede = models.CharField(max_length=255)
    Codice_indirizzam_ruoli_erariali = models.CharField(max_length=255)
    Data_Decorrenza = models.CharField(max_length=255)
    Ufficio_statale = models.CharField(max_length=255)




class ListaimposteModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    Data_Validita = models.CharField(max_length=255)
    Tipologia_Imposta = models.CharField(max_length=255)
    Codice_Lingua = models.CharField(max_length=255)
    Descrizione_Tipologia = models.CharField(max_length=255)
    Data_Decorrenza = models.CharField(max_length=255)




class CodicientrataModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    Data_Validita = models.CharField(max_length=255, null=True, blank=True)
    Codice_Entrata = models.CharField(max_length=255, null=True, blank=True)
    Codice_Lingua = models.CharField(max_length=255, null=True, blank=True)
    Denominazione_Entrata = models.CharField(max_length=255, null=True, blank=True)
    Denominazione_Estesa = models.CharField(max_length=255, null=True, blank=True)
    Data_Decorrenza = models.CharField(max_length=255, null=True, blank=True)




class CodicientrataModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    Data_Validita = models.CharField(max_length=255, null=True, blank=True)
    Codice_Entrata = models.CharField(max_length=255, null=True, blank=True)
    Codice_Lingua = models.CharField(max_length=255, null=True, blank=True)
    Denominazione_Entrata = models.CharField(max_length=255, null=True, blank=True)
    Denominazione_Estesa = models.CharField(max_length=255, null=True, blank=True)
    Data_Decorrenza = models.CharField(max_length=255, null=True, blank=True)




class ListaentiModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    Data_Validita = models.CharField(max_length=255, null=True, blank=True)
    Tipologia_Ente = models.CharField(max_length=255, null=True, blank=True)
    Codice_Lingua = models.CharField(max_length=255, null=True, blank=True)
    Descrizione_Tipologia = models.CharField(max_length=255, null=True, blank=True)
    Data_Decorrenza = models.CharField(max_length=255, null=True, blank=True)




class ListaentiModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    Data_Validita = models.CharField(max_length=255, null=True, blank=True)
    Tipologia_Ente = models.CharField(max_length=255, null=True, blank=True)
    Codice_Lingua = models.CharField(max_length=255, null=True, blank=True)
    Descrizione_Tipologia = models.CharField(max_length=255, null=True, blank=True)
    Data_Decorrenza = models.CharField(max_length=255, null=True, blank=True)




class ListaimposteModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    Data_Validita = models.CharField(max_length=255, null=True, blank=True)
    Tipologia_Imposta = models.CharField(max_length=255, null=True, blank=True)
    Codice_Lingua = models.CharField(max_length=255, null=True, blank=True)
    Descrizione_Tipologia = models.CharField(max_length=255, null=True, blank=True)
    Data_Decorrenza = models.CharField(max_length=255, null=True, blank=True)




class ListaimposteModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    Data_Validita = models.CharField(max_length=255, null=True, blank=True)
    Tipologia_Imposta = models.CharField(max_length=255, null=True, blank=True)
    Codice_Lingua = models.CharField(max_length=255, null=True, blank=True)
    Descrizione_Tipologia = models.CharField(max_length=255, null=True, blank=True)
    Data_Decorrenza = models.CharField(max_length=255, null=True, blank=True)




class DipendentiModel(models.Model):
    id = models.BigAutoField(primary_key=True)




class DipendentiModel(models.Model):
    id = models.BigAutoField(primary_key=True)




class AssenzeModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    codice_matricola = models.CharField(max_length=255, null=True, blank=True)
    operatore = models.CharField(max_length=255, null=True, blank=True)
    sede = models.CharField(max_length=255, null=True, blank=True)
    lun = models.CharField(max_length=255, null=True, blank=True)
    mar = models.CharField(max_length=255, null=True, blank=True)
    mer = models.CharField(max_length=255, null=True, blank=True)
    gio = models.CharField(max_length=255, null=True, blank=True)
    ven = models.CharField(max_length=255, null=True, blank=True)
    sab = models.CharField(max_length=255, null=True, blank=True)
    dom = models.CharField(max_length=255, null=True, blank=True)
    lun = models.CharField(max_length=255, null=True, blank=True)
    mar = models.CharField(max_length=255, null=True, blank=True)
    mer = models.CharField(max_length=255, null=True, blank=True)
    gio = models.CharField(max_length=255, null=True, blank=True)
    ven = models.CharField(max_length=255, null=True, blank=True)
    sab = models.CharField(max_length=255, null=True, blank=True)
    dom = models.CharField(max_length=255, null=True, blank=True)
    lun = models.CharField(max_length=255, null=True, blank=True)
    mar = models.CharField(max_length=255, null=True, blank=True)
    mer = models.CharField(max_length=255, null=True, blank=True)
    gio = models.CharField(max_length=255, null=True, blank=True)
    ven = models.CharField(max_length=255, null=True, blank=True)
    sab = models.CharField(max_length=255, null=True, blank=True)
    dom = models.CharField(max_length=255, null=True, blank=True)
    lun = models.CharField(max_length=255, null=True, blank=True)
    mar = models.CharField(max_length=255, null=True, blank=True)
    mer = models.CharField(max_length=255, null=True, blank=True)
    gio = models.CharField(max_length=255, null=True, blank=True)
    ven = models.CharField(max_length=255, null=True, blank=True)
    sab = models.CharField(max_length=255, null=True, blank=True)
    dom = models.CharField(max_length=255, null=True, blank=True)
    lun = models.CharField(max_length=255, null=True, blank=True)
    mar = models.CharField(max_length=255, null=True, blank=True)




class AssenzeModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    codice_matricola = models.CharField(max_length=255, null=True, blank=True)
    operatore = models.CharField(max_length=255, null=True, blank=True)
    sede = models.CharField(max_length=255, null=True, blank=True)
    lun = models.CharField(max_length=255, null=True, blank=True)
    mar = models.CharField(max_length=255, null=True, blank=True)
    mer = models.CharField(max_length=255, null=True, blank=True)
    gio = models.CharField(max_length=255, null=True, blank=True)
    ven = models.CharField(max_length=255, null=True, blank=True)
    sab = models.CharField(max_length=255, null=True, blank=True)
    dom = models.CharField(max_length=255, null=True, blank=True)
    lun = models.CharField(max_length=255, null=True, blank=True)
    mar = models.CharField(max_length=255, null=True, blank=True)
    mer = models.CharField(max_length=255, null=True, blank=True)
    gio = models.CharField(max_length=255, null=True, blank=True)
    ven = models.CharField(max_length=255, null=True, blank=True)
    sab = models.CharField(max_length=255, null=True, blank=True)
    dom = models.CharField(max_length=255, null=True, blank=True)
    lun = models.CharField(max_length=255, null=True, blank=True)
    mar = models.CharField(max_length=255, null=True, blank=True)
    mer = models.CharField(max_length=255, null=True, blank=True)
    gio = models.CharField(max_length=255, null=True, blank=True)
    ven = models.CharField(max_length=255, null=True, blank=True)
    sab = models.CharField(max_length=255, null=True, blank=True)
    dom = models.CharField(max_length=255, null=True, blank=True)
    lun = models.CharField(max_length=255, null=True, blank=True)
    mar = models.CharField(max_length=255, null=True, blank=True)
    mer = models.CharField(max_length=255, null=True, blank=True)
    gio = models.CharField(max_length=255, null=True, blank=True)
    ven = models.CharField(max_length=255, null=True, blank=True)
    sab = models.CharField(max_length=255, null=True, blank=True)
    dom = models.CharField(max_length=255, null=True, blank=True)
    lun = models.CharField(max_length=255, null=True, blank=True)
    mar = models.CharField(max_length=255, null=True, blank=True)




