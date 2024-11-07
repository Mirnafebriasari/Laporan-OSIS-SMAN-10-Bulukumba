# pelaporan_osis/kegiatan.py

class Kegiatan:
    def __init__(self, nama_kegiatan, tanggal, anggaran, deskripsi):
        self.nama_kegiatan = nama_kegiatan
        self.tanggal = tanggal
        self.anggaran = anggaran
        self.deskripsi = deskripsi

    def __str__(self):
        return f"{self.nama_kegiatan} pada {self.tanggal} - Anggaran: Rp{self.anggaran}"

class LaporanKegiatan:
    def __init__(self):
        self.kegiatan_list = []

    def tambah_kegiatan(self, nama_kegiatan, tanggal, anggaran, deskripsi):
        kegiatan = Kegiatan(nama_kegiatan, tanggal, anggaran, deskripsi)
        self.kegiatan_list.append(kegiatan)

    def cetak_laporan(self):
        laporan = "\n--- Laporan Kegiatan OSIS ---\n"
        for kegiatan in self.kegiatan_list:
            laporan += f"{kegiatan}\n"
        return laporan
