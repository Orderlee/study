def get_name(s_no, s_name, find_no):
    n = len(s_no)
    for i in range(0,n):
        if find_no == s_no[i]:
            return s_name[i]
    return "?"

sample_no = [39, 14, 67, 105]
sample_name = ["Justin", "John", "Mike", "Summer"]
print(get_name(sample_no, sample_name, 105))
print(get_name(sample_no, sample_name, 777))
