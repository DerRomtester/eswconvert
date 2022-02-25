import re
import glob
import html

path = "C:\\TEMP\\ELO"

def find_ESW(path):
    text_files = glob.glob(path + "/**/*.ESW", recursive = True)
    return text_files

def convert_xml(path):
    for file in path:
        with open(file,'r', encoding='ANSI',errors='ignore') as f: 
            lines = f.readlines()
            splitpath = file.strip().split(".")
            print(splitpath[0])
            f = open(splitpath[0] + '.xml', 'a', encoding='UTF-8',errors='ignore')
            f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
            f.write('<elo>\n')
            oldchild = ""
            newchild = ""
            child = ["","",""]
            counter = 0
            for line in lines: 
                    counter+=1
                    line = re.sub('\\d+=:', 'a=', line)
                    if line.find("[", 0, 1) == False:
                        oldchild = child[1]
                        child = re.split('\[|\]', line)
                        newchild = child[1]
                    else: 
                        oldchild = child[1]
                        a = line.strip()
                        splitted = a.split("=")
                        splitted[1] = re.sub('\\d+=:', 'a=', splitted[1])
                        writeline = "<" + splitted[0].lower() + ">" + html.escape(splitted[1]) + "</" + splitted[0].lower() + ">\n"
                        newchild = child[1]
                        f.write(writeline)  

                    if counter == 1:
                        if oldchild != newchild:
                            f.write("<" + newchild.lower() + ">\n")
                    else: 
                        if oldchild != newchild:
                            f.write("</" + oldchild.lower() + ">\n")
                            f.write("<" + newchild.lower() + ">\n")
            f.write("</" + oldchild.lower() + ">\n") 
            f.write('</elo>')
            f.close()
        
convert_xml(find_ESW(path))
