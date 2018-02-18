#!/usr/bin/python3
# Cristina del Río. #ejemplo: http://localhost:1234/9/mas/8
# Reutilizo parte del código que tenía en servidor-random.
"""
Simple HTTP Server version 2: reuses the port, so it can be
restarted right after it has been killed. Accepts connects from
the outside world, by binding to the primary interface of the host.

Jesus M. Gonzalez-Barahona and Gregorio Robles
{jgb, grex} @ gsyc.es
SAT and SARO subjects (Universidad Rey Juan Carlos)
"""

import socket
import calculadora

# Create a TCP objet socket and bind it to a port
# Port should be 80, but since it needs root privileges,
# let's use one above 1024

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Let the port be reused if no process is actually using it
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# Bind to the address corresponding to the main name of the host
mySocket.bind(('localhost', 1234))

# Queue a maximum of 5 TCP connection requests
mySocket.listen(5)

# Accept connections, read incoming data, and answer back an HTML page
# (in an almost-infinite loop; the loop can be stopped with Ctrl+C)
try:
    while True:
        print('Waiting for connections')
        (recvSocket, address) = mySocket.accept()
        print('HTTP Request received:')
        request = str(recvSocket.recv(2048), 'utf-8')
        resource = request.split()[1]  # Hay que poner: /num1/operacion/num2
        print(resource)
        _, op1, operacion, op2 = resource.split('/')  # Para ir separando con /

        try:
            num1 = float(op1)
            num2 = float(op2)
            resultado = calculadora.funciones[operacion](num1, num2)
        except ValueError:
            resultado = "Error, solo puedes meter operandos que sean numeros."
        except KeyError:
            resultado = "Error: mas, menos, multiplicado, dividido, elevado"

        # Respuesta:
        recvSocket.send(bytes(
                        "HTTP/1.1 200 OK\r\n\r\n" +
                        "<html><body><h1>Bienvenido a la calculadora!</h1>" +
                        "<p>El resultado de la operacion es: " +
                        str(resultado) +
                        "</p></body></html>" +
                        "\r\n", "utf-8"))
        recvSocket.close()

except KeyboardInterrupt:
    print("\nClosing binded socket")
mySocket.close()
