# pelaporan_osis/laporan.py

from .Kegiatan import LaporanKegiatan
from .Keuangan import LaporanKeuangan

class Laporan:
    def __init__(self):
        self.laporan_kegiatan = LaporanKegiatan()
        self.laporan_keuangan = LaporanKeuangan()

    def tambah_kegiatan(self, nama_kegiatan, tanggal, anggaran, deskripsi):
        self.laporan_kegiatan.tambah_kegiatan(nama_kegiatan, tanggal, anggaran, deskripsi)

    def tambah_transaksi_keuangan(self, jenis, jumlah):
        self.laporan_keuangan.tambah_transaksi(jenis, jumlah)

    def cetak_laporan_osisi(self):
        laporan = self.laporan_kegiatan.cetak_laporan()
        laporan += self.laporan_keuangan.cetak_laporan()
        return laporan
