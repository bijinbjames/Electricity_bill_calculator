old=int(input("Enter the old KWh value "))

new=int(input("Enter the new KWh value "))

value=new-old

print(value)

if value<=50:

  print(value*3.15,"rupee is your electricity bill")

if value>=51 and value<=100:

  print((50*3.15)+(value-50)*3.70,"rupee is your electricity bill")

if value>=101 and value<=150:

  print((50*3.15)+(100-50)*3.70+(value-100)*4.80,"rupee is your electricity bill")

if value>=151 and value<=200:

  print((50*3.15)+(100-50)*3.70+(150-100)*4.80+(value-150)*6.40,"rupee is your electricity bill")

if value>=201 and value<=250:

  print((50*3.15)+(100-50)*3.70+(150-100)*4.80+(200-150)*6.40+(value-200)*7.60,"rupee is your electricity bill")



if value>=251:

  print((50*3.15)+(100-50)*3.70+(150-100)*4.80+(200-150)*6.40+(value-200)*7.60,"rupee is your electricity bill")
