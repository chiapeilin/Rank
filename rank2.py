data,lis=[],[]

#Each line of data after reading \n is removed and stored in the data string.
with open("census.csv","r") as f:
	for line in f:
		data.append(line.strip())
#(Hive string) divides each row in Data into splits and adds them to the lis string.
	for l in range(2,len(data)-1):
		lis.append(data[l].split(","))

#1
#Find the state with the most counties in it
staname={} 
a=0
for i in range(len(lis)):	
	if lis[i-1][0]=="040":	#Return to zero after changing to another state
		a=0
	if lis[i][0]=="040":  #The state does not count
		a=a
	if lis[i][0]=="050":
		a+=1
	staname[lis[i][5]]=a	


def answer31(d,k):
	topk=[]
	for i in range(k):
		counties_max = 0
		state = ""
		for c in d:
			if c in topk:
				continue
			counties = d[c]
			#Replace if the current value is greater than the original maximum
			if counties > counties_max:  
				counties_max = counties
				state = c
		topk.append(state)
	return topk
print(answer31(staname,1))


#2
#Only looking at the three most populous counties for each state 
#Find the three most populous states
staname1={}
pop_c=[]
for i in range(len(lis)): 
	if lis[i][0]=="050":
		pop_c.append(int(lis[i][7]))
		pop_c.sort()

	if lis[i][0]=="040":
		pop_c=[]

	staname1[lis[i][5]]=pop_c

pop_max3=[]
for key in staname1:
	staname1[key]=sum(staname1[key][-3:])


def answer32(d,k):
	topk1=[]
	for i in range(k):
		state_max = 0
		state1 = ""
		for c in d:
			if c in topk1:
				continue
			pop = d[c]
			#Replace if the current value is greater than the original maximum
			if pop > state_max:  
				state_max = pop
				state1 = c
		topk1.append(state1)
	return topk1
print(answer32(staname1,3))


#3
#Find the county with the largest change in population within the five year period
gap={}
pop10_15=[]
for i in range(len(lis)):
	pop10_15.append([lis[i][9],lis[i][10],lis[i][11],lis[i][12],lis[i][13],lis[i][14]])
	ma=max(pop10_15[i])  #Find the year with the highest number of people in each county
	mi=min(pop10_15[i])	 #Find the year with the least number of people in each county
	gap[lis[i][6]]=int(ma)-int(mi)	#Use a dictionary to indicate the annual population gap in each county

def answer33(d,k):
	topk2=[]
	for i in range(k):
		gap_max = 0
		state2 = ""
		for c in d:
			if c in topk2:
				continue
			pop_gap = d[c]
			#Replace if the current value is greater than the original maximum
			if pop_gap>gap_max:  
				gap_max = pop_gap
				state2 = c
		topk2.append(state2)
	return topk2
print(answer33(gap,1))



