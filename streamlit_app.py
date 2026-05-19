import streamlit as st

st.title("🎈 Aplikasi Pengenceran")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
import sys

def hitung_v1(c1, c2, v2):
    """
    Menghitung V1 (Volume Stock yang dibutuhkan)
    Rumus: V1 = (C2 * V2) / C1
    """
    if c1 <= 0 or c2 <= 0 or v2 <= 0:
        return None
    if c2 > c1:
        print("\n[!] Peringatan: Konsentrasi tujuan (C2) lebih tinggi dari stok (C1).")
        print("    Ini secara fisik tidak mungkin jika hanya menambah pelarut.")
        print("    Harap periksa kembali input Anda.")
        return None
    
    v1 = (c2 * v2) / c1
    return v1

def hitung_c2(c1, v1, v2):
    """
    Menghitung C2 (Konsentrasi Akhir)
    Rumus: C2 = (C1 * V1) / V2
    """
    if c1 <= 0 or v1 <= 0 or v2 <= 0:
        return None
    if v1 > v2:
        print("\n[!] Peringatan: Volume stock (V1) lebih besar dari volume total (V2).")
        return None
        
    c2 = (c1 * v1) / v2
    return c2

def hitung_v2(c1, v1, c2):
    """
    Menghitung V2 (Volume Total Akhir)
    Rumus: V2 = (C1 * V1) / C2
    """
    if c1 <= 0 or v1 <= 0 or c2 <= 0:
        return None
    if c2 > c1:
        print("\n[!] Peringatan: Konsentrasi tujuan (C2) lebih tinggi dari stok (C1).")
        return None
        
    v2 = (c1 * v1) / c2
    return v2

def main():
    while True:
        print("\n--- KALKULATOR PENGENCERAN (C1.V1 = C2.V2) ---")
        print("Pilih variabel yang ingin dihitung:")
        print("1. Hitung Volume Stock (V1) -> 'Berapa mL stok yang saya butuhkan?'")
        print("2. Hitung Konsentrasi Akhir (C2) -> 'Berapa molar/konsentrasi larutan akhirnya?'")
        print("3. Hitung Volume Total (V2) -> 'Berapa total volume larutan yang dihasilkan?'")
        print("4. Keluar")

        pilihan = input("Masukkan pilihan (1/2/3/4): ")

        if pilihan == '4':
            print("Terima kasih telah menggunakan kalkulator ini.")
            break

        try:
            if pilihan == '1':
                print("\n--- Menghitung V1 (Volume Stock) ---")
                c1 = float(input("Masukkan Konsentrasi Stock (C1): "))
                c2 = float(input("Masukkan Konsentrasi Tujuan (C2): "))
                v2 = float(input("Masukkan Volume Total Yang Diinginkan (V2): "))
                
                hasil = hitung_v1(c1, c2, v2)
                if hasil is not None:
                    print(f"\n=> Hasil: Anda memerlukan {hasil:.4f} unit volume stock (V1).")
                    print(f"   Tambahkan {hasil:.4f} unit stock ke dalam {v2 - hasil:.4f} unit pelarut.")

            elif pilihan == '2':
                print("\n--- Menghitung C2 (Konsentrasi Akhir) ---")
                c1 = float(input("Masukkan Konsentrasi Stock (C1): "))
                v1 = float(input("Masukkan Volume Stock yang ditambahkan (V1): "))
                v2 = float(input("Masukkan Volume Total Larutan (V2): "))
                
                hasil = hitung_c2(c1, v1, v2)
                if hasil is not None:
                    print(f"\n=> Hasil: Konsentrasi akhir (C2) adalah {hasil:.4f}")

            elif pilihan == '3':
                print("\n--- Menghitung V2 (Volume Total) ---")
                c1 = float(input("Masukkan Konsentrasi Stock (C1): "))
                v1 = float(input("Masukkan Volume Stock yang ditambahkan (V1): "))
                c2 = float(input("Masukkan Konsentrasi Tujuan (C2): "))
                
                hasil = hitung_v2(c1, v1, c2)
                if hasil is not None:
                    print(f"\n=> Hasil: Total volume larutan (V2) adalah {hasil:.4f}")
                    print(f"   Jadi, tambahkan {v1} stock ke dalam {hasil - v1:.4f} pelarut.")

            else:
                print("Pilihan tidak valid. Silakan coba lagi.")

        except ValueError:
            print("\nError: Input harus berupa angka! Silakan coba lagi.")
        except ZeroDivisionError:
            print("\nError: Jangan ada nilai nol (0) pada input.")
        
        input("\nTekan Enter untuk mengulang...")

if __name__ == "__main__":
    main()
