import yaml
with open('simple.yml', 'r') as file:
    prime_service = yaml.safe_load(file)
print(prime_service)





"""dict={
    'name':"Rushi"
}

with open("simple.yml","w") as ym:
    ym.dump()"""