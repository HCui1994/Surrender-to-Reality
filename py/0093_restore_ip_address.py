class Solution:
    def restoreIpAddresses(self, s):
        all_possible_ip = []
        self.restorer(string=s, segment=0, ip="", all_posible_ip=all_possible_ip)
        return list(all_possible_ip)
        
    def restorer(self, string, segment, ip, all_posible_ip):

        # pay attention to lexicographical order, which is default in python
        # but here neet to use 
        def compare(string1, string2):
            if len(string1) < len(string2):
                return True
            elif len(string1) == len(string2):
                return string1 <= string2
            else:
                return False

        if segment == 3 and compare(string, "255") and compare("0", string):
            if len(string) == 1:
                all_posible_ip.append(ip+string)
            elif string[:1] != "0":
                all_posible_ip.append(ip+string)
            return      # Attention! need to return to end this branch
        if segment < 3:
            # Attention! To not use if-elif-else, since all 3 branches need to be created here
            if compare(string[:1], "255") and compare("0", string[:1]):
                self.restorer(string=string[1:], segment=segment+1, ip=ip+string[:1]+".", all_posible_ip=all_posible_ip)
            if compare(string[:2], "255") and string[:1] != "0" and string[:2] != "00" and compare("0", string[:2]):
                self.restorer(string=string[2:], segment=segment+1, ip=ip+string[:2]+".", all_posible_ip=all_posible_ip)
            if compare(string[:3], "255") and string[:1] != "0" and string[:2] != "00" and string[:3] != "000" and compare("0", string[:3]):
                self.restorer(string=string[3:], segment=segment+1, ip=ip+string[:3]+".", all_posible_ip=all_posible_ip)
            
            # edge case: a non-zero segment cannot start with '0'!
    

solution = Solution()
s = "010010"
print(solution.restoreIpAddresses(s=s))