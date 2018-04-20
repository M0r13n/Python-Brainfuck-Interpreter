class BrainfuckParser:
    """A Parser for the Brainfuck Programming Language in Python"""

    def __init__(self, code=None):
        self.instructions = ('<', '>', '+', '-', '.', ',', '[', ']')

    def __call__(self, code):
        self.solve(code)

    def solve(self, code):
        self.data_ptr = 0
        self.data = [0, ]
        self.code = code
        self.code_ptr = 0
        self.loops = []
        self.code_length = len(self.code)
        while self.code_ptr < self.code_length:
            instruction = self.code[self.code_ptr]
            if instruction in self.instructions:
                if instruction == '[':
                    self.loops.append(self.code_ptr)

                elif instruction == ']':
                    # close a loop
                    if self.data[self.data_ptr] > 0:
                        self.code_ptr = self.loops[-1]
                    else:
                        # remove last entry
                        self.loops.pop()

                elif instruction == '>':
                    # increment data pointer
                    self.data_ptr += 1
                    if self.data_ptr == len(self.data):
                        self.data.append(0)

                elif instruction == '<':
                    # decrement code pointer
                    if self.data_ptr > 0:
                        self.data_ptr -= 1
                    else:
                        self.data_ptr = 0

                elif instruction == '+':
                    # increment value at current data field
                    # in case of overflow start with 0 again
                    self.data[self.data_ptr] = self.data[self.data_ptr] + 1 if self.data[self.data_ptr] < 255 else 0

                elif instruction == '-':
                    # decrement value at current data field
                    # i case of overflow start with 255 again
                    self.data[self.data_ptr] = self.data[self.data_ptr] - 1 if self.data[self.data_ptr] > 0 else 255

                elif instruction == '.':
                    # print current data as ASCII
                    print(chr(self.data[self.data_ptr]))
                elif instruction == ',':
                    # TODO missing
                    pass
                self.code_ptr += 1
