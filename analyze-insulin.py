# creating preproinsulin-seq-clean with set string conditions
with open("preproinsulin-seq.txt", 'r') as input:
        with open("preproinsulin-seq-clean.txt", 'w') as output:
            for line in input:
                clean = line.replace("ORIGIN", '').replace('\r', '').replace(" ", '').replace('/', '').replace('\n', '');
                clean = ''.join(i for i in clean if not i.isdigit());
                output.write(clean);

# checking preproinsulin-seq-clean size
with open("preproinsulin-seq-clean.txt", 'r') as f:
    data = f.read();
size_of_file = len(data);
print(size_of_file);

#open isinsulin
with open("preproinsulin-seq-clean.txt", 'r') as input:
        with open("isinsulin-seq-clean.txt", 'w') as output:
           for line in input:
            output.write(line[0:24]);
#open binsulin
with open("preproinsulin-seq-clean.txt", 'r') as input:
        with open("binsulin-seq-clean.txt", 'w') as output:
            for line in input:
                output.write(line[24:54]);
#open cinsulin
with open("preproinsulin-seq-clean.txt", 'r') as input:
        with open("cinsulin-seq-clean.txt", 'w') as output:
            for line in input:
                output.write(line[54:89]);
#open ainsulin
with open("preproinsulin-seq-clean.txt", 'r') as input:
        with open("ainsulin-seq-clean.txt", 'w') as output:
            for line in input:
                output.write(line[89:110]);

#checking file char size
with open("isinsulin-seq-clean.txt", 'r') as f:
    data = f.read();
size_of_file = len(data);
print(size_of_file);
with open("binsulin-seq-clean.txt", 'r') as f:
    data = f.read();
size_of_file = len(data);
print(size_of_file);
with open("cinsulin-seq-clean.txt", 'r') as f:
    data = f.read();
size_of_file = len(data);
print(size_of_file);
with open("ainsulin-seq-clean.txt", 'r') as f:
    data = f.read();
size_of_file = len(data);
print(size_of_file);