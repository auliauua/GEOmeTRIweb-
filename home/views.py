from django.shortcuts import render

def datar(request):
    materi = ["Lingkaran", "Persegi", "Persegi panjang", "Jajar genjang", "Belah ketupat", "Segitiga", "Segi lima (pentagon)", "Trapesium"]
    
    konteks = {
    'title': materi
    }
    return render(request, 'datar.html', konteks)

def ruang(request):
    materi = ["Kubus", "Balok", "Prisma", "Limas", "Kerucut", "Tabung", "Bola"]
    
    konteks = {
        'title': materi
    }
    return render(request, 'ruang.html', konteks)

def tokoh(request):
    materi = ["Thales", "Phytagoras", "Euclid", "Al-khawarizmi"]
    
    konteks = {
        'title': materi
    }
    return render(request, 'tokoh.html', konteks)

def soal(request):
    materi = ["Bangun Datar", "Bangun Ruang "]
    
    konteks = {
        'title': materi
    }
    return render(request, 'soal.html', konteks)

def home(request):
    return render(request, 'home.html')