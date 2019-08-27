import random
x = ['g','g','g']
l = random.randint(0,2)
x[l] = 'c'
#m = input("enter the door you want to choose")
#m = int(m) - 1

def goatdoor(r, b = []):
 j = 0
 while j < 3:
  if   j != r:
   if b[j] == 'g':
     return j
   else:
    j += 1
  else:
   j += 1

n =0
while n<1000:
 m = random.randint(0,2)
 q = goatdoor(m, x)
#print("door",q+1,"is a goatdoor")
#m = input("please re-enter or change your choice")
#m = int(m) - 1
 c = 0
 while c < 3: #switcher
  if c != m:
   if c != q:
    m = c
   else:
    c += 1
  else:
   c += 1
 if m == l:
  #print("you won!")
  print("Swtiched",'\t',"won")
 else:
  #print("better luck next time!")
   print("Swtiched",'\t',"lost")
 n += 1 