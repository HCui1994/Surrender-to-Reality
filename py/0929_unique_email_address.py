"""
Every email consists of a local name and a domain name, separated by the @ sign.
For example, in alice@leetcode.com, alice is the local name, and leetcode.com is the domain name.
Besides lowercase letters, these emails may contain '.'s or '+'s.

If you add periods ('.') between some characters in the local name part of an email address, 
    mail sent there will be forwarded to the same address without dots in the local name.  
For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.  
(Note that this rule does not apply for domain names.)

If you add a plus ('+') in the local name, everything after the first plus sign will be ignored. 
This allows certain emails to be filtered, for example m.y+name@email.com will be forwarded to my@email.com.  
(Again, this rule does not apply for domain names.)

It is possible to use both of these rules at the same time.
Given a list of emails, we send one email to each address in the list.  How many different addresses actually receive mails? 

Example 1:
Input: ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
Output: 2
Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails
 
Note:

1 <= emails[i].length <= 100
1 <= emails.length <= 100
Each emails[i] contains exactly one '@' character.
"""


class Solution(object):
    def num_unique_emails_trie(self, emails):
        """
        尝试使用 trie 数据结构
        very slow
        """
        trie = {}
        count = 0
        for email in emails:
            curr = trie
            final = ""
            i = 0
            is_local = True
            while i < len(email):
                if is_local:
                    if email[i] == '.':
                        i += 1
                    elif email[i] == '+':
                        while email[i] != '@':
                            i += 1
                        final += email[i]
                        is_local = False
                        i += 1
                    else:
                        curr = curr.setdefault(email[i], {})
                        final += email[i]
                        i += 1
                else:
                    curr = curr.setdefault(email[i], {})
                    final += email[i]
                    i += 1
            if not curr.get("email"):
                count += 1
                curr["email"] = final
        print(trie)
        print(count)
        return count

    def num_unique_emails_string(self, emails):
        """
        python 库函数比自己写循环要快得多
        """
        unique_emails = set()
        for email in emails:
            unique_email = ""
            idx = 0
            while True:
                if email[idx] == '+':
                    while email[idx] != '@':
                        idx += 1
                    unique_emails.add(unique_email + email[idx:])
                    break
                elif email[idx] == '.':
                    idx += 1
                elif email[idx] == '@':
                    unique_emails.add(unique_email + email[idx:])
                else:
                    unique_email += email[idx]
                    idx += 1
        print(unique_emails)



    def test(self):
        emails = ["test.email+alex@leetcode.com",
                  "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]
        self.num_unique_emails_string(emails)


Solution().test()
