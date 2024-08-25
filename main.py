from PIL import Image, ImageDraw, ImageFont
import os

# Assumes img should be horizontally centered so we just need the y value
def create_certificates(template_path, img_to_paste, output_folder, y_pos_img, img_size, font_path, font_size, y_pos_text):
    # Load the template image
    template = Image.open(template_path)

    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Enumerate all image files in the QR codes folder
    qr_codes_paths = [os.path.join(img_to_paste, f) for f in os.listdir(img_to_paste) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

    for idx, qr_code_path in enumerate(qr_codes_paths):
        composite = template.copy()

        paste_image_to_template(qr_code_path, composite, y_pos_img, img_size)

        write_text_to_template("Christian Lee Lunaba", y_pos_text, font_path, font_size, 1600, composite)

        save_to_output(composite, "sample", output_folder)


# Assumes img should be horizontally centered so we just need the y value
def paste_image_to_template(path_img_to_paste, composite, y_pos, size):
    # Load the QR code image
    img = Image.open(path_img_to_paste)

    # Resize the QR code to the specified size
    img = img.resize(size)

    # Centering Horizontally
    x_pos = (composite.width - size[0]) // 2

    # Overlay the QR code onto the template at the specified position
    composite.paste(img, (x_pos, y_pos), img)

    print(f"Pasting image success")


# Assumes text should be horizontally centered so we just need the y value
def write_text_to_template(text, y_pos, font_path, font_size, treshold, composite):
    draw = ImageDraw.Draw(composite)
    font = ImageFont.truetype(font_path, font_size)

    # Ensures the text is within the cert
    for i in range(font_size):
        font = ImageFont.truetype(font_path, font_size - i)
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]

        if (text_width <= treshold):
            break

    # Centering Horizontally
    x_pos = (composite.width - text_width) // 2

    # Add text to the image at the specified position
    draw.text((x_pos, y_pos), text, font=font, fill=(0, 0, 0))
    
    print(f"Writing Text Success")


def save_to_output(composite, name, output_folder):
    output_path = os.path.join(output_folder, f"output_{name}.png")
    composite.save(output_path)

    print(f"Saved: {output_path}")


# Example usage
template_path   : str   = "template/cert_member.png"
qr_codes_folder : str   = "qr-codes"       
output_folder   : str   = "output"      
qr_code_size    : int   = 250    
y_pos_img       : int = 825
font_path       : str   = "fonts/citadel_script.ttf"  
y_pos_text      : int   = 600
font_size       : int   = 150

create_certificates(template_path, qr_codes_folder, output_folder, y_pos_img, (qr_code_size, qr_code_size), font_path, font_size, y_pos_text)
