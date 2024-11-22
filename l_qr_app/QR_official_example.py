import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask

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
        qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
        qr.add_data(data)
        # img_1 = qr.make_image(image_factory=StyledPilImage, module_drawer=RoundedModuleDrawer())
        img_2 = qr.make_image(image_factory=StyledPilImage, color_mask=RadialGradiantColorMask())
        img_2.save(f"{filename}.png")
        # img_3 = qr.make_image(image_factory=StyledPilImage, embeded_image_path="image.png")