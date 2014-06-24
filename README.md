commanda <input file> <output file> <key> <c or v> <c or d>

input file - входной файл
output file - выходной файл
key - ключ, для Цезаря это чило, а для Видженера это слово
c or d - Ceasar or Vigenere 
c or d - crypt(закодировать) or decrypt(раскодировать)  


example:
python lab.py in out 300 c c - читать из файла in, результат поместить в файл out, ключ = 300, использовать шифр Цезаря, закодировать
python lab.py in out secret v d - читать из файла in, результат поместить в файл out, ключ = secret, использовать шифр Видженера, раскодировать
