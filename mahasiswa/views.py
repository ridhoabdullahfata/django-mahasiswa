from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Mahasiswa
from .forms import MahasiswaForm

# Landing page (untuk user belum login)
def home(request):
    if request.user.is_authenticated:
        return redirect('mahasiswa:list')
    return render(request, 'mahasiswa/home.html')

# Register
def register(request):
    if request.user.is_authenticated:
        return redirect('mahasiswa:list')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        
        if password != password2:
            messages.error(request, 'Password tidak cocok!')
            return redirect('mahasiswa:register')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username sudah digunakan!')
            return redirect('mahasiswa:register')
        
        user = User.objects.create_user(username=username, email=email, password=password)
        messages.success(request, 'Registrasi berhasil! Silakan login.')
        return redirect('mahasiswa:login')  # ← DIPERBAIKI
    
    return render(request, 'mahasiswa/registration/register.html')

# List mahasiswa dengan fitur pencarian
@login_required(login_url='mahasiswa:login')
def mahasiswa_list(request):
    # Ambil parameter pencarian dari GET request
    search_query = request.GET.get('search', '')
    
    # Filter mahasiswa berdasarkan pencarian
    if search_query:
        mahasiswa_list = Mahasiswa.objects.filter(
            nama__icontains=search_query
        ) | Mahasiswa.objects.filter(
            nim__icontains=search_query
        ) | Mahasiswa.objects.filter(
            jurusan__icontains=search_query
        )
    else:
        mahasiswa_list = Mahasiswa.objects.all()
    
    # Urutkan berdasarkan nama
    mahasiswa_list = mahasiswa_list.order_by('nama')
    
    context = {
        'mahasiswa_list': mahasiswa_list,
        'search_query': search_query,
    }
    return render(request, 'mahasiswa/list.html', context)

# Create mahasiswa
@login_required(login_url='mahasiswa:login')  # ← DIPERBAIKI
def mahasiswa_create(request):
    if request.method == 'POST':
        form = MahasiswaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mahasiswa berhasil ditambahkan!')
            return redirect('mahasiswa:list')
    else:
        form = MahasiswaForm()
    
    return render(request, 'mahasiswa/form.html', {
        'form': form, 
        'title': 'Tambah Mahasiswa',
        'button_text': 'Simpan'
    })

# Detail mahasiswa
@login_required(login_url='mahasiswa:login')  # ← DIPERBAIKI
def mahasiswa_detail(request, pk):
    mahasiswa = get_object_or_404(Mahasiswa, pk=pk)
    return render(request, 'mahasiswa/detail.html', {'mahasiswa': mahasiswa})

# Update mahasiswa
@login_required(login_url='mahasiswa:login')  # ← DIPERBAIKI
def mahasiswa_update(request, pk):
    mahasiswa = get_object_or_404(Mahasiswa, pk=pk)
    if request.method == 'POST':
        form = MahasiswaForm(request.POST, request.FILES, instance=mahasiswa)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data mahasiswa berhasil diupdate!')
            return redirect('mahasiswa:list')
    else:
        form = MahasiswaForm(instance=mahasiswa)
    
    return render(request, 'mahasiswa/form.html', {
        'form': form, 
        'title': 'Edit Mahasiswa',
        'button_text': 'Update'
    })

# Delete mahasiswa
@login_required(login_url='mahasiswa:login')  # ← DIPERBAIKI
def mahasiswa_delete(request, pk):
    mahasiswa = get_object_or_404(Mahasiswa, pk=pk)
    if request.method == 'POST':
        mahasiswa.delete()
        messages.success(request, 'Mahasiswa berhasil dihapus!')
        return redirect('mahasiswa:list')
    
    return render(request, 'mahasiswa/confirm_delete.html', {'mahasiswa': mahasiswa})

# ... kode yang sudah ada ...

def about_us(request):
    """Halaman About Us"""
    return render(request, 'mahasiswa/about_us.html')

def gallery(request):
    """Halaman Gallery"""
    return render(request, 'mahasiswa/gallery.html')