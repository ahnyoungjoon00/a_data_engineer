import io
import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask

class QRGenerator:
    def generate(self, data):
        qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
        qr.add_data(data)
        img = qr.make_image(image_factory=StyledPilImage
                            , color_mask=RadialGradiantColorMask())
        
        img_bytes = io.BytesIO()
        img.save(img_bytes)
        img_bytes.seek(0)
        return img_bytes.read()

