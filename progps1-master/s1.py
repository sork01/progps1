# Mikael Forsberg <miforsb@kth.se>
# Robin Gunning <rgunning@kth.se>
# Skapad 20151019

def dna():          # uppgift 1
    return "^[ACGT]+$"

def sorted():       # uppgift 2
    return "^9*8*7*6*5*4*3*2*1*0*(?<=\d)$"

def hidden1(x):     # uppgift 3
# indata x är strängen som vi vill konstruera ett regex för att söka efter
    return x

def hidden2(x):     # uppgift 4
# indata x är strängen som vi vill konstruera ett regex för att söka efter
    return ".*?".join(list(x))

def equation():     # uppgift 5
    return "^[+-]?\d+([+*/-]\d+)*(=[+-]?\d+([+*/-]\d+)*)?$"

def parentheses():  # uppgift 6
    return "^(\((\((\((\((\(\))*\))*\))*\))*\))+$"

def sorted3():      # uppgift 7
    return "^\d*(01[2-9]|[0-1]2[3-9]|[0-2]3[4-9]|[0-3]4[5-9]|[0-4]5[6-9]|[0-5]6[7-9]|[0-6]7[8-9]|[0-7]89)\d*$"
