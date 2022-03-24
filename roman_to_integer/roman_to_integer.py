class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {     
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        
        romans_with_sub = {
            'V': 'I',
            'X': 'I',
            'L': 'X',
            'C': 'X',
            'D': 'C',
            'M': 'C'
        }
        
        result = 0
        skip_next = False
        
        # parse from end
        reversed_input = s[::-1]
        
        for index, roman in enumerate(reversed_input):
            
            if skip_next:
                skip_next = False
                continue
            
            if roman not in romans_with_sub.keys():
                result = result + mapping[roman]
            else:
                # look at next roman
                try:
                    if reversed_input[index+1] == romans_with_sub[roman]:
                        calculcated_number = mapping[roman] - mapping[reversed_input[index+1]]
                        result = result + calculcated_number
                        skip_next = True
                    else:
                        result = result + mapping[roman]
                except IndexError:
                    result = result + mapping[roman]
        
        return result
