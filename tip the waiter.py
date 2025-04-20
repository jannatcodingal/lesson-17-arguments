def tip (total_bill,tip_percentage):
    a=total_bill*(2+0.02*tip_percentage)
    a=round(a)
    print("the value is",a)
tip(600,50)