import math


print("Polymer Surface Energy Calculation by Group Contribution")
#purpose of the code

print("    ")
#space



print("How many functional carbon groups are there?")
#what it's asking for

c=int(input("Enter the number of carbon groups: "))
#input for number of carbon groups

print("    ")
#space



print("How many CH2 groups are in your polymer?")
#letting you know what it's asking for

ch2 = int(input("Enter the number of CH2 groups: "))
#input for CH2 groups

print("    ")
#space



print("How many CH groups are in your polymer?")
#what this line is asking for

ch=int(input("Enter the number of CH groups: "))
#input for CH groups

print("    ")
#space



print("How many CH3 groups are in your polymer?")
#what this line is asking for

ch3=int(input("Enter the number of CH3 groups: "))
#input for CH3 groups

print("    ")
#space


print("How many COO groups are in your polymer?")
#what this line is asking for

coo=int(input("Enter the number of COO groups: "))
#input for COO groups

print("    ")
#space


print("How many CHCl groups are in your polymer?")
#what this line is asking for

chcl=int(input("Enter the number of CHCl groups: "))
#input for CHCl groups

print("    ")
#space


print("How many CF3 groups are in your polymer?")
#what this line is asking for

cf3=int(input("Enter the number of CF3 groups: "))
#input for CF3 groups

print("    ")
#space


print("How many CF2 groups are in your polymer?")
#what this line is asking for

cf2=int(input("Enter the number of CF2 groups: "))
#input for CF2 groups

print("    ")
#space


print("How many CH2OH groups are in your polymer?")
#what this line is asking for

ch2oh=int(input("Enter the number of CH2OH groups: "))
#input for CH2OH groups

print("    ")
#space


print("How many CHOH groups are in your polymer?")
#what this line is asking for

choh=int(input("Enter the number of CHOH groups: "))
#input for CHOH groups

print("    ")
#space


print("How many COH groups are in your polymer?")
#what this line is asking for

coh=int(input("Enter the number of COH groups: "))
#input for COH groups

print("    ")
#space

s=((ch2*30.8)+(ch*63.3)+(ch3*(-6.4))+(coo*74.8)+(chcl*70.8)+(cf3*(-27.3))+(cf2*21.4)+(ch2oh*47.5)+(choh *72)+(coh*104))/(c)
#homopolymer surface energy calculation via Calculation of Hamaker constant (Vial et al)

print ("homopolymer surface energy =")
#what is going to be displayed as a result
print("    ")
#space

print(s)
#surface energy calculation







