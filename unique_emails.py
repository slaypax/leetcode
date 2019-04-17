# https://leetcode.com/problems/unique-email-addresses/
# Every email consists of a local name and a domain name, separated by the 
# @ sign. For example, in alice@leetcode.com, alice is the local name, 
# and leetcode.com is the domain name.
# Besides lowercase letters, these emails may contain '.'s or '+'s.
# If you add periods ('.') between some characters in the local name
#  part of an email address, mail sent there will be forwarded to the same address
#  without dots in the local name.  For example, "alice.z@leetcode.com" and
# "alicez@leetcode.com" forward to the same email address.
# (Note that this rule does not apply for domain names.)
# If you add a plus ('+') in the local name, everything after the first plus
#  sign will be ignored. This allows certain emails to be filtered, for example
#  m.y+name@email.com will be forwarded to my@email.com. 
# (Again, this rule does not apply for domain names.)
# It is possible to use both of these rules at the same time.
# Given a list of emails, we send one email to each address in the list.
# How many different addresses actually receive mails? 

# Input: ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
# Output: 2
# Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails

# Your runtime beats 48.83 % of python3 submissions.
# Runtime: 52 ms

import re

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        email_list = []
        regex = '([a-zA-Z+.]*)(@)([a-zA-Z.]*).(com)'
        for email in emails:
            m = re.search(regex, email )
            clean_email = m[1]
            if '.' in clean_email:
                clean_email = m[1].replace(".", "")
            if '+' in clean_email:
                plus_sign_loc = clean_email.index('+')
                clean_email = clean_email[:plus_sign_loc]
            email_list.append(clean_email + m[2] + m[3] + m[4])
        email_list = list(dict.fromkeys(email_list))
        return(len(email_list))