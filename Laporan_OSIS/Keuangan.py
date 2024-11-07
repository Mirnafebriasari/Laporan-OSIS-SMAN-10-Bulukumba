# pelaporan_osis/keuangan.py

class Keuangan:
    def __init__(self):
        self.pemasukan = 0
        self.pengeluaran = 0

    def tambah_pemasukan(self, jumlah):
        self.pemasukan += jumlah

    def tambah_pengeluaran(self, jumlah):
        self.pengeluaran += jumlah

    def saldo(self):
        return self.pemasukan - self.pengeluaran

class LaporanKeuangan:
    def __init__(self):
        self.keuangan = Keuangan()

    def tambah_transaksi(self, jenis, jumlah):
        if jenis == "pemasukan":
            self.keuangan.tambah_pemasukan(jumlah)
        elif jenis == "pengeluaran":
            self.keuangan.tambah_pengeluaran(jumlah)

    def cetak_laporan(self):
        laporan = f"\n--- Laporan Keuangan OSIS ---\n"
        laporan += f"Pemasukan: Rp{self.keuangan.pemasukan}\n"
        laporan += f"Pengeluaran: Rp{self.keuangan.pengeluaran}\n"
        laporan += f"Saldo Akhir: Rp{self.keuangan.saldo()}\n"
        return laporan
