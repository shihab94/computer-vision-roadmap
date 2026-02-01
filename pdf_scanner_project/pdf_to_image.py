import os
from pdf2image import convert_from_path

# take terminal input of invoice directory
INVOICE_DIR = '/home/ahmed/Desktop/practice/computer_vision/computer-vision-roadmap/invoices'

def convert_pdfs_to_images() :

    if not os.path.exists(INVOICE_DIR) :
        print("Directory path is invalid!")
        exit(0)

    # creating 'images' sub-directory
    output_image_dir = os.path.join(INVOICE_DIR, 'images')
    os.makedirs(output_image_dir, exist_ok=True)

    # listing pdf files inside the directory
    for file in os.listdir(INVOICE_DIR) :

        if not file.lower().endswith('.pdf') :
            continue

        file_path = os.path.join(INVOICE_DIR, file)
        pdf_page_images = convert_from_path(file_path, dpi=300)

        file_name = os.path.splitext(file)[0]
        print(f"Started file processing : {file_name} ...")

        # saving pdf pages as image
        for i, page in enumerate(pdf_page_images) :
            img_name = f"{file_name}_page_{i+1}.png"
            img_path = os.path.join(output_image_dir, img_name)
            page.save(img_path, "PNG")

        print(f"Completed file processing : {file_name}")

    print(f"Completed Full processing.")


convert_pdfs_to_images()