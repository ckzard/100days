from calcylator import calc_app

def format_name(f_name, l_name):
    first = f_name.title()
    last = l_name.title()

    return first + " "  + last

print(format_name('chris', 'burns'))