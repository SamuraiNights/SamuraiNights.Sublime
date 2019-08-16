import string
for i in range(1,101,1):
	print(" ")
print("Hi")
print(" ")
d = input("Write your essay, dude: ")
d = d.lower()
d_exclude = set(string.punctuation)
d = ''.join(ch for ch in d if ch not in d_exclude)
d_split = d.split()
freq = {}
for i in range(len(d_split)):
	word = d_split[i]
	if word not in freq:
		freq[word] = 0
	freq[word] += 1
print("Here's yo word count: ")
for word in freq:
	print(word + ": " + str(freq[word]))