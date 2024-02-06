price=99.99 #a
discountpercent=25 #b
markdown=(discountpercent/100)*price #c
newprice=price-markdown #d
print ("Price=",round (newprice,2))