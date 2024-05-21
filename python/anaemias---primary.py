# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"57114.0","system":"readv2"},{"code":"69269.0","system":"readv2"},{"code":"5823.0","system":"readv2"},{"code":"69379.0","system":"readv2"},{"code":"57859.0","system":"readv2"},{"code":"68087.0","system":"readv2"},{"code":"938.0","system":"readv2"},{"code":"69027.0","system":"readv2"},{"code":"37320.0","system":"readv2"},{"code":"30994.0","system":"readv2"},{"code":"31774.0","system":"readv2"},{"code":"15658.0","system":"readv2"},{"code":"107828.0","system":"readv2"},{"code":"34754.0","system":"readv2"},{"code":"70128.0","system":"readv2"},{"code":"72104.0","system":"readv2"},{"code":"61326.0","system":"readv2"},{"code":"21723.0","system":"readv2"},{"code":"15422.0","system":"readv2"},{"code":"34953.0","system":"readv2"},{"code":"44913.0","system":"readv2"},{"code":"69061.0","system":"readv2"},{"code":"64625.0","system":"readv2"},{"code":"65502.0","system":"readv2"},{"code":"7225.0","system":"readv2"},{"code":"32715.0","system":"readv2"},{"code":"47438.0","system":"readv2"},{"code":"47620.0","system":"readv2"},{"code":"43166.0","system":"readv2"},{"code":"16108.0","system":"readv2"},{"code":"43825.0","system":"readv2"},{"code":"109273.0","system":"readv2"},{"code":"71965.0","system":"readv2"},{"code":"61462.0","system":"readv2"},{"code":"31275.0","system":"readv2"},{"code":"65351.0","system":"readv2"},{"code":"41142.0","system":"readv2"},{"code":"40244.0","system":"readv2"},{"code":"66239.0","system":"readv2"},{"code":"72252.0","system":"readv2"},{"code":"31491.0","system":"readv2"},{"code":"102848.0","system":"readv2"},{"code":"32900.0","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('aplastic-anaemias-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["anaemias---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["anaemias---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["anaemias---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
