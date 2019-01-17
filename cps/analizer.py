import julian as julian
import numpy
from numpy import fix

from dispAllElements import dispAllElements
from locate_it import locate_it
from binArrayToChar import vbin2char
from binArrayToDec import vbin2dec


# analize of 26 bits
def analise(index, data, PSN, text1, text2, TA, TP, MS, Day, Month, Year,Hour,Minutes,LocalTimeOffset):
    # print("analize")
    # pobieramy bity blokow danych
    blockA = data[index: index + 25]
    blockB = data[index + 26: index + 51]
    blockC = data[index + 52: index + 77]
    blockD = data[index + 78: index + 103]
    groupType = blockB[0:5]
    # print(groupType)
    # znajdujemy blok programowy rzetwarzajacy grupe
    if numpy.array_equal(groupType[0:4], [0, 0, 0, 0]):
        # print("GrupaA");
        TP.data = blockB[5]
        TA.data = blockB[11]
        MS.data = blockB[12]  # Music Speech switch
        array = [0, 0, 0]
        for i in blockB[6:11]:
            array.append(i)



        seg_addr = blockB[14:16]
        # adres segmentu

        ascii_1 = blockD[0:8]
        ascii_2 = blockD[8:16]

        char_1 = vbin2char(ascii_1)  # bin -> char
        char_2 = vbin2char(ascii_2)  # bin -> char

        if numpy.array_equal(seg_addr, [0, 0]):
            s = list(PSN.data)
            s[0] = char_1
            s[1] = char_2
            PSN.data = "".join(s)
        elif numpy.array_equal(seg_addr, [0, 1]):
            s = list(PSN.data)
            s[2] = char_1
            s[3] = char_2
            PSN.data = "".join(s)
            # PSN[2:4]=[char_1,char_2]
        elif numpy.array_equal(seg_addr, [1, 0]):

            s = list(PSN.data)
            s[4] = char_1
            s[5] = char_2
            PSN.data = "".join(s)

        elif numpy.array_equal(seg_addr, [1, 1]):
            s = list(PSN.data)

            s[6] = char_1
            s[7] = char_2
            PSN.data = "".join(s)
    #  8 bits for PSN
    elif numpy.array_equal(groupType[0:4], [0, 0, 1, 0]):
        text_seg = blockB[12:16]
        #  A/B flag
        AB_flag = blockB[11]
        ascii_1 = blockC[0:8]
        ascii_2 = blockC[9:16]
        ascii_3 = blockD[0:8]
        ascii_4 = blockD[8:16]

        char_1 = vbin2char(ascii_1)
        char_2 = vbin2char(ascii_2)
        char_3 = vbin2char(ascii_3)
        char_4 = vbin2char(ascii_4)

        chars = [char_1, char_2, char_3, char_4]
        result = locate_it(chars, text_seg, AB_flag, text1.data, text2.data)
        text1.data = result[0]
        text2.data = result[1]

    elif numpy.array_equal(groupType, [0, 1, 0, 0, 0]):

        # GRUPA 4A
        dateArray = [0, 0, 0, 0, 0, 0, 0]
        for i in blockB[14:16]:
            dateArray.append(i)
        for i in blockC[0:15]:
            dateArray.append(i)

        MJD = vbin2dec(dateArray)

        date = julian.from_jd(MJD, fmt='mjd')
        Year.data = date.year
        Month.data = date.month
        Day.data = date.day



        hourArray = [0, 0, 0]
        hourArray.append(blockC[15])
        for i in blockD[0:4]:
            hourArray.append(i)

        Hour.data = vbin2dec(hourArray)

        minutesArray = [0, 0]
        for i in blockD[4:10]:
            minutesArray.append(i)

        Minutes.data = vbin2dec(minutesArray)

        offsetArray = [0, 0, 0]
        for i in blockD[11:16]:
            minutesArray.append(i)

        LocalTimeOffset.data = (vbin2dec(offsetArray)) / 2 # LocalTimeOffset



    dispAllElements(groupType, PSN, text1, text2, TA, TP, MS, Day, Month, Year,Hour,Minutes,LocalTimeOffset)
