from argparse import _AttributeHolder


filename = input("Enter a filename : ")
position = filename.rfind(".")
extension = filename[position:]
print(extension)