from datetime import datetime
import matplotlib.pyplot as plt
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
        res.append((str(int(timestamp)), (float(values[1]) - 2.0535)*10e6))
        

t = []
dop = []

for elem in res:
    t.append(elem[0])
    dop.append(elem[1])

plt.plot(t, dop, marker='.', linestyle='-', color='blue', label='Measured frequency shift')

# Set labels and title
plt.xlabel('POSIX time[s]')
plt.ylabel('Freq_Offset [Hz]')
plt.title('Doppler Offset')
plt.grid()

plt.legend()
# Display the plot
plt.show()
