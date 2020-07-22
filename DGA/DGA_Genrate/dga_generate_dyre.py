# python3
# Author: Yhk
# Description: dyre dga domain gengerate function
# Tlds: ['.cc', '.ws', '.to', '.in', '.hk', '.cn', '.tk', '.so']
# Factors: time
# Example: ['a08b140bc9edfdf82326ed46a4c0208fb0.cc',
#             'bf742c5783133cd2bcedd6c47d21a46d4c.ws',
#             'c15c212f9520e83217514f3a71e50679a9.to',
#             'dfc2f2b7dd4720596646f8d034a631cf4a.in',]


import datetime
from hashlib import sha256

def create_domain(date_str, seq_nr): 
    for i in range(seq_nr):
        tlds = ['.cc', '.ws', '.to', '.in', '.hk', '.cn', '.tk', '.so'] 
        hash = sha256('{0}{1}'.format(date_str, i).encode("utf-8")).hexdigest()[3:36] 
        replace_char = chr(0xFF & ((i % 26) + 97))
        domain = '{0}{1}{2}'.format(replace_char, hash, tlds[i % len(tlds)])
        yield domain


def dga_generate_dyre(generate_count,date_id):
    dga_list = []
    if generate_count and date_id:
        date_id = datetime.datetime.strftime(date_id, "%Y-%m-%d")
    for domain in create_domain(date_id, generate_count):
            dga_list.append(domain)
    return dga_list

dga_generate_dyre(10,datetime.datetime.today())
