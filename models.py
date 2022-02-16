# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class CabinetMedical(models.Model):
    id_cabinet_medical = models.DecimalField(primary_key=True, max_digits=4, decimal_places=0)
    etaj = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    corp_cladire = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cabinet_medical'


class Doctor(models.Model):
    cnp = models.DecimalField(db_column='CNP', primary_key=True, max_digits=13, decimal_places=0)  # Field name made lowercase.
    prenume = models.CharField(max_length=25, blank=True, null=True)
    nume = models.CharField(max_length=25, blank=True, null=True)
    telefon = models.CharField(unique=True, max_length=20, blank=True, null=True)
    email = models.CharField(unique=True, max_length=50, blank=True, null=True)
    data_angajare = models.DateField(blank=True, null=True)
    salariu = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True)
    puncte_comision = models.DecimalField(max_digits=2, decimal_places=2, blank=True, null=True)
    denumire_specialitate = models.CharField(max_length=20, blank=True, null=True)
    id_cabinet_medical = models.ForeignKey(CabinetMedical, models.DO_NOTHING, db_column='id_cabinet_medical', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'doctor'


class DoctorAtasatLaProiect(models.Model):
    id_doctor_proiect = models.DecimalField(primary_key=True, max_digits=5, decimal_places=0)
    cnp_doctor_proiect = models.ForeignKey(Doctor, models.DO_NOTHING, db_column='CNP_doctor_proiect', blank=True, null=True)  # Field name made lowercase.
    id_proiect = models.ForeignKey('Proiect', models.DO_NOTHING, db_column='id_proiect', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'doctor_atasat_la_proiect'


class Medicament(models.Model):
    id_medicament = models.DecimalField(primary_key=True, max_digits=5, decimal_places=0)
    nume_medicament = models.CharField(max_length=50, blank=True, null=True)
    nume_producator = models.CharField(max_length=20, blank=True, null=True)
    forma_farmaceutica = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'medicament'


class MedicamenteContinuteDeTratament(models.Model):
    id_medicamente_continute_de_tratament = models.DecimalField(primary_key=True, max_digits=5, decimal_places=0)
    id_medicament = models.ForeignKey(Medicament, models.DO_NOTHING, db_column='id_medicament', blank=True, null=True)
    id_tratament_medicament = models.ForeignKey('Tratament', models.DO_NOTHING, db_column='id_tratament_medicament', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'medicamente_continute_de_tratament'


class Pacient(models.Model):
    cnp = models.DecimalField(db_column='CNP', primary_key=True, max_digits=13, decimal_places=0)  # Field name made lowercase.
    nume = models.CharField(max_length=25, blank=True, null=True)
    prenume = models.CharField(max_length=25, blank=True, null=True)
    telefon = models.CharField(unique=True, max_length=20, blank=True, null=True)
    sex = models.CharField(max_length=8, blank=True, null=True)
    data_nasterii = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pacient'


class PrescriptiiProgramare(models.Model):
    id_prescriptie = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)
    id_tratament = models.ForeignKey('Tratament', models.DO_NOTHING, db_column='id_tratament', blank=True, null=True)
    id_programare = models.ForeignKey('Programare', models.DO_NOTHING, db_column='id_programare', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prescriptii_programare'


class Programare(models.Model):
    id_programare = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)
    cnp_pacient_programare = models.ForeignKey(Pacient, models.DO_NOTHING, db_column='CNP_pacient_programare', blank=True, null=True)  # Field name made lowercase.
    cnp_doctor_programare = models.ForeignKey(Doctor, models.DO_NOTHING, db_column='CNP_doctor_programare', blank=True, null=True)  # Field name made lowercase.
    data = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'programare'


class Proiect(models.Model):
    id_proiect = models.DecimalField(primary_key=True, max_digits=2, decimal_places=0)
    data_inceput = models.DateField(blank=True, null=True)
    buget_alocat = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    nume_proiect = models.CharField(unique=True, max_length=200, blank=True, null=True)
    stadiu_curent = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proiect'


class Terapie(models.Model):
    id_terapie = models.DecimalField(primary_key=True, max_digits=2, decimal_places=0)
    nume_terapie = models.CharField(max_length=20, blank=True, null=True)
    durata_in_zile = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'terapie'


class TerapieInclusaInTratament(models.Model):
    id_terapie_inclusa_in_tratament = models.DecimalField(primary_key=True, max_digits=5, decimal_places=0)
    id_terapie = models.ForeignKey(Terapie, models.DO_NOTHING, db_column='id_terapie', blank=True, null=True)
    id_tratament_terapie = models.ForeignKey('Tratament', models.DO_NOTHING, db_column='id_tratament_terapie', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'terapie_inclusa_in_tratament'


class Tratament(models.Model):
    id_tratament = models.DecimalField(primary_key=True, max_digits=4, decimal_places=0)
    nume_tratament = models.CharField(max_length=60, blank=True, null=True)
    tip_tratament = models.CharField(max_length=11, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tratament'
