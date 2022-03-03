class Reversable:
    def __init__(self, seq):
        self.seq = seq

    def __len__(self):
        return len(self.seq)
    
    def __getitem__(self, item):
        return self.seq[item]
    
    def __reversed__(self):
        yield from f'Reversing: {self.seq[::-1]}'
    

r = Reversable('Foo bar baz!')
print(list(r))
print(list(reversed(r)))
# ['F', 'o', 'o', ' ', 'b', 'a', 'r', ' ', 'b', 'a', 'z', '!']
# ['R', 'e', 'v', 'e', 'r', 's', 'i', 'n', 'g', ':', ' ', '!', 'z', 'a', 'b', ' ', 'r', 'a', 'b', ' ', 'o', 'o', 'F']