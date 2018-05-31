fw = open("a_text_file.txt", 'w')
fw.write("Just a text file sample\n")
fw.write("On the second line\n")
fw.close()

fr = open("a_text_file.txt", 'r')
text = fr.read()
print(text)
fr.close()