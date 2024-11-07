from setuptools import setup, find_packages

setup(
    name='Laporan_OSIS',
    version='0.1.0',
    author='Mirna',
    author_email='email@mirnhafebriasari.com',
    description='Paket Python untuk pengolahan gambar',
    long_description=open('README.md').read(),  # Membaca isi README.md untuk deskripsi yang lebih panjang
    long_description_content_type='text/markdown',  # Tipe konten README
    url='https://github.com/Mirnafebriasari/Laporan-OSIS-SMAN-10-Bulukumba.git',
    license='MIT',
    packages=find_packages(),  # Menemukan semua paket yang ada
    install_requires=[
        
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',  # Versi Python yang dibutuhkan
)
