d, h, m = [int (i) for i in input().split()]
  
start_time = (11 * 24 * 60) + (11 * 60) + 11
end_time = (d * 24 * 60) + (h * 60) + m 

if end_time < start_time:
  print (-1)
else:
  print (end_time - start_time)
