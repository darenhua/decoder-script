import numpy as np

hexadecimal = "2A6835740F7532760E6F336E2F1A39F63AE436FA0F6738A32E9C3AE637ED3635"
#hexadecimal = "2A4825540F472B231E9C2CCA26CE1428"
sep_hex = []
joined_hex = []
bin_list = []
cut_pasted = []
byte_listA = []
byte_listB = []


#seperate hex string into chunks of 4 hex code
for i, j in enumerate(hexadecimal):
    if i%4==0:
        sep_hex.append([j])
    else:
        sep_hex[i//4].append(j)

for i in sep_hex:
    joined = ''.join(i)
    joined_hex.append(joined)

#print("Hexadecimal \n", joined_hex, sep='')
print("Hexadecimal \n", '\n'.join(joined_hex), sep='')

end_length = len(joined_hex[0]) * 4
list_length = len(joined_hex)
#hex to binary
for i in joined_hex:
    int_hex = int(i, 16)
    bin_hex = bin(int_hex)
    padded_bin = bin_hex[2:].zfill(end_length)
    bin_list.append(padded_bin)


#print("Binary Original \n", bin_list, sep='')
print("Binary Original \n", '\n'.join(bin_list), sep='')

set_length = len(bin_list)//2
first_set = bin_list[:set_length]
sec_set = bin_list[set_length:]

#cut and paste: 0th column -> 8th column, all positions after 8 shifted 1
#set 1
first_cut = [np.zeros(end_length) for i in first_set]
sec_cut = [np.zeros(end_length) for i in sec_set]

for i in range(len(first_set)):
    for j in range(end_length):
        if 9>j>0:
            first_cut[i][j] = first_set[i][j+1]
        elif j>=9:
            first_cut[i][j] = first_set[i][j]
        elif j == 0:
            first_cut[i][0] = first_set[i][j+1]
        first_cut[i][8] = first_set[i][0]

        #tempA = first_cut[i][8]
        #first_cut[i][8] = first_cut[i][9]
        #first_cut[i][9] = tempA
    first_cut[i] = first_cut[i].tolist()
    for k in range(end_length):
        first_cut[i][k] = int(first_cut[i][k])
        first_cut[i][k] = str(first_cut[i][k])
    first_cut[i] = ''.join(first_cut[i])

for i in range(len(sec_set)):
    for j in range(end_length):
        if 9>j>0:
            sec_cut[i][j] = sec_set[i][j+1]
        elif j>=9:
            sec_cut[i][j] = sec_set[i][j]
        elif j == 0:
            sec_cut[i][0] = sec_set[i][j+1]

        sec_cut[i][8] = sec_set[i][0]

        #tempB= sec_cut[i][8]
        #sec_cut[i][8] = sec_cut[i][9]
        #sec_cut[i][9] = tempB
    sec_cut[i] = sec_cut[i].tolist()
    for k in range(end_length):
        sec_cut[i][k] = int(sec_cut[i][k])
        sec_cut[i][k] = str(sec_cut[i][k])
    sec_cut[i] = ''.join(sec_cut[i])

#print("Cut and pasted Set1\n", first_cut,sep='')
#print("Cut and pasted Set2",sec_cut,sep='')
print("Cut and pasted Set1\n", '\n'.join(first_cut), sep='')
print("Cut and pasted Set2\n", '\n'.join(sec_cut), sep='')

#seperate 16 bit binary to 2 8 bit arrays
#set1
for i in first_cut:
    first_byteA = i[0:8]
    sec_byteA = i[8:16]
    byte_listA.append([first_byteA,sec_byteA])
#set2
   
for i in sec_cut:
    first_byteB = i[0:8]
    sec_byteB = i[8:16]
    byte_listB.append([first_byteB,sec_byteB])

print("Seperated into bytes Set1\n", '\n'.join(['\t'.join([str(cell) for cell in row]) for row in byte_listA]), sep='')
print("Seperated into bytes Set2\n", '\n'.join(['\t'.join([str(cell) for cell in row]) for row in byte_listB]), sep='')

#print("Seperated into bytes Set1\n", byte_listA)
#print("Seperated into bytes Set2\n", byte_listB)

subtracted_listA = byte_listA
subtracted_listB = byte_listB

#odd subtact -> if odd index, subtract value equal to row number
#even add -> if even index, add value equal to row number
#set1
for i,j in enumerate(byte_listA):
    for k in range(len(j)):
        decimal_evenA = int(byte_listA[i][k],2)
        if i%2 == 0:
            subtractedA = decimal_evenA + i
            subtracted_binA = bin(subtractedA)
            padded_subtractA = subtracted_binA[2:].zfill(8)
            subtracted_listA[i][k] = padded_subtractA
        else:
            subtracted_listA[i][k] = byte_listA[i][k]
print("Added by even row number Set 1\n", '\n'.join(['\t'.join([str(cell) for cell in row]) for row in subtracted_listA]), sep='')
       
#print("Added by even row number Set 1\n", subtracted_listA)
added_listA = subtracted_listA

for i,j in enumerate(byte_listA):
    for k in range(len(j)):
        decimal_oddA = int(byte_listA[i][k],2)
        if i%2 != 0:
            addedA = decimal_oddA - i
            added_binA = bin(addedA)
            padded_addA = added_binA[2:].zfill(8)
            added_listA[i][k] = padded_addA
print("Subtracted by odd row number Set1\n", '\n'.join(['\t'.join([str(cell) for cell in row]) for row in added_listA]), sep='')

#print("Subtracted by odd row number Set1\n", added_listA)
#set2
for i,j in enumerate(byte_listB):
    for k in range(len(j)):
        decimal_evenB = int(byte_listB[i][k],2)
        if i%2 == 0:
            subtractedB = decimal_evenB + i
            subtracted_binB = bin(subtractedB)
            padded_subtractB = subtracted_binB[2:].zfill(8)
            subtracted_listB[i][k] = padded_subtractB
        else:
            subtracted_listB[i][k] = byte_listB[i][k]
print("Added by even row number Set 2\n", '\n'.join(['\t'.join([str(cell) for cell in row]) for row in subtracted_listB]), sep='')
       
#print("Added by even row number Set 2\n", subtracted_listB)
added_listB = subtracted_listB

for i,j in enumerate(byte_listB):
    for k in range(len(j)):
        decimal_oddB = int(byte_listB[i][k],2)
        if i%2 != 0:
            addedB = decimal_oddB - i
            added_binB = bin(addedB)
            padded_addB = added_binB[2:].zfill(8)
            added_listB[i][k] = padded_addB
print("Subtracted by odd row number Set2\n", '\n'.join(['\t'.join([str(cell) for cell in row]) for row in added_listB]), sep='')

#print("Subtracted by odd row number Set2\n", added_listB)
raster_asciiA = added_listA
raster_asciiB = added_listB
#binary to ascii
for counter, row in enumerate(added_listA):
    for count, byte in enumerate(row):
        decimalA = int(byte,2)
        ascii_charA = chr(decimalA)
        raster_asciiA[counter][count] = ascii_charA
        
#print("Convert to Raster Ascii Set1 \n", raster_asciiA)
print("Convert to Raster Ascii Set1 \n", '\n'.join(['\t'.join([str(cell) for cell in row]) for row in raster_asciiA]), sep='')

for counter,row in enumerate(added_listB):
    for count, byte in enumerate(row):
        decimalB = int(byte,2)
        ascii_charB = chr(decimalB)
        raster_asciiB[counter][count] = ascii_charB
        
#print("Convert to Raster Ascii Set1\n", raster_asciiB)
print("Convert to Raster Ascii Set2 \n", '\n'.join(['\t'.join([str(cell) for cell in row]) for row in raster_asciiB]), sep='')

#raster to complete string
complete_string = ''
for i in raster_asciiA:
    for j in i:
        complete_string += j
        
for i in raster_asciiB:
    for j in i:
        complete_string += j
print("Final Decoded\n", complete_string, sep='')
