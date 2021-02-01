from commands import commander

commands = open('input.txt', 'r').read()
commands_ = commands.split('\n')

output = ''
for command in commands_:
    result = commander(command)
    output = output + command + '\n' + result + '\n\n'

text_file = open("output.txt", "w")
text_file.write(output)
text_file.close()