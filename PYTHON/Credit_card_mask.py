# Credit card mask
# 7 kyu

def maskify(cc):

    if len(cc) <= 4:
        return cc
    else:
        mask = (len(cc)-4)*'#' + cc[-4:]
        return mask
