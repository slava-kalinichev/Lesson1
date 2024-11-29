with open("input.bmp", 'rb') as fin:
    data = list(fin.read())

result = bytes(data[:54] + [255-e for e in data[54:])

with open("res.bmp", 'wb') as fout:
    fout.write(result)