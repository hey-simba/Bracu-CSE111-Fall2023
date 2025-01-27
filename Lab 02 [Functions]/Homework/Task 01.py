

def hospital_fee(**dic):
    max_fee = 0
    max_person = ''
    for person, fee in dic.items():
        if max_fee<= fee:
            max_fee = fee
    for person,fee in dic.items():
        if max_fee == fee:
            max_person += person + ', '
    return max_fee, max_person[:-2]
max_amount, max_player = hospital_fee(Neymar = 1000, Dembele = 600, Reus = 500, Bale = 1000)
print(f'Highest fee was {max_amount} tk which was paid by {max_player}.')