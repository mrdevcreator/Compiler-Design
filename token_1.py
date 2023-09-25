keywords = ["int", "float", "if", "else"]
math_op = ["*", "-", "+", "/", "="]
log_op = [">", "<", ">=", "<="]
other = [",", "(", ")", "{", "}", ";"]
k = []
m_op = []
l_op = []
n_values = []
identifiers = []
others = []

f = open("Input.txt", "r",encoding="utf-8-sig")
for lines in f.readlines():
    line = lines.strip().replace(',', ' ,').replace(';', ' ;').split(" ")
    #print(line)
    for each in line:
        if each in keywords and each not in k:
            k.append(each)
        elif each in math_op and each not in m_op:
            m_op.append(each)
        elif each in log_op and each not in l_op:
            l_op.append(each)
        elif each in other and each not in others:
            others.append(each)
        elif each.isdigit() or (each.replace(".", "").isdigit() and each.count(".") == 1):
            if each not in n_values:
                n_values.append(each)
        elif each.isalpha() and each not in identifiers:
            identifiers.append(each)

f.close()

print("Keywords:", ", ".join(k))
print("Identifiers:", ", ".join(identifiers))
print("Math Operators:", ", ".join(m_op))
print("Logical Operators:", ", ".join(l_op))
print("Numerical Values:", ", ".join(n_values))
print("Others:", ", ".join(others))