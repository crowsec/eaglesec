import subprocess

for linha in open('command.txt', 'r') :
    subprocess.run(linha.split(" ")[:-1])