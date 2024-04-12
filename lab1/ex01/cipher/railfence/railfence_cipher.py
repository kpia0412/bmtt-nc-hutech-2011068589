class RailFenceCipher:
    def __init__(self):
        pass

    def rail_fence_encrypt(self, plain_text, num_rails):
        rails = [[] for _ in range(num_rails)]
        rail_index = 0
        direction = 1  # 1: down, -1: up
        for char in plain_text:
            rails[rail_index].append(char)
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction
        cipher_text = ''.join(''.join(rail) for rail in rails)
        return cipher_text

    def rail_fence_decrypt(self, cipher_text, num_rails):
        rail_lengths = [0] * num_rails
        rail_index = 0
        direction = 1

        for i in range(len(cipher_text)):
            rail_lengths[rail_index] += 1
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction

        rails = [''] * num_rails  # Initialize empty rails
        current_rail = 0
        for char in cipher_text:
            rails[current_rail] += char
            current_rail += direction
            if current_rail == num_rails or current_rail == -1:
                direction *= -1
                current_rail += direction

        plain_text = ''.join(rails)
        return plain_text