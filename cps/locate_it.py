def locate_it(chars, text_seg, AB_flag, text1, text2):
    first = (text_seg[0] * 8 + text_seg[1] * 4 + text_seg[2] * 2 + text_seg[3]) * 4 + 1;
    if AB_flag == 0 :

       
        s=list(text1)


        s[first-1]=chars[0]
        s[first]=chars[1]
        s[first+1]=chars[2]
        s[first+2]=chars[3]
        text1="".join(s)
    else:
        s = list(text2)
        s[first-1] = chars[0]
        s[first] = chars[1]
        s[first + 1] = chars[2]
        s[first + 2] = chars[3];
        text2 = "".join(s)

    textA = text1
    textB = text2

    return [textA,textB]
