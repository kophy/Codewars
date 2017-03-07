def hamming(n):
  data = [1] * n;
  ctr2, ctr3, ctr5 = 0, 0, 0;
  for i in range(1, n):
      data[i] = min(data[ctr2] * 2, data[ctr3] * 3, data[ctr5] * 5);
      if data[i] == data[ctr2] * 2:
          ctr2 += 1;
      if data[i] == data[ctr3] * 3:
          ctr3 += 1;
      if data[i] == data[ctr5] * 5:
          ctr5 += 1;
  return data[-1];