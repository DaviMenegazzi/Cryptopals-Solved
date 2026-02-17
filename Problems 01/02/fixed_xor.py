"""CONVERTE HEXADECIMAIS EM BASE64"""

string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

class Hex_Em_Bits():
    def __init__(self):
        self.hex_map = {
            "a": 10, "b": 11, "c": 12,
            "d": 13, "e": 14, "f": 15,
            "g": 16, "h": 17, "i": 18
        }

        self.hex_index = "0123456789abcdefghi"

        self.bits = 0
        self.hex = None

    def hex_em_bits(self, hex_string):
        """
        Retorna lista de indexes em strings de 4-bits do hex
        
        :param self: Description
        :param hex_string: Description
        
        """

        bits_list = []

        
        for letter_or_number in hex_string:

            # Tenta converter para número
            try:
                letter_or_number = int(letter_or_number)
            except ValueError:
                letter_or_number = str(letter_or_number)

            if type(letter_or_number) == int: # Se for número
                bit_number = "{0:04b}".format(int(letter_or_number))

                # Adiciona o número em formato binário para a lista e sai do loop
                bits_list.append(bit_number)

            if type(letter_or_number) == str:
                letter_in_hex_index = self.hex_map[letter_or_number]
                
                bits_string = [] 
                def retorna_divisao (numero_atual, n):
                    if n == 0: raise Exception("Não pode dividir por 0")
                    bits_string.append(numero_atual % n)
                    quociente = numero_atual // n
                    if quociente != 0:
                        retorna_divisao(quociente, n)
                retorna_divisao(letter_in_hex_index, 2)
                bits_list.append("".join(str(b) for b in bits_string[::-1]))
        return bits_list
 

    def bits_em_hex(self, hex_bits):
        def retorna_decimal (bits):
            decimal = 0
            bits = list(bits)
            bits.reverse()
            for index, num in enumerate(bits):
                if int(num) == 1:
                    decimal += 2**index
            return decimal
        
        s = []
        for i in range(0, len(hex_bits), 4):
            bloco = hex_bits[i:i+4].split()
            for bits in bloco:
                decimal = retorna_decimal(bits)
                s.append(self.hex_index[decimal])
        return "".join(i for i in s)
    
    def em_lista(self, string):
        bits = []
        for caractere in string:
            em_bits = self.hex_em_bits(caractere)
            if em_bits == None: # NOTE: por algum motivo, quando o número no hex é "0" ele retorna None e dá problema no resto do código inteiro
                em_bits = "0000"
            if (em_bits != None):
                bits.append(em_bits)

        return bits
    
    def xor (self, og_bits=None, to_xor_bits=None):
        if og_bits is None:
            og_bits = self.hex
            if og_bits is None:
                raise Exception("Não há HEX String")
        if to_xor_bits is None: 
            ''' Não há XOR string '''
            raise Exception("Não há TO XOR HEX String")
        
        # Considerando que há og_string e xor_string...

        if len(og_bits) != len(to_xor_bits):
            raise Exception("Tamanhos diferentes de strings")
        
        resultado = []

        og_bits = self.hex_em_bits(og_bits)
        to_xor_bits = self.hex_em_bits(to_xor_bits)

        size = len(og_bits)

        for four_bits in range(size):
            f_b = ""
            for bit in range(4):
                if str(og_bits[four_bits][bit]) == str(to_xor_bits[four_bits][bit]):
                    f_b += str(0)
                else:
                    f_b += str(1)
            resultado.append(f_b)

        return self.bits_em_hex("".join(str(r) for r in resultado))


if __name__ == "__main__":

    h = Hex_Em_Bits()
    print(h.xor("1c0111001f010100061a024b53535009181c", "686974207468652062756c6c277320657965"))