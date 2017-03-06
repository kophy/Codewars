def lcs(x, y, memo = {}):
  key = x + "@" + y;
  if key in memo:
      return memo[key];
  
  if len(x) > len(y):
      return lcs(y, x);
  if x == y[:len(x)]:
      return x;
  
  result = "";
  if x[0] == y[0]:
      result = x[0] + lcs(x[1:], y[1:]);
  else:
      l1, l2 = lcs(x, y[1:]), lcs(x[1:], y);
      result = l1 if len(l1) > len(l2) else l2;
  memo[key] = result;
  return result;