#!/usr/bin/env python3
# Task 01 : Implement Caesar Cipher 
# Create a Python program that can encrypt and decrypt text using the Caesar Cipher algorithm. 
# Allow users to input a message and a shift value to perform encryption and decryption.

# How it works: Replacing each letter of the alphabet with the letter standing three places further down the alphabet

    # Cipher Algorithm:
    # Encryption: (x + k) % m
    # Decryption: (y - k) % m

        # where x is the message letter position, 
        # y is the position of the encrypted letter.
        # k is the key (3 for Caesar Cipher),
        # m is the size of the alphabet.

import sys
import string

chars = {
    'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10,
    'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20,
    'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25,
    
    'a': 26, 'b': 27, 'c': 28, 'd': 29, 'e': 30, 'f': 31, 'g': 32, 'h': 33, 'i': 34, 'j': 35, 'k': 36,
    'l': 37, 'm': 38, 'n': 39, 'o': 40, 'p': 41, 'q': 42, 'r': 43, 's': 44, 't': 45, 'u': 46,
    'v': 47, 'w': 48, 'x': 49, 'y': 50, 'z': 51,
    
    '0': 52, '1': 53, '2': 54, '3': 55, '4': 56, '5': 57, '6': 58, '7': 59, '8': 60, '9': 61,
    ' ': 62, '!': 63, '"': 64, '#': 65, '$': 66, '%': 67, '&': 68
}

def encrypt_caesar(plaintext, key=3):
    
    ciphertext = ""
    
    for char in plaintext:
        
        if char in chars:
            x = chars[char]
            y = (x + key) % len(chars)
            for k, v in chars.items():
                if v == y:
                    ciphertext += k
                    break    
        else: ciphertext += char
            
    return ciphertext

def decrypt_caesar(ciphertext, key=3):
    
    plaintext = ""

    for char in ciphertext:
        if char in chars:
            char_index = chars[char]
            decrypted_index = (char_index - key) % len(chars)
            for k, v in chars.items():
                if v == decrypted_index:
                    plaintext += k
                    break
        else: ciphertext += char

    return plaintext

def run_caesar_cipher():
    
    print("===== Welcome to the Caesar Cipher Program! =====")
    
    continue_program = True
    while continue_program:
        
        match input("Do you want to encrypt a message using Caesar Cipher? (yes/no): ").strip().lower():
            
            case 'yes':
                plaintext = input("Enter the plaintext you would like to encrypt: ")
                encrypted = encrypt_caesar(plaintext) 
                print(" 🔐 Encrypted Text:", encrypted)     
                
                if input("Do you want to decrypt a message? (yes/no): ").strip().lower() == 'yes':
                    print(" 🔓 Decrypted Text:", decrypt_caesar(encrypted))
                else:
                    print(" ⏳ Exiting decryption process.")

                        
            case 'no':
                print(" ⏳ Exiting Caesar Cipher program...")
                continue_program = False
            
            case _:
                print(" ⚠️ Invalid choice. Please enter 'yes' or 'no'.")
                run_caesar_cipher()
                
if __name__ == "__main__":
    run_caesar_cipher()
