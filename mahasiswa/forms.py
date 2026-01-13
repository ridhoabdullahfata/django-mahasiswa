from django import forms
from .models import Mahasiswa, GrupMahasiswa

class MahasiswaForm(forms.ModelForm):
    class Meta:
        model = Mahasiswa
        fields = ['nama', 'nim', 'email', 'jurusan', 'angkatan', 'alamat', 'telepon', 'foto', 'grup']
        widgets = {
            'nama': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Masukkan nama lengkap'
            }),
            'nim': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Masukkan NIM'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'email@example.com'
            }),
            'jurusan': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Contoh: Teknik Informatika'
            }),
            'angkatan': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '2025'
            }),
            'alamat': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Alamat lengkap'
            }),
            'telepon': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '08xxxxxxxxxx'
            }),
            'foto': forms.FileInput(attrs={
                'class': 'form-control'
            }),
            'grup': forms.CheckboxSelectMultiple()
        }
        labels = {
            'nama': 'Nama Lengkap',
            'nim': 'NIM',
            'email': 'Email',
            'jurusan': 'Jurusan',
            'angkatan': 'Angkatan',
            'alamat': 'Alamat',
            'telepon': 'Nomor Telepon',
            'foto': 'Foto Mahasiswa',
            'grup': 'Grup/Kelas'
        }

class GrupMahasiswaForm(forms.ModelForm):
    class Meta:
        model = GrupMahasiswa
        fields = ['nama_grup', 'tipe_grup', 'tahun_dibuat', 'deskripsi', 'aktif']
        widgets = {
            'nama_grup': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Contoh: Kelas A, Tim Project X'
            }),
            'tipe_grup': forms.Select(attrs={
                'class': 'form-control'
            }),
            'tahun_dibuat': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '2025'
            }),
            'deskripsi': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Deskripsi grup (opsional)'
            }),
            'aktif': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            })
        }