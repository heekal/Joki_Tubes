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
        'bandung' : 1000,
        'jakarta' : 2000,
        'surabaya' : 1000, 
        'pekanbaru' : 500},
    'armada' : {
        'tv_girl' : {
            'vocal' : 'alex',
            'guitarist' : 'mark',
            'drummer' : 'john'
        },
        'grrl_gen' : {
            'vocal' : 'maudy',
            'guitarist' : 'djadjat',
            'dummer' : 'sucipto'
        }
    },
    'harga' : {
        'regular' : 1,
        'premium' : 2,
        'firstclass': 3
    },
    'tiket_terjual' : {
        # cara isinya misal :
        # tv girl : 3
    },
    'pembeli' : {
        'nama' : [],
        'tiket' : [],
        'tanggal' : []
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

aplikasi = Aplikasi('', '', '', '')
username, name, password,  = aplikasi.login(admin)

haikal = Admin(username, name, password, admin)
haikal.main_menu()