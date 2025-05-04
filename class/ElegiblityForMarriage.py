class ElegiblityForMarriage():
    def eligible(gender, age):
        if(gender == "Male"):
            if(age > 21):
                print("Eligible")
            else:
                print("Not Eligible")
        elif(gender == "Female"):
            if(age > 18):
                print("Eligible")
            else:
                print("Not Eligible")
        else:
            print("Invalid Entry")