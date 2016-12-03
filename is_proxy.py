import socket


def is_proxy(ip, port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect((ip, port))
    except:
        client.close()
        return False

    client.send('''GET http://bot.whatismyipaddress.com/ HTTP/1.1
Server: bot.whatismyipaddress.com:80
Host: bot.whatismyipaddress.com

''')

    recv_data = ''
    buf = client.recv(10)
    while True:
        recv_data += buf

        http_response = recv_data.split('\r\n')
        if len(http_response) > 1:
            if 'HTTP/' not in http_headers[0]:
                client.close()
                return False

            if http_response[0] == 'HTTP/1.1 200 OK':
                client.close()
                return True

            if 'Proxy Authentication' in http_response[0]:
                client.close()
                return True

        buf = client.recv(100)
