import heapq
from collections import Counter
import matplotlib.pyplot as plt
import networkx as nx

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.freq < other.freq

def BuildHuffmanTree(frequencies):
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

def BuildCodes(node, prefix="", codebook={}):
    if node is not None:
        if node.char is not None:
            codebook[node.char] = prefix
        BuildCodes(node.left, prefix + "0", codebook)
        BuildCodes(node.right, prefix + "1", codebook)
    return codebook

def HuffmanEncoding(data):
    if not data:
        return "", {}
    
    frequencies = Counter(data)
    huffman_tree = BuildHuffmanTree(frequencies)
    codebook = BuildCodes(huffman_tree)
    
    encoded_data = ''.join(codebook[char] for char in data)
    return encoded_data, codebook

def HuffmanDecoding(encoded_data, codebook):
    reverse_codebook = {v: k for k, v in codebook.items()}
    current_code = ""
    decoded_data = []
    
    for bit in encoded_data:
        current_code += bit
        if current_code in reverse_codebook:
            decoded_data.append(reverse_codebook[current_code])
            current_code = ""
    
    return ''.join(decoded_data)

def ReadFile(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def WriteFile(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(data)

def ReplaceWords(text, replacements):
    for old_word, new_word in replacements.items():
        text = text.replace(old_word, new_word)
    return text

def VisualizeHuffmanTree(node):
    def add_edges(graph, node, pos=None, level=0, x=0, y=0, width=4.0):
        if pos is None:
            pos = {}
        pos[node] = (x, y)
        if node.left:
            graph.add_edge(node, node.left)
            l = x - width / 2
            add_edges(graph, node.left, pos, level + 1, l, y - 1, width / 2)
        if node.right:
            graph.add_edge(node, node.right)
            r = x + width / 2
            add_edges(graph, node.right, pos, level + 1, r, y - 1, width / 2)
        return pos

    graph = nx.DiGraph()
    pos = add_edges(graph, node)
    labels = {node: (node.char if node.char else '') + f'\n{node.freq}' for node in pos}
    nx.draw(graph, pos, labels=labels, with_labels=True, node_size=2000, node_color="skyblue", font_size=10, font_weight="bold", arrows=False)
    plt.show()

if __name__ == "__main__":

    # # Test 1
    # input_file_path = 'test1.txt'
    # output_file_path = 'output1.txt'
    # replacements = {'Lorem': 'absolutnie nie Lorem', 'ipsum': 'print(hello World)'}

    # original_text = ReadFile(input_file_path)

    # modified_text = ReplaceWords(original_text, replacements)

    # encoded_data, codebook = HuffmanEncoding(modified_text)
    # WriteFile(output_file_path, encoded_data)

    # decoded_data = HuffmanDecoding(encoded_data, codebook)
    # print("Decoded data:", decoded_data)

    # # visualizacja
    # frequencies = Counter(modified_text)
    # huffman_tree = BuildHuffmanTree(frequencies)
    # VisualizeHuffmanTree(huffman_tree)


    # Test 2 - Opowieść-melodia
    input_text = "boli boli boli boli poli boli boli"
    replacements = {'poli': 'boli'}
    modified_text = ReplaceWords(input_text, replacements)

    print("Original text:", input_text)
    print("Modified text:", modified_text)

    encoded_data, codebook = HuffmanEncoding(modified_text)
    print("Encoded data:", encoded_data)

    decoded_data = HuffmanDecoding(encoded_data, codebook)
    print("Decoded data:", decoded_data)

    frequencies = Counter(modified_text)
    huffman_tree = BuildHuffmanTree(frequencies)
    VisualizeHuffmanTree(huffman_tree)
