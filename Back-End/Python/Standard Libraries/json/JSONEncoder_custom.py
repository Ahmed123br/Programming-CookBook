import json 

class ComplexEncoder(json.JSONEncoder):
    def default(self, z):
        return (z.real, z.imag) if isinstance(z, complex) else super().default(z)

print(json.dumps(2 + 5j, cls=ComplexEncoder))