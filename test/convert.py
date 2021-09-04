import csv

file_object = open('test.sql', 'a')
with open('test.csv','r') as csv_file:
    csv_reader = list(csv.reader(csv_file, delimiter=','))
    line_count = 0
    # print(csv_reader[0][0])
    for row in csv_reader:
        # Append 'hello' at the end of file
        if line_count == 0:
            create_table = f'CREATE TABLE `test` (`id` int(255) NOT NULL AUTO_INCREMENT,'
            for column in row:
                create_table += f'`{column}` varchar(1000) COLLATE utf8_unicode_ci  DEFAULT NULL ,'
            create_table += f' PRIMARY KEY (`id`) ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1; \n \n \n \n'
            file_object.write(create_table)
            line_count += 1
        else:
            no_of_column = len(csv_reader[0])
            create_column = f'INSERT INTO `test` ('
            for i in range(no_of_column):
                if(i == no_of_column - 1):
                    create_column += f'`{csv_reader[0][i]}`'
                    continue
                create_column += f'`{csv_reader[0][i]}`,'

            create_column += ') values ('
            
            i = 0
            for column in row:
                
                if(i == no_of_column - 1):
                    create_column += f'"{column}"'
                    i = i + 1
                    continue
                create_column += f'"{column}",'
                i = i + 1
            create_column += '); \n'
            file_object.write(create_column)
            line_count += 1
        
    print(f'Processed {line_count} lines.')
    file_object.close()
