class Solution:
    def romanToInt(self, s: str) -> int:
        roman_numerals = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        # prev_value = 'ZZ'
        # sum = 0
        # for x in range(len(s) - 1, -1, -1):
        #     val = roman_numerals[s[x]]
        #     if prev_value == 'ZZ':
        #         pass
        #     else:
        #         if (((prev_value == 'V' or prev_value == 'X') and s[x] == 'I')
        #              or ((prev_value == 'L' or prev_value == 'C') and s[x] == 'X') or ((prev_value == 'D' or prev_value == 'M') and s[x] == 'C')):
        #             val = val * -1
        #         else:
        #             val = val
        #     sum = sum + val
        #     print(sum)

        #     prev_value = s[x]
        # return sum

        total = 0
        for i in range(len(s)):
            current_val = roman_numerals[s[i]]
            if i + 1 < len(s) and current_val < roman_numerals[s[i + 1]]:
                total -= current_val
            else:
                total += current_val
        return total
           
            
        