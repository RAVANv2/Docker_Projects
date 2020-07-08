from pystrich.datamatrix import DataMatrixEncoder

encoder = DataMatrixEncoder('This is a DataMatrix.')
encoder.save('./datamatrix_test.png')
print(encoder.get_ascii())

print("Yes i implemented my first python docker file")
