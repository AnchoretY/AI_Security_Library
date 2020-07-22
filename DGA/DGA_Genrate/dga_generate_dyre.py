from datetime import datetime, timedelta 
from hashlib import sha256

def create_domain(date_str, seq_nr): 
  for i in range(seq_nr):
    tlds = ['.cc', '.ws', '.to', '.in', '.hk', '.cn', '.tk', '.so'] 
    hash = sha256('{0}{1}'.form at(date_str, i)).hexdigest()[3:36] 
    replace_char = chr(0xFF & ((i % 26) + 97))
    
    domain = '{0}{1}{2}'.form at(replace_char, hash, tlds[i % len(tlds)])
    yield domain
    
class dga_generate_dyre(BaseUDTF): 
  @annotate("bigint,string->string")
  def process(self, generate_count, date_d):
    # seq_nr: how many dga u need to generate
    if generate_count and date_d:
        date_d = datetime.strptime(date_d, "%Y-%m -%d")
    for domain in create_domain(date_d, generate_count):
        self.forward(str(domain), 'dyre')
