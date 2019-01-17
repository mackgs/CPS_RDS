import numpy

from binArrayToDec import vbin2dec

TrafficApps = ["This programme does not carry traffic announcements nor does it refer,via EON,to a programme That does",
               "This programme carries EON information about another programme which gives traffic information",
               "This programme carries traffic announcements but none are being broadcast at present and may also carry EON information About other traffic announcements",
               "A traffic announcement is being broadcast on this programme at present"]


def dispAllElements(type, PSN, text1, text2, TA, TP, MS, Day, Month, Year, Hour, Minutes, LocalTimeOffset):
    if numpy.array_equal(type[0:4], [0, 0, 0, 0]):
        # print(type)
        if type[4] == 0:
            print("Group 0A detected:")

        else:
            print("Group 0b detected:")

        print("PSN: " + PSN.data)
        TATP = vbin2dec([0, 0, 0, 0, 0, 0, TP.data, TA.data])
        print("TATP: " + TrafficApps[TATP])
        if MS.data:
            print("MS: Music")
        else:
            print("MS: Speech")
        print("\n")

    elif numpy.array_equal(type[0:4], [0, 0, 1, 0]):
        if type[4] == 0:
            print("Group 2A detected:")
        else:
            print("Group 2A detected:")

        print("Radio Text1 : " + text1.data)
        print("Radio Text2 : " + text2.data)
        print("\n")
    elif numpy.array_equal(type, [0, 1, 0, 0, 0]):
        print("Date: " + str(int(Day.data)) + "/" + str(int(Month.data)) + "/" + str(int(Year.data)) + "  " + str(
            Hour.data) + ":" + str(Minutes.data) + " +" + str(LocalTimeOffset.data))
        print("\n")
