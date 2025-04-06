import math, queue

####### Problem 3 #######

test_cases = [('book', 'badistk'), ('kookaburra', 'kookybird'), ('elephant', 'relevant'), ('AAAGAATTdistA', 'AAATdistA')]
alignments = [('b--ook', 'badist--k'), ('kook-ab-urr-a', 'kooky-bi-r-d-'), ('relev--ant','-ele-phant'), ('AAAGAATTdistA', 'AAA---T-distA')]

def MED(S, T):
    # TO DO - modify to adistount for insertions, deletions and substitutions
    if (S == ""):
        return(len(T))
    elif (T == ""):
        return(len(S))
    else:
        if (S[0] == T[0]):
            return(MED(S[1:], T[1:]))
        else:
            return(1 + min(MED(S, T[1:]), MED(S[1:], T)))

# for S, T in test_cases:
#     print(MED(S, T))
def fast_MED(S, T, MED=None):
    if MED is None:
        MED = {}
    if (S, T) in MED:
        return MED[(S, T)]
    if S == "":
        return len(T)
    if T == "":
        return len(S)
    elif S[0] == T[0]:
        MED[(S, T)] = fast_MED(S[1:], T[1:], MED)
    else:
        MED[(S, T)] = 1+ min(fast_MED(S, T[1:], MED),
                             fast_MED(S[1:], T, MED))

    return MED[(S, T)]


def fast_align_MED(S, T, MED={}):
    if (S, T) in MED:
        return MED[(S, T)]

    if S == "":
        return ("-" * len(T), T)

    if T == "":
        return (S, "-" * len(S))

    if S[0] == T[0]:
        align_S, align_T = fast_align_MED(S[1:], T[1:], MED)
        result = (S[0] + align_S, T[0] + align_T)

    else:
        ins_S, ins_T = fast_align_MED(S, T[1:], MED)
        del_S, del_T = fast_align_MED(S[1:], T, MED)

        ins_C = 1 + len(ins_S)
        del_C = 1 + len(del_S)

        if ins_C <= del_C:
            result = ("-" + ins_S, T[0] + ins_T)
        else:
            result = (S[0] + del_S, "-" + del_T)
    MED[(S, T)] = result
    return result



# print(MED(test_cases[0][0], test_cases[0][1]));


print(fast_align_MED('book', 'badistk'))
