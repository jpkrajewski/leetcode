# Every valid email consists of a local name and a domain name, separated by the '@' sign. Besides lowercase letters, the email may contain one or more '.' or '+'.

# For example, in "alice@leetcode.com", "alice" is the local name, and "leetcode.com" is the domain name.
# If you add periods '.' between some characters in the local name part of an email address, mail sent there will be forwarded to the same address without dots in the local name. Note that this rule does not apply to domain names.

# For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.
# If you add a plus '+' in the local name, everything after the first plus sign will be ignored. This allows certain emails to be filtered. Note that this rule does not apply to domain names.

# For example, "m.y+name@email.com" will be forwarded to "my@email.com".
# It is possible to use both of these rules at the same time.

# Given an array of strings emails where we send one email to each emails[i], return the number of different addresses that actually receive mails.

 

# Example 1:

# Input: emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
# Output: 2
# Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails.
# Example 2:

# Input: emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
# Output: 3
 

# Constraints:

# 1 <= emails.length <= 100
# 1 <= emails[i].length <= 100
# emails[i] consist of lowercase English letters, '+', '.' and '@'.
# Each emails[i] contains exactly one '@' character.
# All local and domain names are non-empty.
# Local names do not start with a '+' character.
# Domain names end with the ".com" suffix.
# Domain names must contain at least one character before ".com" suffix.

from typing import List



class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        emails_set = set()
        for email in emails:
            local, domain = email.split("@")
            local = local.replace(".", "")
            if "+" in local:
                local, _ = local.split("+", maxsplit=1)
            emails_set.add(local + "@" + domain)
        return len(emails_set)


emails = ["fg.r.u.uzj+o.pw@kziczvh.com","r.cyo.g+d.h+b.ja@tgsg.z.com","fg.r.u.uzj+o.f.d@kziczvh.com","r.cyo.g+ng.r.iq@tgsg.z.com","fg.r.u.uzj+lp.k@kziczvh.com","r.cyo.g+n.h.e+n.g@tgsg.z.com","fg.r.u.uzj+k+p.j@kziczvh.com","fg.r.u.uzj+w.y+b@kziczvh.com","r.cyo.g+x+d.c+f.t@tgsg.z.com","r.cyo.g+x+t.y.l.i@tgsg.z.com","r.cyo.g+brxxi@tgsg.z.com","r.cyo.g+z+dr.k.u@tgsg.z.com","r.cyo.g+d+l.c.n+g@tgsg.z.com","fg.r.u.uzj+vq.o@kziczvh.com","fg.r.u.uzj+uzq@kziczvh.com","fg.r.u.uzj+mvz@kziczvh.com","fg.r.u.uzj+taj@kziczvh.com","fg.r.u.uzj+fek@kziczvh.com"]
Solution().numUniqueEmails(emails)