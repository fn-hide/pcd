from PyQt5.QtGui import (
    QImage,
    QPixmap,
    QColor,
    qRgb,
)
import cv2 as cv



class Model:
    def __init__(self):
        pass
    
    def changeBrightness(self, img, val):
        if (val < -255 | val > 255):
            return img

        for row_pixel in range(img.width()):
            for col_pixel in range(img.height()):
                current_val = QColor(img.pixel(row_pixel, col_pixel))
                red = current_val.red()
                green = current_val.green()
                blue = current_val.blue()

                new_red = red + val
                new_green = green + val
                new_blue = blue + val

                # Set the new RGB vals for the current pixel
                if new_red > 255:
                    red = 255
                elif new_red < 0:
                    red = 0
                else:
                    red = new_red

                if new_green > 255:
                    green = 255
                elif new_green < 0:
                    green = 0
                else:
                    green = new_green

                if new_blue > 255:
                    blue = 255
                elif new_blue < 0:
                    blue = 0
                else:
                    blue = new_blue

                new_val = qRgb(red, green, blue)
                img.setPixel(row_pixel, col_pixel, new_val)