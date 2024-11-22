import io
import qrcode
class QRGenerator :
    def generate(self) :
    # inp = input("QR코드로 만들 데이터 : ")
    # filename = input("파일 이름 : ")
        with open("qr_list.txt", "r") as file :
            for line in file :
                filename = line.split("-")[0]
                data = line.split("-")[1]
                self.__create_qr_ascii(filename, data)

    def __create_qr_ascii(self, filename, data) :
        qr = qrcode.QRCode()
        qr.add_data(data)
        f = io.StringIO()
        qr.print_ascii(out=f)
        f.seek(0)
        print(f.read())