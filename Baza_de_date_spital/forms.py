from dataclasses import fields
from re import M
from django import forms
from django.forms import ModelForm, widgets

# from Django_BD.Baza_de_date_spital.views import view
from .models import CabinetMedical, Doctor, Medicament, MedicamenteContinuteDeTratament, Pacient, PrescriptiiProgramare, Programare, Proiect, Terapie, TerapieInclusaInTratament, Tratament, DoctorAtasatLaProiect

class DoctorForm(ModelForm):
    class Meta:
        model = Doctor
        fields = ('prenume', 'nume', 'telefon', 'email', 'data_angajare', 'salariu', 'puncte_comision', 'denumire_specialitate', 'id_cabinet_medical')
        labels = {
            
            'prenume': '',
            'nume': '',
            'telefon': '',
            'email': '',
            'data_angajare': '',
            'salariu': '',
            'puncte_comision': '',
            'denumire_specialitate': '',
            'id_cabinet_medical': '',
                    }
        widgets = {
            'cnp': forms.TextInput(attrs={}),
            'prenume': '',
            'nume': '',
            'telefon': '',
            'email': '',
            'data_angajare': '',
            'salariu': '',
            'puncte_comision': '',
            'denumire_specialitate': '',
            'id_cabinet_medical': '',
        }

class PacientForm(ModelForm):
    class Meta:
        model = Pacient
        fields = ( 'prenume', 'nume', 'telefon', 'sex', 'data_nasterii')
        labels = {
            
            'prenume': '',
            'nume': '',
            'telefon': '',
            'sex': '',
            'data_nasterii': '',
                    }
        widgets = {
            'cnp': forms.TextInput(attrs={}),
            'prenume': '',
            'nume': '',
            'telefon': '',
            'email': '',
            'data_angajare': '',
            'salariu': '',
            'puncte_comision': '',
            'denumire_specialitate': '',
            'id_cabinet_medical': '',
        }

class CabinetMedicalForm(ModelForm):
    class Meta:
        model = CabinetMedical
        fields = ('etaj', 'corp_cladire')
        labels = {
            
            'etaj': '',
            'corp_cladire': '',
                    }
        widgets = {
            'cnp': forms.TextInput(attrs={}),
            'prenume': '',
            'nume': '',
            'telefon': '',
            'email': '',
            'data_angajare': '',
            'salariu': '',
            'puncte_comision': '',
            'denumire_specialitate': '',
            'id_cabinet_medical': '',
        }

class ProiectForm(ModelForm):
    class Meta:
        model = Proiect
        fields = ( 'data_inceput', 'buget_alocat', 'nume_proiect', 'stadiu_curent')
        labels = {
            
            'data_inceput': '',
            'buget_alocat': '',
            'nume_proiect': '',
            'stadiu_curent': '',
                    }
        widgets = {
            'cnp': forms.TextInput(attrs={}),
            'prenume': '',
            'nume': '',
            'telefon': '',
            'email': '',
            'data_angajare': '',
            'salariu': '',
            'puncte_comision': '',
            'denumire_specialitate': '',
            'id_cabinet_medical': '',
        }

class DoctorAtasatLaProiectForm(ModelForm):
    class Meta:
        model = DoctorAtasatLaProiect
        fields = ('cnp_doctor_proiect', 'id_proiect')
        labels = {
            
            'cnp_doctor_proiect': '',
            'id_proiect': '',
                    }
        widgets = {
            'cnp': forms.TextInput(attrs={}),
            'prenume': '',
            'nume': '',
            'telefon': '',
            'email': '',
            'data_angajare': '',
            'salariu': '',
            'puncte_comision': '',
            'denumire_specialitate': '',
            'id_cabinet_medical': '',
        }

class MedicamentForm(ModelForm):
    class Meta:
        model = Medicament
        fields = ('nume_medicament', 'nume_producator', 'forma_farmaceutica')
        labels = {
           
            'nume_medicament': '',
            'nume_producator': '',
            'forma_farmaceutica': '',
                    }
        widgets = {
            'cnp': forms.TextInput(attrs={}),
            'prenume': '',
            'nume': '',
            'telefon': '',
            'email': '',
            'data_angajare': '',
            'salariu': '',
            'puncte_comision': '',
            'denumire_specialitate': '',
            'id_cabinet_medical': '',
        }

class TratamentForm(ModelForm):
    class Meta:
        model = Tratament
        fields = ( 'nume_tratament', 'tip_tratament')
        labels = {
            
            'nume_tratament': '',
            'tip_tratament': '',
                    }
        widgets = {
            'cnp': forms.TextInput(attrs={}),
            'prenume': '',
            'nume': '',
            'telefon': '',
            'email': '',
            'data_angajare': '',
            'salariu': '',
            'puncte_comision': '',
            'denumire_specialitate': '',
            'id_cabinet_medical': '',
        }

