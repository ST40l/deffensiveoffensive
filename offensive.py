import socket

def scan_target(ip_address, activity_type):
    # Tarama yapılacak port numaraları
    target_ports = [80, 443, 22, 3389, 8080]

    for port in target_ports:
        try:
            # Soket oluşturma
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)

            # IP adresi ve portu bağlama
            result = sock.connect_ex((ip_address, port))

            if result == 0:
                print(f"Port {port} açık. [{activity_type}]")

                # Veri alımı (data retrieval)
                data = sock.recv(1024)
                print(f"Port {port} verileri: {data.decode('utf-8')}")

            else:
                print(f"Port {port} kapalı. [{activity_type}]")

            sock.close()

        except KeyboardInterrupt:
            print("Tarama kullanıcı tarafından iptal edildi.")
            break

        except socket.gaierror:
            print("Hostname çözümlenemedi. Geçersiz IP adresi.")
            break

        except socket.error:
            print("Sunucu ile bağlantı kurulurken bir hata oluştu.")
            break

# Örnek kullanım
if __name__ == "__main__":
    target_ip = "192.168.1.1"  # Taramak istediğiniz hedef IP adresini buraya yazın.
    activity_type = "Offensive"  # Etkinliğin tipini "Defensive" ya da "Offensive" olarak ayarlayın.

    print(f"İSTİHBARAT BİRLİĞİ: Siber suçlarla mücadele ve terörle mücadele kapsamında {activity_type} port tarama başlatılıyor...")
    scan_target(target_ip, activity_type)
