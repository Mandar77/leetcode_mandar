class Solution(object):
    def maskPII(self, s):
        """
        :type s: str
        :rtype: str
        """
        if '@' in s:
            name, domain = s.split('@')
            return name[0].lower()+ "*****" + name[-1].lower() + "@" + domain.lower()

        else:
            digits = ''.join(filter(str.isdigit,s))
            local = "***-***-" + digits[-4:]
            if len(digits) == 10:
                return local
            elif len(digits) == 11:
                return "+*-" + local
            elif len(digits) == 12:
                return "+**-" + local
            else:
                return "+***-" + local