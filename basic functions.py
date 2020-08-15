#some basic functions
def check_parity (v):
    num = v.count('1')
    if num%2 == 0:
        parity = 1
    else:
        parity = -1
    return parity

def get_probability_distribution(counts):
    output_distr = {}
    output_distr.update({ v: counts[v]/NUM_SHOTS for v in counts.keys() })
    return output_distr
