import csv
from datetime import datetime
import time
import matplotlib.pyplot as plt
import numpy as np



c = 299792458 #Speed of light


def read_dopplercomp_file(filename):
    # Read tle-based predicted doppler pre-compensation file from Radio and do a conversion from velocity to frequency  
    data = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            timestamp = int(row[0])
            dp_shift = calculate_doppler_shift(float(row[1]))
            data.append((timestamp, dp_shift))
    return data



def calculate_doppler_shift( v, f = 2053.5*10**6):
    # Calculate doppler shift from velocity
    return f * (v / c)


def read_csv_file(filename):
    # 
    data = []
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
           
          
            timestamp_str = row[1]  # Assuming timestamp is at index 1
            timestamp = datetime.strptime(timestamp_str, '%b.%d.%Y %I:%M:%S.%f %p')
            posix_time = int(timestamp.timestamp())
            posix_time = posix_time +50
            data.append((posix_time, row[6:]))  # Store tuple of (posix_time, data)
    return data

def merge(list1, list2):
    # Merge two lists into a corresponding list of tuples
    return [(list1[i], list2[i]) for i in range(0, len(list1))]
     

def find_max_aplitude_index(data_tuple):
    # Find the index of the sample in trace with highest aplitude. 

    values_list = data_tuple[1]  # Extract the list of values from the tuple
    timestamp = data_tuple[0]
    highest_value = float(values_list[0])  # Initialize with the first value
    highest_index = 0

    for i in range(1, len(values_list)):
        value = float(values_list[i])
        if value > highest_value:
            highest_value = value
            highest_index = i

    timestamp_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestamp))
    result_tuple = (highest_value, highest_index)

    return result_tuple, timestamp

# Usage example
filename = 'measurement_14-06-23.csv'
data = read_csv_file(filename)


start = 69950000
end = 70050000
num_points = 1001

step = (end - start) / (num_points - 1)
freq = [start + step * i for i in range(num_points)]


#freq = range(69958100, 70050000 ,255)
res = ()
f = []
ts = []
print(len(data))
for row in data: 
    res= find_max_aplitude_index(row)
    first_tuple = res[0]
    idx = first_tuple[1]
   

    ts.append(res[1])
    f.append(freq[idx]-70e6)
    print(len(f))

"""
d = read_dopplercomp_file('AWSTEST_SG223.csv')
#print (d)
time_doppler=[]
freq_doppler=[]
for elem in d: 
    time_doppler.append(elem[0] -10000 + 2500 +310)
    freq_doppler.append(elem[1])

print(time_doppler, freq_doppler)
plt.plot(time_doppler, freq_doppler, marker='.', linestyle='-', color='red', label='Frequecy shift calculated by qRadio (TLE-based)')

# Set labels and title
plt.xlabel('Time')
plt.ylabel('Freq_Offset')

plt.title('Doppler Offset on qRadio')

"""



# Display the plot
for elem in ts:
    print(elem)

# Plot the numbers
g1 = ts


#plt.plot(g1, f, marker='.', linestyle='-', color='blue', label='Measured frequency shift')

# Set labels and title
#plt.xlabel('POSIX time[s]')
#plt.ylabel('Freq_Offset [Hz]')
#plt.title('Doppler Offset')
#plt.grid()

#plt.legend()
# Display the plot





#####





res = []
filename = 'AWS-doppler-stk.txt'  # Replace with your text file's name

ts = []
with open(filename, 'r') as file:
    lines = file.readlines()
    header = lines[0].strip().split('\t')  # Get the header line and split it into fields
    print ('header', header)
    ts.append(header)



    print(ts)

    
    #header.append('Timestamp')  # Add a new field for the timestamp
    #updated_lines = [','.join(header)]  # Start the updated lines list with the modified header


    timecode = []

    for line in lines[1:]:
       
        values = line.strip().split('\t')
        time_string = values[0]
        timestamp = datetime.strptime(time_string, '%Y/%m/%d %H:%M:%S.%f').timestamp()
        timecode.append(str(int(timestamp)))  # Append the timestamp as a string
        res.append((str(int(timestamp)), (float(values[1]) - 2.0535)*-10e6) )
        

t = []
dop = []





for elem in res:
    t.append(int(elem[0]) +50)
    dop.append(elem[1]*100)

print ('t0', t[0] + 138)
print('g0', g1[0])
#plt.plot(ts, f)
plt.plot(g1,f, 'r', t ,dop ,'b')
plt.xticks(g1, range(0,529))

#plt.plot(t, dop, marker='.', linestyle='-', color='blue', label='Measured frequency shift')

# Set labels and title
plt.xlabel('time[s]')
plt.ylabel('Freq_Offset [Hz]')
plt.title('Doppler Offset')
plt.grid()
plt.locator_params(axis = 'x', nbins = 4)
plt.legend()
# Display the plot
plt.show()

