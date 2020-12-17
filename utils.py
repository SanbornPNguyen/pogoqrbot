import qrcode
from PIL import Image  
import PIL  
import pyimgur

CLIENT_ID = "" // Imgur client ID goes here
im = pyimgur.Imgur(CLIENT_ID)

def extract_fc(text):
    """
    Extracts Pokemon Go friend codes in any piece of text
    Returns a list of friend codes
    """
    friend_codes = list()
    friend_code = ""

    for character in text:
        if character == " ":
            continue

        try:
            int(character)
            friend_code += character

            if len(friend_code) == 12:
                if friend_code not in friend_codes:
                    friend_codes.append(friend_code)
                friend_code = ""

        except ValueError as e:
            if len(friend_code) < 12 and len(friend_code) > 0:
                friend_code = ""
                
            continue

    return friend_codes

def generate_qr(text):
    """
    Generate QR code from any piece of text
    Returns the location of the saved image
    """
    path = "./qrcodes/{}.jpg".format(text)
    qrcode.make(text).save(path) 
    return path

def imgur_upload(image_path):
    """
    Uploads image at path to imgur
    Returns the imgur link
    """
    return im.upload_image(image_path).link

def create_qr(text):
    """
    Creates QR codes for Pokemon Go friend codes and hosts them
    on imgur
    Returns a list of imgur links
    """
    links = list()
    friend_codes = extract_fc(text)
    for code in friend_codes:
        qr = generate_qr(code)
        url = imgur_upload(qr)
        links.append(url)
    return links
