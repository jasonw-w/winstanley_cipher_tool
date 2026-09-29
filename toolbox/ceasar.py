class caesar:
    def __init__(self, plaintext='', ciphertext='', shifting=0):
        self.plaintext = plaintext
        self.ciphertext = ciphertext
        self.shifting = shifting

    def shiftchar(self, char=None, shifting=None):
        if shifting is None:
            shifting = self.shifting
        if char is None:
            return char
        if char.isalpha():
            if char.islower():
                base = ord('a')
            else:
                base = ord('A')
            return chr((ord(char) - base + shifting) % 26 + base)
        return char
            
    def plain2cipher(self, plaintext=None, shifting=None):
        if shifting is None:
            shifting = self.shifting
        if plaintext is None:
            plaintext = self.plaintext
        opt = ""
        for char in plaintext:
            opt += self.shiftchar(char, shifting)
        return opt
    def cipher2plain(self, ciphertext=None, shifting=None):
        if shifting is None:
            shifting = self.shifting
        if ciphertext is None:
            ciphertext = self.ciphertext
        opt = ""
        for char in ciphertext:
            opt += self.shiftchar(char, -shifting)
        return opt
