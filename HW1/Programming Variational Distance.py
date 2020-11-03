# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 10:27:45 2020

@author: Jasmijn
"""

import math
import string
import re
import os

# open the inputfiles
eng_r = open(os.path.join("HW1", "data", "Alice_eng.txt"))
esp_r = open(os.path.join("HW1", "data", "Alice_esp.txt"), encoding = 'utf-8')
fin_r = open(os.path.join("HW1", "data", "Alice_fin.txt"))
ger_r = open(os.path.join("HW1", "data", "Alice_ger.txt"))
ita_r = open(os.path.join("HW1", "data", "Alice_ita.txt"))

# compile the input files to one lowercased string ([a-z] characters only)
eng = "".join(re.findall("[a-z]", eng_r.read().lower()))
esp = "".join(re.findall("[a-z]", esp_r.read().lower()))
fin = "".join(re.findall("[a-z]", fin_r.read().lower()))
ger = "".join(re.findall("[a-z]", ger_r.read().lower()))
ita = "".join(re.findall("[a-z]", ita_r.read().lower()))

# compute the total amount of characters for each language
tot_eng = len(eng)
tot_esp = len(esp)
tot_fin = len(fin)
tot_ger = len(ger)
tot_ita = len(ita)

# initialize dictionaries
dict_eng = {}
dict_esp = {}
dict_fin = {}
dict_ger = {}
dict_ita = {}

for c in "abcdefghijklmnopqrstuvwxyz":
    dict_eng[c] = 0
    dict_esp[c] = 0
    dict_fin[c] = 0
    dict_ger[c] = 0
    dict_ita[c] = 0

# count the occurrences of each character    
for c in eng:
    dict_eng[c] += 1
    
for c in esp:
    dict_esp[c] += 1
    
for c in fin:
    dict_fin[c] += 1

for c in ger:
    dict_ger[c] += 1

for c in ita:
    dict_ita[c] += 1
    
# compute the relative occurrence for each character
for key in dict_eng:
    dict_eng[key] = dict_eng[key] / tot_eng

for key in dict_esp:
    dict_esp[key] = dict_esp[key] / tot_esp
    
for key in dict_fin:
    dict_fin[key] = dict_fin[key] / tot_fin
    
for key in dict_ger:
    dict_ger[key] = dict_ger[key] / tot_ger
    
for key in dict_ita:
    dict_ita[key] = dict_ita[key] / tot_ita
    
# compute the variational distance
eng_esp = 0
for key in dict_eng:
    eng_esp += abs(dict_eng[key] - dict_esp[key])
eng_esp = eng_esp / 2
print("eng_esp : " + str(eng_esp))

eng_fin = 0
for key in dict_eng:
    eng_fin += abs(dict_eng[key] - dict_fin[key])
eng_fin = eng_fin / 2
print("eng_fin : " + str(eng_fin))

eng_ger = 0
for key in dict_eng:
    eng_ger += abs(dict_eng[key] - dict_ger[key])
eng_ger = eng_ger / 2
print("eng_ger : " + str(eng_ger))

eng_ita = 0
for key in dict_eng:
    eng_ita += abs(dict_eng[key] - dict_ita[key])
eng_ita = eng_ita / 2
print("eng_ita : " + str(eng_ita))

esp_fin = 0
for key in dict_esp:
    esp_fin += abs(dict_esp[key] - dict_fin[key])
esp_fin = esp_fin / 2
print("esp_fin : " + str(esp_fin))

esp_ger = 0
for key in dict_esp:
    esp_ger += abs(dict_esp[key] - dict_ger[key])
esp_ger = esp_ger / 2
print("esp_ger : " + str(esp_ger))

esp_ita = 0
for key in dict_esp:
    esp_ita += abs(dict_esp[key] - dict_ita[key])
esp_ita = esp_ita / 2
print("esp_ita : " + str(esp_ita))

fin_ger = 0
for key in dict_fin:
    fin_ger += abs(dict_fin[key] - dict_ger[key])
fin_ger = fin_ger / 2
print("fin_ger : " + str(fin_ger))

fin_ita = 0
for key in dict_fin:
    fin_ita += abs(dict_fin[key] - dict_ita[key])
fin_ita = fin_ita / 2
print("fin_ita : " + str(fin_ita))

ger_ita = 0
for key in dict_ger:
    ger_ita += abs(dict_ger[key] - dict_ita[key])
ger_ita = ger_ita / 2
print("ger_ita : " + str(ger_ita))

print("")

# compute the collision probabilities
cp_eng = 0
for key in dict_eng:
    cp_eng += dict_eng[key]**2 
print("cp_eng : " + str(cp_eng))

cp_esp = 0
for key in dict_esp:
    cp_esp += dict_esp[key]**2 
print("cp_esp : " + str(cp_esp))

cp_fin = 0
for key in dict_fin:
    cp_fin += dict_fin[key]**2 
print("cp_fin : " + str(cp_fin))

cp_ger = 0
for key in dict_ger:
    cp_ger += dict_ger[key]**2 
print("cp_ger : " + str(cp_ger))

cp_ita = 0
for key in dict_ita:
    cp_ita += dict_ita[key]**2 
print("cp_ita : " + str(cp_ita))

print("")

# read the permutation file
perm_r = open(os.path.join("HW1", "data", "permuted_cipher.txt"), encoding = 'utf-8')
perm = "".join(re.findall("[a-z]", perm_r.read().lower()))

# compute the relative occurrence of each character
tot_perm = len(perm)

dict_perm = {}
for c in "abcdefghijklmnopqrstuvwxyz":
    dict_perm[c] = 0

for c in perm:
    dict_perm[c] += 1
    
for key in dict_perm:
    dict_perm[key] = dict_perm[key] / tot_perm
    
# compute the variational distances
perm_eng = 0
for key in dict_perm:
    perm_eng += abs(dict_perm[key] - dict_eng[key])
perm_eng = perm_eng / 2
print("perm_eng : " + str(perm_eng))

perm_esp = 0
for key in dict_perm:
    perm_esp += abs(dict_perm[key] - dict_esp[key])
perm_esp = perm_esp / 2
print("perm_esp : " + str(perm_esp))

perm_fin = 0
for key in dict_perm:
    perm_fin += abs(dict_perm[key] - dict_fin[key])
perm_fin = perm_fin / 2
print("perm_fin : " + str(perm_fin))

perm_ger = 0
for key in dict_perm:
    perm_ger += abs(dict_perm[key] - dict_ger[key])
perm_ger = perm_ger / 2
print("perm_ger : " + str(perm_ger))

perm_ita = 0
for key in dict_perm:
    perm_ita += abs(dict_perm[key] - dict_ita[key])
perm_ita = perm_ita / 2
print("perm_ita : " + str(perm_ita))

print("")

# collision probability perm
cp_perm = 0
for key in dict_perm:
    cp_perm += dict_perm[key]**2 
print("cp_perm : " + str(cp_perm))










