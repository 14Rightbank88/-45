countnumbers = int(input('Please enter the Total Number of list Elements: '))
listnumbers = []
for i in range(countnumbers):
  i +=1
  Element = int(input('Please enter the Value {0} of Element: '.format(i)))
  if Element != 0:
    if Element % 2 == 0:
      listnumbers.append(Element)
print(listnumbers)