class MedicamenteContinuteDeTratamentForm(ModelForm):
    class Meta:
        model = MedicamenteContinuteDeTratament
        fields = ( 'id_medicament', 'id_tratament_medicament')
        labels = {
           
            'id_medicament': '',
            'id_tratament_medicament': '',
                    }
        widgets = {
            'cnp': forms.TextInput(attrs={}),
            'prenume': '',
            'nume': '',
            'telefon': '',
            'email': '',
            'data_angajare': '',
            'salariu': '',
            'puncte_comision': '',
            'denumire_specialitate': '',
            'id_cabinet_medical': '',
        }

class ProgramareForm(ModelForm):
    class Meta:
        model = Programare
        fields = ( 'cnp_pacient_programare', 'cnp_doctor_programare', 'data')
        labels = {
            
            'cnp_pacient_programare': '',
            'cnp_doctor_programare': '',
            'data': "",
                    }
        widgets = {
            'cnp': forms.TextInput(attrs={}),
            'prenume': '',
            'nume': '',
            'telefon': '',
            'email': '',
            'data_angajare': '',
            'salariu': '',
            'puncte_comision': '',
            'denumire_specialitate': '',
            'id_cabinet_medical': '',
        }

class PrescriptieProgramareForm(ModelForm):
    class Meta:
        model = PrescriptiiProgramare
        fields = ( 'id_tratament', 'id_programare')
        labels = {
            
            'id_tratament': '',
            'id_programare': '',
                    }
        widgets = {
            'cnp': forms.TextInput(attrs={}),
            'prenume': '',
            'nume': '',
            'telefon': '',
            'email': '',
            'data_angajare': '',
            'salariu': '',
            'puncte_comision': '',
            'denumire_specialitate': '',
            'id_cabinet_medical': '',
        }

class TerapieForm(ModelForm):
    class Meta:
        model = Terapie
        fields = ( 'nume_terapie', 'durata_in_zile')
        labels = {
           
            'nume_terapie': '',
            'durata_in_zile': '',
                    }
        widgets = {
            'cnp': forms.TextInput(attrs={}),
            'prenume': '',
            'nume': '',
            'telefon': '',
            'email': '',
            'data_angajare': '',
            'salariu': '',
            'puncte_comision': '',
            'denumire_specialitate': '',
            'id_cabinet_medical': '',
        }

class TerapieInclusaInTratamentForm(ModelForm):
    class Meta:
        model = TerapieInclusaInTratament
        fields = ( 'id_terapie', 'id_tratament_terapie')
        labels = {
            
            'id_terapie': '',
            'id_tratament_terapie': '',
                    }
        widgets = {
            'cnp': forms.TextInput(attrs={}),
            'prenume': '',
            'nume': '',
            'telefon': '',
            'email': '',
            'data_angajare': '',
            'salariu': '',
            'puncte_comision': '',
            'denumire_specialitate': '',
            'id_cabinet_medical': '',
        }

class View1Form(ModelForm):
    class Meta:
        model = Medicament
        fields = ('nume_medicament', 'nume_producator')
        labels = {
            
            'nume_medicament': '', 
            'nume_producator': ''
                    }
        widgets = {
            'id_medicament': forms.TextInput(attrs={'class': 'form-control'}), 
            'nume_medicament': forms.TextInput(attrs={'class': 'form-control'}), 
            'nume_producator': forms.TextInput(attrs={'class': 'form-control'})       
        }

class View2Form(ModelForm):
    class Meta:
        model = Doctor
        fields =('cnp', 'prenume', 'nume', 'telefon', 'email', 'data_angajare', 'denumire_specialitate', 'id_cabinet_medical')
        labels = {
            'cnp': '', 
            'prenume': '', 
            'nume': '',
            'telefon': '',
            'email': '',
            'data_angajare': '',
            'denumire_specialitate': '',
            'id_cabinet_medical': ''
        }
        widgets = {
            'cnp': forms.TextInput(attrs={'class': 'form-control'}), 
            'prenume': forms.TextInput(attrs={'class': 'form-control'}), 
            'nume': forms.TextInput(attrs={'class': 'form-control'}),
            'telefon': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'data_angajare': forms.TextInput(attrs={'class': 'form-control'}),
            'denumire_specialitate': forms.TextInput(attrs={'class': 'form-control'}),
            'id_cabinet_medical': forms.TextInput(attrs={'class': 'form-control'})
        }