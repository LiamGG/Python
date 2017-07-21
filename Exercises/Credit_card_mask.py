# Credit card mask
# 7 kyu

# Your task is to write a function maskify, which changes all but the last four characters into '#'.

def maskify(cc):
    if len(cc) <= 4:
        return cc
    else:
        mask = (len(cc)-4)*'#' + cc[-4:]
        return mask
