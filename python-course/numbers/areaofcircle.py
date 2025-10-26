pie = 3.14
radius = input('Enter a radius number = ')
if(radius.replace('.', '', 1).isdigit()):
    area = pie * radius ** 2
    print (area)
else: 
    print('please enter a number')


'''
🧩 1. Why .isnumeric() and .isdecimal() fail on floats

Both .isnumeric() and .isdecimal() are string methods.
They don’t actually “understand” math — they just check whether every single character in the string is a numeric digit.

Example:

"123".isnumeric()    # True
"٥".isnumeric()      # True (Arabic-Indic digit!)
"Ⅷ".isnumeric()      # True (Roman numeral 8!)
"3.14".isnumeric()   # False (because of the '.')


So "3.14" fails because of the . — it’s not a digit.
Same story with .isdecimal(). It’s even stricter — it only returns True for standard digits 0–9 (not Unicode numerals, not fractions, and definitely not decimals).

So neither method was ever meant for “number detection” — they were meant for text validation, like when checking if a string only contains digit characters.

⚙️ 2. Why .isdigit() works better for integers

.isdigit() is basically the same as .isdecimal() but a tiny bit looser — it accepts some Unicode digits beyond 0–9.
Still, it fails the same way on floats:

"123".isdigit()    # True
"3.14".isdigit()   # False


because that pesky . is not a digit.

That’s why we do this little trick:

radius.replace('.', '', 1).isdigit()


Here’s what happens:

"3.14".replace('.', '', 1) → "314"

"314".isdigit() → ✅ True

"3.1.4".replace('.', '', 1) → "31.4" → .isdigit() → ❌ False
(because now it still has one . left)

So it’s a quick-and-dirty way to allow one decimal point while still rejecting invalid stuff.
'''