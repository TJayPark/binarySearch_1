N, M = map(int, input().split())
array = list(map(int,input().split()))
#DDuckList.sort()

maxD = max(array)

def binary_search(array,target,start,end):
  if(start > end):
    return None

  H = (start+end) // 2
  sum = 0
  for DDuck in array:
    if DDuck > H:
      sum+=(DDuck-H)
      
  if(sum==target):
    return H
  elif sum < target:
    return binary_search(array, target, start, H-1)
  else:
    return binary_search(array, target, H+1, end)

result = binary_search(array, M, 0, maxD)
print(result)