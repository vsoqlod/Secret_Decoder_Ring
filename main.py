"""
Jae Bum Jang
Fall 2022, 10/04
Lab 7

This program is  called secret decoder ring that encrypt and decrypt message using two types of encryption and decryption method, Atbash Cipher and Caesar Cipher. The encrypted message will be written in "message.txt" file, and read to decrypt.  
"""


import check_input
import cipher
import caesar_cipher

def main():
  """Prompt user to encrypt or decrypt, provide encryption or decryption method which are Atbash or Caesar Cipher. If they choose to encrypt, let user to write a message to "messasge.txt" file. If they choose to decrypt, read the encrypted message in "message.txt" file, then display the decrypted message from it. For Caesar cipher, prompt user to enter the shift value from 0 to 25 for the decod or decoded message."""
  
  atbash_msg = cipher.Cipher()
  
  print('Secret Decoder Ring:')
  print('1. Encrypt')
  print('2. Decrypt')
  decoder = check_input.get_int_range("", 1, 2)
  
  if decoder == 1:
    print('Enter encrypytion type: ')
    print('1. Atbash')
    print('2. Caesar')
    encryption_type = check_input.get_int_range('', 1, 2)
    user_msg = input('Enter message: ')
    
    if encryption_type == 1:
      encryption = atbash_msg.encrypt_message(user_msg)
      msg_encrypt = open('message.txt', 'w')
      msg_encrypt.write(encryption)
    
    elif encryption_type == 2:
      shift_input = check_input.get_int_range('Enter the shift value: ', 0, 25)
      caesar_msg = caesar_cipher.CaesarCipher(shift_input)
      encryption = caesar_msg.encrypt_message(user_msg)
      msg_encrypt = open('message.txt', 'w')
      msg_encrypt.write(encryption)
      msg_encrypt.close()
      
    print('Encrypted message saved to \'message.txt\'.')
  
  elif decoder == 2:
    print('Enter decryption type:')
    print('1. Atbash')
    print('2. Caesar')
    user_msg = open('message.txt', 'r')
    decrypt = user_msg.read().strip('\n')
    decryption_type = check_input.get_int_range('', 1, 2)

    if decryption_type == 1:
      decryption = atbash_msg.decrypt_message(decrypt)
                                           
    elif decryption_type == 2:
      shift_input = check_input.get_int_range('Enter the shift value: ', 0, 25)
      caesar_msg = caesar_cipher.CaesarCipher(shift_input)
      decryption = caesar_msg.decrypt_message(decrypt)
    print('Reading encrypted message from \'message.txt\'.')
    print(f'Decrypted message: {decryption}')
    user_msg.close()
  
main()