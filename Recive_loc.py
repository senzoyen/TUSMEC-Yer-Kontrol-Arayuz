import serial

# Arduino'nun bağlı olduğu port ve baud rate'i tanımlayın
SERIAL_PORT = 'COM7'  # Arduino'nun bağlı olduğu portu burada belirtin (ör. COM7, /dev/ttyUSB0)
BAUD_RATE = 9600             # Arduino kodunda ayarlanan baud rate

def main():
    try:
        # Seri bağlantıyı başlat
        ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
        print("Arduino bağlantısı kuruldu. Veri bekleniyor...\n")

        while True:
            # Arduino'dan gelen veriyi oku
            if ser.in_waiting > 0:  # Gelen veri olup olmadığını kontrol et
                data = ser.readline().decode('utf-8').strip()  # Veriyi oku ve Unicode olarak çöz
                print(f"Gelen veri: {data}")  # Konsola yazdır
    
    except serial.SerialException as e:
        print(f"Seri bağlantı hatası: {e}")
    except KeyboardInterrupt:
        print("\nProgram sonlandırılıyor...")
    finally:
        if 'ser' in locals() and ser.is_open:
            ser.close()
            print("Arduino bağlantısı kapatıldı.")

if __name__ == "__main__":
    main()
