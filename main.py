import os
import time

from commands import commander

commands = open('input.txt', 'r').read()
commands_ = commands.split('\n')


def len_fit(text, length, char=' '):
    return str(text + char * (length - len(text)))


def header(title):
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\n\n\n\n')
    print('             ╔══════════════════════════════════════════════════╗')
    print('             ║    {}║'.format(len_fit(title, 46)))
    print('             ╠══════════════════════════════════════════════════╣')


def about():
    header('Contact Book')
    print('             ║ Lesson: Save and recover data                    ║')
    print('             ║ Home work: HW3                                   ║')
    print('             ║ Teacher: Pr. Rasekh                              ║')
    print('             ║ Student: Amin Hemmati                            ║')
    print('             ║ Student number: 9672193                          ║')
    print('             ╚══════════════════════════════════════════════════╝')
    time.sleep(5)



about()

output = ''
for command in commands_:
    result = commander(command)
    output = output + command + '\n' + result + '\n\n'

text_file = open("output.txt", "w")
text_file.write(output)
text_file.close()

os.system('cls' if os.name == 'nt' else 'clear')
print('\n\n\n\n\n                  output.txt generated.')
print('                  github: https://github.com/AminHCE/hcesql\n\n\n\n\n\n\n\n\n')
