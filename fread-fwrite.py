# The code of the email_gen function was originally provided in the task
def email_gen(list_of_names):
    emails = []
    for i in list_of_names:
        letter = 1
        while i[1] + '.' + i[0][0:letter] + '@company.io' in emails:
            letter+=1
        emails.append(i[1] + '.' + i[0][0:letter] + '@company.io')
    return emails

# Below is my task implementation code
f = open('task_file.txt', 'r')
list_of_names = []
lines = []
for line in f:
    tmp_list = []
    split_line = line.split(', ')
    lines.append(split_line)
    if split_line[1] != '' and split_line[2] != '' and len(split_line[3]) == 7 and split_line[4] != '':
        tmp_list.append(split_line[1])
        tmp_list.append(split_line[2])
        list_of_names.append(tmp_list)
emails = email_gen(list_of_names)
f.close()
f = open('task_file.txt', 'w')
i = 0

for line in lines:
    if line[0] == 'EMAIL':
        line = ", ".join(line)
        f.write(line)
        continue
    if line[1] != '' and line[2] != '' and len(line[3]) == 7 and line[4] != '':
        line = ", ".join(line)
        line = emails[i] + line
    else:
        line = ", ".join(line)
        f.write(line)
        continue
    f.write(line)
    i += 1
f.close()
