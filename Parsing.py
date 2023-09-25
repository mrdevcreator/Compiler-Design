class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

stack = Stack()

terminal = ["id", "*", "+", "(", ")", "$"]
parse_rules = {
    "id": {"E": "TE'", "T": "FT'", "F": "id"},
    "+": {"E'": "+TE'", "T'": "epsilon","T": "synch", "F": "synch"},
    "*": {"T'": "*FT'", "F": "synch"},
    "(": {"E": "TE'", "T": "FT'", "F": "(E)"},
    ")": {"E'": "epsilon", "T'": "epsilon","E": "synch","T": "synch","F": "synch"},
    "$": {"E'": "epsilon", "T'": "epsilon","E": "synch","T": "synch","F": "synch"}
}

input_str = str(input("Enter your string")).lower()
#input_str = "id+id*id"
input_str += "$"
input_list = []

while input_str:
    for term in terminal:
        if input_str.startswith(term):
            input_list.append(term)
            input_str = input_str[len(term):]
            break


stack.push("$")
stack.push("E")
input_ptr = 0


matched_list = []
print(f"{' Matched':<20}{'Stack':<20}{'Input':<20}{'Action':<20}")
print("-------------------------------------------------------------------")
print(f"{'':<20}{''.join(reversed(stack.items)):<20}{''.join(input_list[input_ptr:]):<20}{'':<20}")

while True:
    x = stack.peek()
    a = input_list[input_ptr]

    if x in terminal or x == "$":
        if x == a:
            if x == "$":
                print()
                print("Parsing Successful")
                break
            stack.pop()
            matched_list.append(a)
            print(f"{''.join(matched_list):<20}{''.join(reversed(stack.items)):<20}{''.join(input_list[input_ptr+1:]):<20}{'match ' + a:<20}")
            input_ptr += 1
        else:
            stack.pop()
    else:
        if parse_rules[a][x] != "":
            rule = parse_rules[a][x]
            q = stack.pop()

            if rule in terminal:
                stack.push(rule)
                print(f"{''.join(matched_list):<20}{''.join(reversed(stack.items)):<20}{''.join(input_list[input_ptr:]):<20}{q + ' ==> ' + rule:<20}")
            elif rule == "epsilon":
                print(f"{''.join(matched_list):<20}{''.join(reversed(stack.items)):<20}{''.join(input_list[input_ptr:]):<20}{q + ' ==> ' + rule:<20}")
                pass
            elif rule == "synch":
                print(f"{''.join(matched_list):<20}{''.join(reversed(stack.items)):<20}{''.join(input_list[input_ptr:]):<20}{q + ' ==> ' + rule:<20}")
                pass
            else:
                i = len(rule) - 1
                while i >= 0:
                    if rule[i] == "'":
                        combined_symbol = rule[i - 1] + rule[i]
                        stack.push(combined_symbol)
                        i -= 2
                    else:
                        stack.push(rule[i])
                        i -= 1
                print(f"{''.join(matched_list):<20}{''.join(reversed(stack.items)):<20}{''.join(input_list[input_ptr:]):<20}{q + ' ==> ' + rule:<20}")
        else:
            input_ptr += 1 # If there is no rule or blanked then skipped the input symbol.
