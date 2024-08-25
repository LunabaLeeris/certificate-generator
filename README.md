# certificate-generator
Automatically create certificates. 

# How To Use
Modify the create_certificates() function to your liking 

# Folders

1. Template

- Should contain the certificate template 

2. qr-codes

- On my usecase, I want to paste qr-codes on the certificates so I stored the img_to_paste here

3. output 

- Where the certificates will be stored

4. fonts

- Storage of all the fonts you'll be using. For my use case I used this font to dynamically write the names on the certificates

# Functions

1. ```create_certificates()```

- Sample use case of the script

2. ```paste_image_to_template(path_img_to_paste, composite, y_pos, size)```

- Pastes the img_to_paste inside the composite at y_pos, centered horizontally scaled to a specific size

3. ```write_text_to_template(text, y_pos, font_path, font_size, treshold, composite)```

- Dynamically writes text to a composite image on y_pos, centered horizontally with an initial size of font_size
  If the width of the text exceeds the specified treshold, font_size is reduced iteretively by 1 until the width is within treshold

4. ```save_to_output(composite, name, output_folder)```

- Saves the composite to the output folder