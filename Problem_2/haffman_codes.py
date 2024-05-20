import heapq
from collections import Counter

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(frequencies):
    heap = [HuffmanNode(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)
        merged = HuffmanNode(None, node1.freq + node2.freq)
        merged.left = node1
        merged.right = node2
        heapq.heappush(heap, merged)
    
    return heap[0]

def build_codes(node, prefix="", codebook={}):
    if node is not None:
        if node.char is not None:
            codebook[node.char] = prefix
        build_codes(node.left, prefix + "0", codebook)
        build_codes(node.right, prefix + "1", codebook)
    return codebook

def huffman_encoding(data):
    if not data:
        return "", {}
    
    frequencies = Counter(data)
    huffman_tree = build_huffman_tree(frequencies)
    codebook = build_codes(huffman_tree)
    
    encoded_data = ''.join(codebook[char] for char in data)
    return encoded_data, codebook

def huffman_decoding(encoded_data, codebook):
    reverse_codebook = {v: k for k, v in codebook.items()}
    current_code = ""
    decoded_data = []
    
    for bit in encoded_data:
        current_code += bit
        if current_code in reverse_codebook:
            decoded_data.append(reverse_codebook[current_code])
            current_code = ""
    
    return ''.join(decoded_data)

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def write_file(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(data)

def replace_words(text, replacements):
    for old_word, new_word in replacements.items():
        text = text.replace(old_word, new_word)
    return text


if __name__ == "__main__":

    # pierwszy przyklad
    input_file_path = 'test1.txt'
    output_file_path = 'output1.txt'
    replacements = {'Lorem': 'absolutnie nie Lorem', 'ipsum': 'print(hello World)'}

    original_text = read_file(input_file_path)

    modified_text = replace_words(original_text, replacements)

    encoded_data, codebook = huffman_encoding(modified_text)
    write_file(output_file_path, encoded_data)

    decoded_data = huffman_decoding(encoded_data, codebook)
    print("Decoded data:", decoded_data)

