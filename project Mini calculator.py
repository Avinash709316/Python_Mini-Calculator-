#Mini Calculator
print("Mini Calculator")
print("Operations :   ")
var_1 = print("Seq_1.)Addition \t Seq_2.)Subtraction \t Seq_3.) Multiplication \tSeq_4.)Division \t Seq_5.) Percentage \nSeq_6.)Square root \t Seq_7.)Cube root")
var2= int(input("Enter the sequence of operation = "))

if var2==1:
    print("Addition")
    a1=int(input("Enter 1st value : "))
    a2=int(input("Enter 2nd value : "))
    a3=a1+a2
    print("result : ",a3)

if var2==2:
    print("Subtraction")
    b1=int(input("Enter 1st value : "))
    b2=int(input("Enter 2nd value : "))
    b3=b1-b2
    print("result : ",b3)

if var2==3:
    print("Multiplication")
    c1=int(input("Enter 1st value : "))
    c2=int(input("Enter 2nd value : "))
    c3=c1*c2
    print("result : ",c3)

if var2==4:
    print("Division")
    d1=int(input("Enter 1st value : "))
    d2=int(input("Enter 2nd value : "))
    d3=d1/d2
    print("result : ",d3)

if var2==5:
    print("Percentage")
    e1=int(input("Enter 1st value : "))
    e2=int(input("Enter 2nd value : "))
    e3=e1%e2
    print("result : ",e3)

if var2==6:
    print("Square root")
    f1=int(input("Enter the value for which you want find Sqr root : "))
    f2=f1**2
    print("result : ",f2)

if var2==7:
    print("Cube root")
    g1=int(input("Enter the value for which you want find Sqr root : "))
    g2=g1**3
    print("result : ",g2)

else:
    print("Entered Invalid sequence please enter the correct sequence")

if var2>8:
    print("Entered Invalid sequence please enter the correct sequence")


        
    



     
    



        

    

    
        
           
    
    




