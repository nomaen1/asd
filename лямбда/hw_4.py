names = ["azat", "zina", "kuma", "anna", "sas"]
lambda_names = list(filter(lambda name: name == name[::-1], names))
print(lambda_names)
