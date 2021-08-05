alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
typ = input("Type encode or decode \n") 
txt = input("Enter the text \n")
shift = int(input("Enter the shift number \n"))

def ciper(type_txt,cp_text, shift_number):
  strr = ''
  for letter in cp_text:
    position = alphabet.index(letter)
    if(type_txt == 'decode'):
      new_pos = position-shift_number
    else:
      new_pos = position+shift_number
    new_ltr = alphabet[new_pos]
    strr += new_ltr
  print(strr)





ciper(type_txt = typ, cp_text=txt, shift_number=shift)
  