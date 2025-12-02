with open("requirements.txt") as f:
    lines = [line.strip() for line in f.readlines()]

requirements = []
for line in lines:
    requirements.append(line.split()[0])

with open("requirements.txt", "w") as e:
    for requirement in requirements:     
        e.write(requirement + "\n")