import hashlib

# 1 - Verificar os algoritmos disponíveis
print(hashlib.algorithms_available)

# 2 - Algoritmos disponíveis de acordo com o SO
print(hashlib.algorithms_guaranteed)

# 3 - Utilizando o Sha256
algorithm = hashlib.sha256()
print(algorithm.digest())
message = "Um dia eu serei rei dos piratas!".encode()
algorithm.update(message)
print(algorithm.hexdigest())

# 4 - Utilizando o MD5
md5 = hashlib.md5()
md5.update(message)
print(md5.hexdigest())
