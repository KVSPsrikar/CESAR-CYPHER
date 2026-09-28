alphabets=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

originaltext=str(input("enter the word to encrypt"))
shiftamount=int(input("enter the jump to encrypt"))
ENCODEorDECODE=input("enter encode or decode")


def cesar(originaltext,shiftamount,ENCODEorDECODE):
    outputtext=""
    for i in originaltext:
        if ENCODEorDECODE=="encode":
            shifted=alphabets.index(i) + shiftamount
        else:
            shifted=alphabets.index(i) - shiftamount

        shifted %= len(alphabets)
        
        outputtext+= alphabets[shifted]
    print(outputtext)
cesar(originaltext,shiftamount,ENCODEorDECODE)

