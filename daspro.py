person = {
    '07352311170': {'password': '07352311170'},
    '07352311171': {'password': '07352311171'},
    '07352311172': {'password': '07352311172'},
    '07352311173': {'password': '07352311173'},
    '07352311174': {'password': '07352311174'},
    '07352311175': {'password': '07352311175'},
    '07352311176': {'password': '07352311176'},
    '07352311177': {'password': '07352311177'},
    '07352311178': {'password': '07352311178'},
    '07352311179': {'password': '07352311179'}
}

def login(username, password):
    if username in person and password == person[username]['password']:
        print ("Selamat datang di akun mahasiswa informatika")
    else:
        print ("Data yang Anda masukkan salah")

input_username = input("Masukkan username: ")
input_password = input("Masukkan password: ")

hasil_login = login(input_username, input_password)
print(hasil_login)


