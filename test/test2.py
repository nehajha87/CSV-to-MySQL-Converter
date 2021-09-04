import csv

file_object = open('test.sql', 'a')
with open('test.csv','r') as csv_file:
    csv_reader = list(csv.reader(csv_file, delimiter=','))
    line_count = 0
    # print(csv_reader[0][0])
    print(len(csv_reader[0]))
    for row in csv_reader:
        print(csv_reader[0][0])
        # Append 'hello' at the end of file
        # if line_count == 0:
        #     a = f'CREATE TABLE test ("id" int(255) NOT NULL AUTO_INCREMENT,'
        #     for column in row:
        #         a += f'{column} varchar(1000) COLLATE utf8_unicode_ci  DEFAULT NULL ,'
        #     a += f', PRIMARY KEY (`id`) ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1;'
        #     file_object.write(a)
        #     line_count += 1
        # Close the file
        
        # if line_count == 0:
        #     print(f'Column names are {", ".join(row)}')
        #     line_count += 1
        # else:
        #     print(f'\t{row[0]} works in the {row[1]} city')
        #     line_count += 1
    print(f'Processed {line_count} lines.')
    file_object.close()
