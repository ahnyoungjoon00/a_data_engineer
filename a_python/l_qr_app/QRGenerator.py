import qrcode
class QRGenerator :
    
    def generate(self) :
        # inp = input("QR코드로 만들 데이터 : ")
        # filename = input("파일 이름 : ")
        with open("qr_list.txt", "r") as file :
            for line in file :
                filename = line.split("-")[0]
                data = line.split("-")[1]
                self.__create_qr(filename, data)

    def __create_qr(self, filename, data) :
                img = qrcode.make(data)
                type(img)  # qrcode.image.pil.PilImage
                img.save(f"{filename}.png")