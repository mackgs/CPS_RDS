import numpy

import file_len
from analizer import analise
from syndrome import syndrome

index = 0

# parity check matrix
check = [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 1, 1, 0, 1, 1, 1, 0, 0],
         [0, 1, 0, 1, 1, 0, 1, 1, 1, 0],
         [0, 0, 1, 0, 1, 1, 0, 1, 1, 1],
         [1, 0, 1, 0, 0, 0, 0, 1, 1, 1],
         [1, 1, 1, 0, 0, 1, 1, 1, 1, 1],
         [1, 1, 0, 0, 0, 1, 0, 0, 1, 1],
         [1, 1, 0, 1, 0, 1, 0, 1, 0, 1],
         [1, 1, 0, 1, 1, 1, 0, 1, 1, 0],
         [0, 1, 1, 0, 1, 1, 1, 0, 1, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 1, 1, 1, 0, 1, 1, 1, 0, 0],
         [0, 1, 1, 1, 1, 0, 1, 1, 1, 0],
         [0, 0, 1, 1, 1, 1, 0, 1, 1, 1],
         [1, 0, 1, 0, 1, 0, 0, 1, 1, 1],
         [1, 1, 1, 0, 0, 0, 1, 1, 1, 1],
         [1, 1, 0, 0, 0, 1, 1, 0, 1, 1]]

syndromA = [1, 1, 1, 1, 0, 1, 1, 0, 0, 0]
syndromB = [1, 1, 1, 1, 0, 1, 0, 1, 0, 0]
syndromCa = [1, 0, 0, 1, 0, 1, 1, 1, 0, 0]
syndromCb = [1, 1, 1, 1, 0, 0, 1, 1, 0, 0]
syndromD = [1, 0, 0, 1, 0, 1, 1, 0, 0, 0]


# offset - symulacja błedów w kanale trans.

class Container:

    def __init__(self, data):
        self.data = data


PSN = Container('xxxxxxxx')
text1 = Container('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
text2 = Container('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
TA = Container('')
TP = Container('')
MS = Container('')
Day = Container('')
Month = Container('')
Year = Container('')
Hour=Container('')
Minutes=Container('')
LocalTimeOffset=Container('')

fileName = "rds_bits_samples\PR2_log2.txt"

bits_length = file_len.file_len(fileName) - 130

data = open(fileName).readlines()

detected_block_counter = 0

# convert notation to int (mapowanie)
for i in range(0, bits_length + 2):
    data[i] = int(float(data[i]))
# index - start of block A
while index < bits_length:
    # obliczamy syndromy kazdego z bloku
    syndrome_result = syndrome(index, data, check)
    if numpy.array_equal(syndrome_result, syndromA):

        syndrome_result = syndrome(index + 26, data, check)
        if numpy.array_equal(syndrome_result, syndromB):
            syndrome_result = syndrome(index + 52, data, check)

            if numpy.array_equal(syndrome_result, syndromCa):
                syndrome_result = syndrome(index + 78, data, check)

                if numpy.array_equal(syndrome_result, syndromD):
                    # inkrementacja licznika petli o dlugsc grupy -1
                    analise(index, data, PSN, text1, text2, TA, TP, MS, Day, Month, Year,Hour,Minutes,LocalTimeOffset)
                    index = index + 103

                    detected_block_counter = detected_block_counter + 1
                    # cała grupa znaleziona
            elif numpy.array_equal(syndrome_result, syndromCb):

                syndrome_result = syndrome(index + 78, data, check)
                if numpy.array_equal(syndrome_result, syndromD):

                    analise(index, data, PSN, text1, text2, TA, TP, MS, Day, Month, Year,Hour,Minutes,LocalTimeOffset)

                    index = index + 103
                    # index increament 104-1
                    detected_block_counter = detected_block_counter + 1

    index = index + 1
# loop increament
