n=int(input("Total number of students : "));

for i in range(n):
    name=(input("Enter your name : "));
    clas=(input("Enter your class : "));
    height=(input("Enter your height : "));
    weight=(input("Enter your weight : "));
    prefsport=(input("Enter your preferred sport : "));
    
    if height>160:
        if weight>80:
            print("Most Appropriate sport : Chess");
        else if weight>75 && weight<85::
            print("Most Appropriate sport : Cricket");
    
    else if height>165:
         if weight>75 && weight<85:
            print("Most Appropriate sport : Cricket");
        else if weight>65 && weight<75::
            print("Most Appropriate sport : Football");
      
    else if height>170:
         if weight>75 && weight<85:
            print("Most Appropriate sport : Cricket");
        else if weight>65 && weight<75::
            print("Most Appropriate sport : Javelin Throw");
    
            
