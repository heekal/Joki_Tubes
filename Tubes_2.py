admin = {
    'username' : ['admin1', 'admin2'],
    'name' : ['haikal', 'luna'],
    'password' : ['123', '321']
}

manager = {
    'username' : ['manager1', 'manager2'],
    'name' : ['haikal', 'luna'],
    'password' : ['123', '321']

}

pembeli = {
    'username' : ['haikal_luna', 'luna_haikal'],
    'name' : ['haikal', 'luna'],
    'password' : ['123', '321']
}

database = {
    'penerbangan' : {
        'seat' : {
            'regular' : 1,
            'premium' : 2,
            'firstclass': 3
        }, 
        'rute' : {
            'bandung' : 1000,
            'jakarta' : 2000,
            'surabaya' : 1000, 
            'pekanbaru' : 500
        }
    },
    'armada' : {
        'tv_girl' : {
            'vocal' : 'alex',
            'guitarist' : 'mark',
            'drummer' : 'john',
            'harga' : 5000
        },
        'grrl_gen' : {
            'vocal' : 'maudy',
            'guitarist' : 'djadjat',
            'dummer' : 'sucipto',
            'harga' : 7000
        }
    },
    'tiket_terjual' : {
        'tv_girl' : 5,
        'grrl_gen' : 10
    },
    'pembeli' : {
        'tv_girl' : {
            'nama' : ['haikal', 'luna'],
            'tanggal' : [150, 150]
        },
        'grrl_gen' : {
            'nama' : ['aulia', 'ali'],
            'tanggal' : [300, 300]
        }

    }
}

class Aplikasi:
    def __init__(self, username, name, password, pengguna):
        self.username = username    # isinya username
        self.name = name            # isinya nama user
        self._password = password   # isinya password username
        self.pengguna = pengguna    # isinya jenis pengguna, admin, manager, pembeli
    
    def userlogin(self):
        username = input('Masukkan Username: ')
        password = input('Masukkan Password: ')
        return username, password
    
    def login(self, pengguna):
        username, password = self.userlogin()
        for username_stored, name_stored, password_stored in zip(pengguna['username'], pengguna['name'], pengguna['password']):
            if username == username_stored and password == password_stored:
                return username_stored, name_stored, password_stored
        else:
            return '', '', ''
    
    def verifikasi(self, pengguna):
        username, name, passowrd = self.login(pengguna)
        if username != '' and name != '' and passowrd !='':
            return True
        else:
            return False
        
class Admin(Aplikasi):
    def __init__(self, username, name, password, pengguna):
        super().__init__(username, name, password, pengguna)

    def main_menu(self):
        print('Pilih Opsi Yang Ingin Digunakan: ')
        print('1. Tambah Manager')
        print('2. Edit Manager')
        print('3. Hapus Manger')
        opsi = int(input('Pilihan Kamu: '))

        if opsi == 1:
            self.tambah_data()
        elif opsi == 2:
            self.edit_data()
        elif opsi == 3:
            self.hapus_data()
    
    def admin_login(self):
        print('Harap Masuk Menggunakan Akun Kamu : ')
        self.verifikasi(self.pengguna)

    def tambah_data(self):
        print('Masukkan Data Manager Yang Mau Ditambah: ')
        manager['username'].append(input('Masukkan Username: '))
        manager['name'].append(input('Masukkan Nama Manager: '))
        manager['password'].append(input('Masukkan Password Manager: '))

    def edit_data(self):
        print('Masukkan Data Manager Yang Mau Diganti: ')
        username, password = self.userlogin()
        for indeks, username_stored, in enumerate(manager['username']):
            if username == username_stored:
                manager['username'][indeks] = input('Masukkan Username Baru: ')
                manager['name'][indeks] = input('Masukkan Nama Pengguna Baru: ')
                manager['password'][indeks] = input('Masukkan Password Baru: ')
                print('Data Berhasil Diganti !')
        else:
            print('Data Tidak Ditemukan !')

    def hapus_data(self):
        print('Masukkan Data Manager Yang Ingin Dihapus: ')
        username, password = self.userlogin()
        for username_stored, name_stored, password_stored in zip(manager['username'], manager['name'], manager['password']):
            if username == username_stored and password == password_stored:
                manager['username'].remove(username_stored)
                manager['name'].remove(name_stored)
                manager['password'].remove(password_stored)
                print('Data Telah Dihapus!')
        else:
            print('Data Tidak Ditemukan !')

class Manager(Aplikasi):
    def __init__(self, username, name, password, pengguna):
        super().__init__(username, name, password, pengguna)
    
    def main_menu(self):
        print('Pilih Opsi:')
        print('1. Tambah/Edit Data Penerbangan')
        print('2. Tambah/Edit Data Armada')
        print('3. Ubah Harga Tiket')
        print('4. Tampilkan Data Penerbangan')
        print('5. Tampikan Data Armada')
        print('6. Tampilkan Tiket Terjual')
        print('7. Tampilkan Daftar Pembeli')
        print('8. Tampilkan Total Penjualan dan Sisa Tiket')
        print('9. Keluar')

    def tampil_data(self, kategori_1, kategori_2):
        for key, value in database[kategori_1][kategori_2].items():
            print(f'{key}\t{value}')

    def ganti_data(self, cari_kategori , kategori_1, kategori_2, key, value):
        if cari_kategori in database[kategori_1] and key not in database[kategori_1][kategori_2]:
            return False
        database[kategori_1][kategori_2][key] = value
        return True

    def penerbangan(self):
        print('Pilih Opsi: ')
        print('1. Tambah Data')
        print('2. Edit Data')
        opsi = int(input('Pilihan Kamu: '))

        if opsi == 1:
            self.tambah_data_penerbangan()
        elif opsi == 2:
            self.edit_data_penerbangan()
        else:
            print('Harap Pilih Opsi Yang Ada')

    def tambah_data_penerbangan(self):
        print('Harap Isi Data Berikut')
        print('1. Tambah Data Seat')
        print('2. Tambah Data Rute')
        opsi = int(input('Opsi Kamu: '))

        if opsi == 1:
            pass
        elif opsi == 2:
            pass
        else:
            print('Harap Pilih Opsi Yang Ada')

    def edit_data_penerbangan(self):
        print('Harap Isi Data Berikut')
        print('1. Ganti Data Seat')
        print('2. Ganti Data Rute')
        opsi = int(input('Opsi Kamu: '))

        if opsi == 1:
            self.tampil_data('penerbangan', 'seat')
            key = input('Seat Yang Ingin Diganti: ')
            value = int(input('Harga Seat Yang Baru: '))
            self.ganti_data('seat', 'penerbangan', 'seat', key, value)
        elif opsi == 2:
            self.tampil_data('penerbangan', 'rute')
            key = input('Seat Yang Ingin Diganti: ')
            value = int(input('Harga Seat Yang Baru: '))
            self.ganti_data('rute', 'penerbangan', 'rute', key, value)
        else:
            print('Harap Pilih Opsi Yang Ada')

class Pembeli(Aplikasi):
    def __init__(self, username, name, password, pengguna):
        super().__init__(username, name, password, pengguna)

    def main_menu(self):
        print('Pilih Opsi')
        print('1. Tampilkan Daftar Penerbangan')
        print('2. Tampilkan Daftar Tiket')
        print('3. Cari penerbangan')
        print('4. Cari Tiket')
        print('5. Pesan Tiket')
        print('6. Keluar')

aplikasi = Aplikasi('', '', '', '')
username, name, password,  = aplikasi.login(admin)

haikal = Admin(username, name, password, admin)
haikal.main_menu()