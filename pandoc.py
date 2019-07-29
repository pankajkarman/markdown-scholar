import re, argparse
import pandas as pd
import pytablewriter as ptw

def remove_hash(filename):
    with open(filename, 'r') as md:
        table = md.readlines()
        table[0] = table[0].replace('# ', 'Table: ') + '\n'
        table = ''.join(table)
        
    with open(filename, 'w') as outfile:
        outfile.write(table)

def replace_include(infile, outfile):
    with open(infile, 'r') as data:
        lines = data.readlines()
        for line in lines:
            if re.search("!include", line):
                idx = lines.index(line)
                extfile = line.split(' ')[-1].split('\n')[0]
                with open(extfile, 'r') as ext:
                    content = ext.readlines()
                content = ' '.join(content)
    lines[idx] =  content
    lines = ''.join(lines)
    with open(outfile, 'w') as newfile:
        newfile.write(lines)
        
class Table():
    def __init__(self, df):
        self.df = df
        
    def to_markdown(self, outfile=None):            
        self.writer = ptw.MarkdownTableWriter()
        self.writer.from_dataframe(self.df)
        #self.writer.write_table()
        if outfile:
            self.writer.dump(outfile)
        return self
    
    def to_latex(self, outfile=None):            
        self.writer = ptw.LatexTableWriter()
        self.writer.from_dataframe(self.df)
        #self.writer.write_table()
        if outfile:
            self.writer.dump(outfile)
        return self
