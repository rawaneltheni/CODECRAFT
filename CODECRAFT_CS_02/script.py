"""
TASK 02 : Pixel Manipulation for Image Encryption
------------------------------------------------
Develop a simple image encryption tool using pixel manipulation.
You can perform operations like swapping pixel values
or applying a basic mathematical operation to each pixel.
Allow users to encrypt and decrypt images.
"""

from PIL import Image as PilImage, ImageTk as PilImageTk
import random
import numpy as np
import hashlib
from tkinter import *
from tkinter import filedialog, messagebox
from tkinter import simpledialog


# --------------------------
# GUI Setup
# --------------------------
window = Tk()
window.title("Image Encryption")
window.geometry("500x500")
icon = PhotoImage(file='CODECRAFT_CS_02/appicon.png')
window.iconphoto(True, icon)
window.config(background='#1b1b20')

# --------------------------
# Global State
# --------------------------
check_upload = False
img = None

# --------------------------
# Utility Functions
# --------------------------
def upload():
    global check_upload, img
    file_path = filedialog.askopenfilename(
        title="Select an Image",
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif")]
    )
    
    if file_path:
        img = PilImage.open(file_path)
        img = img.resize((250, 250))
        img_tk = PilImageTk.PhotoImage(img)
        
        image_label.config(image=img_tk)
        image_label.image = img_tk
        
        check_upload = True
        encrypt_button.config(state=NORMAL)
        decrypt_button.config(state=NORMAL)

def encrypt():
    global img, check_upload
    if not check_upload:
        messagebox.showerror("Error", "Upload an image first!")
        return

    # Ask user for password
    password = simpledialog.askstring("Encryption Key", "Enter a password for encryption:")
    if not password:
        messagebox.showerror("Error", "Encryption password is required!")
        return

    # Generate hash-based keys from password
    hash_key = hashlib.sha256(password.encode()).digest()
    keys = [hash_key[0], hash_key[1], hash_key[2]]

    # Convert image to NumPy array
    image_array = np.array(img)

    #  Embed a small verification tag (RGB for "RAW")
    tag = np.array([82, 65, 87], dtype=np.uint8)
    image_array[0, 0, :3] = tag

    # Shuffle pixels using deterministic seed
    np.random.seed(keys[0])
    flat = image_array.reshape(-1, 3)
    np.random.shuffle(flat)
    image_array = flat.reshape(image_array.shape)

    # Encrypt with XOR
    for i in range(3):
        image_array[..., i] ^= keys[i]

    # Convert back to image
    encrypted_img = PilImage.fromarray(image_array.astype('uint8'))
    img = encrypted_img

    # Update GUI
    img_tk = PilImageTk.PhotoImage(img)
    image_label.config(image=img_tk)
    image_label.image = img_tk

    messagebox.showinfo("Encrypt", "Image encrypted successfully!")
    save_button.config(state=NORMAL)


def decrypt():
    global img, check_upload
    if not check_upload:
        messagebox.showerror("Error", "Upload an image first!")
        return

    password = simpledialog.askstring("Decryption Key", "Enter the password for decryption:")
    if not password:
        messagebox.showerror("Error", "Decryption password is required!")
        return

    # Recreate key
    hash_key = hashlib.sha256(password.encode()).digest()
    keys = [hash_key[0], hash_key[1], hash_key[2]]

    image_array = np.array(img)

    # Step 1: Reverse XOR
    for i in range(3):
        image_array[..., i] ^= keys[i]

    # Step 2: Unshuffle pixels
    np.random.seed(keys[0])
    flat = image_array.reshape(-1, 3)
    indices = np.arange(flat.shape[0])
    np.random.shuffle(indices)
    inverse_indices = np.argsort(indices)
    flat = flat[inverse_indices]
    image_array = flat.reshape(image_array.shape)

    # Check verification tag
    tag = image_array[0, 0, :3]
    if not np.array_equal(tag, [82, 65, 87]):  # "RAW"
        messagebox.showerror("Error", "Wrong password! Decryption failed.")
        return

    decrypted_img = PilImage.fromarray(image_array.astype('uint8'))
    img = decrypted_img

    # Update GUI
    img_tk = PilImageTk.PhotoImage(img)
    image_label.config(image=img_tk)
    image_label.image = img_tk

    messagebox.showinfo("Decrypt", "Decryption successful!")
    save_button.config(state=NORMAL)

        
def save():
    if not check_upload:
        messagebox.showerror(title="Error", message="Nothing to save!")
        return

    # Ask user where to save
    file_toSave = filedialog.asksaveasfilename(
        defaultextension=".png", 
        filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All files", "*.*")]
    )
    
    if not file_toSave:  
        return

    # Save the current image
    img.save(file_toSave)
    
    messagebox.showinfo("Save", f"Image saved to:\n{file_toSave}")

# --------------------------
# GUI Elements
# --------------------------

appLable = Label(window, text="Image Encryption Tool", font=("Comic Sans", 30), bg='#1b1b20').grid(row=3, column=3, columnspan=10, pady=30)

upload_icon = PhotoImage(file='CODECRAFT_CS_02/uploadicon.png')
upload_icon = upload_icon.subsample(50, 50)

upload_button = Button(
    window, 
    text="Upload", 
    command=upload, 
    font=("Comic Sans", 20),
    bg='#FFFAFA',
    fg='#1b1b20',
    image=upload_icon,
    compound='left'
)
upload_button.grid(row=6, column=3)

image_label = Label(window)
image_label.grid(row=10, column=6, columnspan=10, pady=20)


encrypt_button = Button(
    window, 
    text="Encrypt", 
    command=encrypt,  # fixed
    font=("Comic Sans", 20),
    bg='#FFFAFA',
    fg='#1b1b20',
    state=DISABLED
)
encrypt_button.grid(row=6, column=6)

decrypt_button = Button(
    window, 
    text="Decrypt", 
    command=decrypt,  
    font=("Comic Sans", 20),
    bg='#FFFAFA',
    fg='#1b1b20',
    state=DISABLED
)
decrypt_button.grid(row=6, column=9)


save_button = Button(
    window, 
    text="Save", 
    command=save,  
    font=("Comic Sans", 20),
    bg='#FFFAFA',
    fg='#1b1b20',
    state=DISABLED
)
save_button.grid(row=6, column=12)

window.mainloop()


