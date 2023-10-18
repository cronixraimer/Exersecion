regex_pattern = r"^(?!$)M{,3}(C[DM]|D?C{,3})(X[LC]|L?X{,3})(I[VX]|V?I{,3})$"
import re
print(str(bool(re.match(regex_pattern, input()))))
