s = "python programming lang object oriented programming dynamic typed"
vowels = "aeiouAEIOU"

acount_freq = 0
ccount_freq = 0
wc = 0

for i in s:
    if i == " ":
        wc += 1
    elif i in vowels:
        acount_freq += 1
    else:
        ccount_freq += 1

print("Vowel count:", acount_freq)
print("Consonant count:", ccount_freq)
print("Word count:", wc + 1)