import socket
import webbrowser

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.bind(("0.0.0.0", 5005))
    while True:
        data, addr = sock.recvfrom(1024)
        comando = data.decode("utf-8")
        if comando == "/abrir":
            chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
            url = "https://laica.ifrn.edu.br/"
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab(url)
except KeyboardInterrupt:
    print("Fechando...")