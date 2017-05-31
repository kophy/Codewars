import hashlib
import itertools

def sha256_cracker(hash, chars):
  for comb in itertools.permutations(list(chars), len(chars)):
      s = "".join(comb);
      if hashlib.sha256(s).hexdigest() == hash:
          return s;
  return None;