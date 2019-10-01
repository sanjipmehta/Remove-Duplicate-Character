s=input("Enter the Duplicate String:")
out=[]
for i in s:
	if i not in out:
		out.append(i)
final=''.join(out)
print(final)