class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_text = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

        print(filtered_text)
        # if len(filtered_text) == 1:
        #     return False
        st = 0
        ed = len(filtered_text)-1
        print(len(filtered_text))
        # print(filtered_text[st])
        # if len(s)%2 == 0:
        while st<=ed:
            if filtered_text[st] != filtered_text[ed]:
                return False
            st +=1
            ed -=1
        return True