myfile = open('task1.html', 'w')
myfile.write("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd\">\n")

myfile.write("<html>\n<head>\n")
myfile.write("<meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\">\n")
myfile.write("<title>Multiplication Table </title>\n")

myfile.write("<style type=\"text/css\">\n")
myfile.write("table {background: #FDF5E6; border: 1px solid #adebad; border-collapse: collapse;}\n")
myfile.write("td, th {padding: 3px; }\n")
myfile.write("td {text-align: center;border-bottom: 1px solid #a52a2a; border: 1px solid #333; \n}")
myfile.write("th {background: #a52a2a; color: white; }\n")
myfile.write("tr.even {background: #FFFFF0; }\n")
myfile.write("</style>\n")

myfile.write("<body>\n<table>\n")

for i in range(1,10):
    if i%2 == 0:
        string = "<tr class=\"even\">"
    else:
        string = "<tr>"
    for j in range(1,10):
        string += '<td>' +str(i) + ' * ' + str(j) + ' = ' + str(i * j) + '</td>'
    string += "</tr>"
    myfile.write(string + '\n')
myfile.write("</table>\n</body>\n</html>\n")