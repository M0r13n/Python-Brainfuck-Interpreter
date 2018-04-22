class BrainfuckParser:
    """A Parser for the Brainfuck Programming Language in Python"""

    def __init__(self):
        self.instructions = ('<', '>', '+', '-', '.', ',', '[', ']')

    def __call__(self, code):
        self.solve(code)

    def map_bracelets(self):
        stack = []
        bracelet_map = {}
        for position, instruction in enumerate(self.code):
            if instruction == '[':
                stack.append(position)
            elif instruction == ']':
                x = stack.pop()
                bracelet_map[x] = position
                bracelet_map[position] = x

        return bracelet_map

    def solve(self, code):
        data_ptr = 0
        data = [0, ]
        self.code = ''.join(filter(lambda x: x in self.instructions, code))  # cut invalid stuff
        code_ptr = 0
        bracelet_map = self.map_bracelets()
        code_length = len(self.code)
        while code_ptr < code_length:
            instruction = self.code[code_ptr]
            if instruction == '[':
                if data[data_ptr] == 0:
                    code_ptr = bracelet_map[code_ptr]
            elif instruction == ']':
                if data[data_ptr] > 0:
                    code_ptr = bracelet_map[code_ptr]
            elif instruction == '>':
                # increment data pointer
                data_ptr += 1
                if data_ptr == len(data):
                    data.append(0)

            elif instruction == '<':
                # decrement code pointer
                if data_ptr > 0:
                    data_ptr -= 1
                else:
                    data_ptr = 0

            elif instruction == '+':
                # increment value at current data field
                # in case of overflow start with 0 again
                data[data_ptr] = data[data_ptr] + 1 if data[data_ptr] < 255 else 0

            elif instruction == '-':
                # decrement value at current data field
                # i case of overflow start with 255 again
                data[data_ptr] = data[data_ptr] - 1 if data[data_ptr] > 0 else 255

            elif instruction == '.':
                # print current data as ASCII
                print(chr(data[data_ptr]))
            elif instruction == ',':
                data[data_ptr] = read_in(data_ptr)

            code_ptr += 1


def read_in(cell):
    inp = input('Enter ASCII Value for cell {} : '.format(cell))
    inp = ord(inp)
    if 0 < inp < 255:
        return inp


b = BrainfuckParser()
b(
    '>++++++++[-<+++++++++>]<.>>+>-[+]++>++>+++[>[->+++<<+++>]<<]>-----.>->+++..+++.>-.<<+[>[+>+]>>]<--------------.>>.+++.------.--------.>+.>+.')
