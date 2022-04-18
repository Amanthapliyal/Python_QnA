s= 'URRRLLDDUDR'
countX=0
countY=0
for i in range(len(s)):
	if s[i]=='R':
		countY+=1
	elif s[i]=='L':
		countY-=1
	elif s[i]=='U':
		countX+=1
	elif s[i]=='D':
		countX-=1
count = 0
if countX>0 and countY>0:
	count = len(s)-countX-countY
if countX<0 and countY<0:
	count = len(s)-(-countX)-(-countY)
if countX>0 and countY<0:
	count = len(s)-countX-(-countY)
if countX<0 and countY>0:
	count = len(s)-(-countX)-(countY)
print(count)