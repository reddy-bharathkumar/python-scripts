import time

sample="In no impression assistance contrasted. Manners she wishing justice hastily new anxious."

# At discovery discourse departure objection we. Few extensive add delighted tolerably sincerity her. Law ought him least enjoy decay one quick court. Expect warmly its tended garden him esteem had remove off. Effects dearest staying now sixteen nor improve.

initial_time=time.time()  
test=input()
after_time=time.time()

sample_split=sample.split()
test_compare=test.split()
boolean=True

while boolean:
  if len(test_compare)<len(sample_split):
    print("Please enter all the words with proper format.")
    exit()
  else:
    boolean=False

count=0
mistakes=[]

for i in range(len(sample_split)):
  if test_compare[i]==sample_split[i]:
    pass
  else:
    count=count+1
    mistakes.append(test_compare[i])

print("Total misspells: "+str(count))
print(mistakes)

time_taken=(after_time-initial_time)/60

words=len(test)/5
wpm=round(words/time_taken)
accuracy=round((len(sample_split)-count)/len(sample_split),2)*100

print("Your wpm: "+str(wpm))
print("Accuracy: "+str(accuracy)+"%")
