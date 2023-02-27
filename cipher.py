class Cipher():
  """Represents Atbash Cipher.
  Attributes:
    list_alphabet (lsit): list with letters A to Z."""
  
  def __init__(self):
    """Initializes list of letters A to Z."""
    self.list_alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  
  def encrypt_message(self, message):
    """Convert the message into upper case letters, then loop through letter to encrypt message and ignore other characters."""
    encryption = ""
    message = message.upper()
    for character in message:
      if character in self.list_alphabet:
        encryption = encryption + self._encrypt_letter(character)
      else:
        encryption = encryption + character
    return encryption
    
  def decrypt_message(self, message):
    """Convert the message into upper case letters, then loop through letter to decrypt message and ignore other characters."""
    decryption = ""
    message = message.upper()
    for character in message:
      if character in self.list_alphabet:
        decryption = decryption + self._decrypt_letter(character)
      else:
        decryption = decryption + character
    return decryption
    
  def _encrypt_letter(self, letter):
    """seek for the location of the letter to encrypt and use Atbash cipher to decode."""
    location = 25 - self.list_alphabet.index(letter)
    return self.list_alphabet[location]
    
  def _decrypt_letter(self, letter):
    """seek for the location of the letter to decrypt and use Atbash cipher to decode."""
    location = 25 - self.list_alphabet.index(letter)
    return self.list_alphabet[location]