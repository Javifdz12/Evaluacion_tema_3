import hashlib
import pandas as pd
class ejercicio5:
    def __init__(self):
        pass

    def cifrar_sha256(self,contenido):
        pals=contenido.split(maxsplit=4)
        m=hashlib.sha256()
        for p in pals:
            m.update(p.encode('ASCII',errors='ignore'))
            s=m.hexdigest()
            return s

    def descifrar(self,resolverhash,type):
        try:
            resolvedor = open("10-million-password-list-top-1000000.txt", 'r')
            for x in resolvedor.readlines():
                a = x.strip("\n").encode('ASCII',errors='ignore')
                if type == 'md5':
                    a = hashlib.md5(a).hexdigest()
                elif type == 'sha1':
                    a = hashlib.sha1(a).hexdigest()
                elif type == 'sha224':
                    a = hashlib.sha224(a).hexdigest()
                elif type == 'sha256':
                    a = hashlib.sha256(a).hexdigest()
                elif type == 'sha384':
                    a = hashlib.sha384(a).hexdigest()
                elif type == 'sha512':
                    a = hashlib.sha512(a).hexdigest()
                else:
                    raise Exception('El tipo de encriptación %s no es válido.' %str(type))
                if a == resolverhash:
                    print("Contraseña: {} - Has resuelto: {} - Encriptado con: {}" .format(x.rstrip(),str(a),str(type)))
                    break

        except Exception as e:
            print("Error: {}".format(e))


    def Preparar_cifrados_ascii(self):
        lineas1=open('codigo-ascii.txt','r')
        lineas2=[]
        for linea in lineas1.readlines():
            lineas2.append(self.cifrar_sha256(linea))
        cifrados=pd.DataFrame(lineas2)
        return cifrados


    def Preparar_descifrados_ascii(self):
        lineas1=open('codigo-ascii.txt','r')
        lineas2=[]
        for linea in lineas1.readlines():
            lineas2.append(self.descifrar(self.cifrar_sha256(linea),'sha256'))
        descifrados=pd.DataFrame(lineas2)
        return descifrados

    def ejecutar(self):
        x=input('¿Que mensaje quieres encriptar y despues probar si podemos desencriptarlo?: ')
        print(self.cifrar_sha256(x))
        self.descifrar(self.cifrar_sha256(x),'sha256')
        print('---------Cifrados Tabla ASCII-----------')
        print(self.Preparar_cifrados_ascii())
        print(print('\n---------Descifrados Tabla ASCII-----------'))
        print(self.Preparar_descifrados_ascii())









