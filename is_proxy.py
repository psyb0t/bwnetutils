import socket


def is_proxy(ip, port, with_auth=True):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(2)

    try:
        client.connect((ip, port))

        client.send('''GET http://example.org/ HTTP/1.1
Server: example.org:80
Host: example.org

''')
        recv_data = ''
        buf = client.recv(10)
        while buf:
            recv_data += buf

            http_response = recv_data.split('\r\n')
            if len(http_response) > 1:
                if 'HTTP/' not in http_response[0]:
                    client.close()
                    return False

                if 'Proxy Authentication' in http_response[0]:
                    client.close()
                    return with_auth

                expected_string = 'http://www.iana.org/domains/example'
                if expected_string in ''.join(http_response):
                    client.close()
                    return True

            buf = client.recv(100)
    except:
        client.close()
        return False
