#!/usr/bin/env python3
#
# Liam Nolan 2017 (c) BSD 2-Clause

from sys import stdout, exit
from html import escape as esc
#import cgitb

def print_100_lines(path):
#   cgitb.enable()
    '''
    print last lines of file
    '''
    header = ('Content-Type: text/html\n\n')
    html_head = ('''
    <!DOCTYPE html>
       <html>
          <head>
             <meta-charset=UTF-8>
             <title> Logfile Display </title>
          </head>
          <body>
    ''')
    html_foot = ('''
          </body>
       </html>

    ''')
    
    stdout.write(header)
    stdout.write(html_head)
    
    # try and open the file and print 100 of the last lines
    # if that does not work write an error instead
    # TODO this could be improved a lot
    try:
        all_lines = []
        with open(path, mode='r') as logfile:
            # for the last 100 lines in the log, format and add to 
            stdout.write('<ul>\n')
            for line in logfile:
                printable = ('<li>' + str(esc(line)) + '</li>\n')
                all_lines.append(printable)
            for each in all_lines[:-100:-1]:
                stdout.write(each)
            stdout.write('</ul>\n')
    except:
        stdout.write('''
              The program encountered a fatal error! 
           </body>
       </html>
    ''')
        return 1
    stdout.write(html_foot)
    return 0

if __name__=='__main__':
    try:
        file_to_print = '/var/www/html/log/snort.log'
        ret = print_100_lines(file_to_print)
        if ret == 0:
            exit(0)
        else:
            exit(1)
    except (KeyboardInterrupt, SystemExit):
        exit(1)
