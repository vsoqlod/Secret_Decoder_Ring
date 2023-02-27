import cipher
"""Extend the cipher class."""

class CaesarCipher(cipher.Cipher):
  """Represents Caesar Cipher.
  Attributes:
    super class: Cipher class.
    shift (int) : shift value of the letters that will shift location of the letters from the message."""
  
  def __init__(self, shift):
    """Call super class to initialize alphabets and set the shift value, raise the exception if it's an invalid value."""
    super().__init__()
    self.shift = shift
    while self.shift != int(shift):
      raise TypeError("Invalid Input - Enter an integer.")

  def _encrypt_letter(self, letter):
    """Find the location of the letter to encrypt and use the Caesar cipher to decode."""
    location = (self.list_alphabet.index(letter) + self.shift) % 26
    return self.list_alphabet[location]
    
  def _decrypt_letter(self, letter):
    """Find the location of the letter to decrypt and use the Caesar cipher to decode."""
    location = (self.list_alphabet.index(letter) - self.shift) % 26
    return self.list_alphabet[location]


