class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        def freq(word: str) -> dict:
            freq_dict = {}
            for char in word:
                if char in freq_dict:
                    freq_dict[char] += 1
                else:
                    freq_dict[char] = 1
            return freq_dict
        
        ans = freq(words[0])
        for index in range(1, len(words)):
            curr = freq(words[index])

            del_keys = []
            for k in ans.keys():
                if k in curr:
                    if curr[k] < ans[k]:
                        ans[k] = curr[k]
                else:
                    del_keys.append(k)
                    
            for dk in del_keys:
                del ans[dk]
                    
                
        ans_ = []
        for k, v in ans.items():
            for _ in range(v):
                ans_.append(k)

        return ans_