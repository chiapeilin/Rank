data,lis=[],[]

#Each line of data after reading \n is removed and stored in the data string.
with open("olympics.csv","r") as f:
	for line in f:
		data.append(line.strip())
#(Hive string) divides each row in Data into splits and adds them to the lis string.
	for l in range(2,len(data)-1):
		lis.append(data[l].split(","))


#Throw the things we want into the dictionary
country1={}
for i in lis:
	country1[i[0]]=[int(i[2]),int(i[7]),int(i[12]),int(i[2])-int(i[7])]
	if (int(i[2])-int(i[7]))>=0:
		country1[i[0]][3]=int(i[2])-int(i[7])
	else:
		country1[i[0]][3]=-(int(i[2])-int(i[7]))

#Create a dictionary and judge that the number of gold medals in summer and winter both are not 0
di={}
for i in lis:	
	if country1[i[0]][0]!=0 and country1[i[0]][1]!=0:
		di[i[0]]=country1[i[0]]
	

#1	
#Find the country that won the most gold medals in summer games
def answer21(d,k): #Ranking
	topk=[]
	for i in range(k):
		gold_max = 0
		gold_country = ""
		for c in d:
			if c in topk:
				continue
			gold = d[c][0]
			#Replace if the current value is greater than the original maximum
			if gold > gold_max: 
				gold_max = gold
				gold_country = c
		topk.append(gold_country)
	return topk
print(answer21(country1,1))


#2
#Find the country with the biggest difference between their summer and winter gold medal counts
def answer22(d,k):
	top_k2=[]
	for i in range(k):
		gold_swt1 = 0
		gold_country_2 = ""
		for c in d:
			if c in top_k2:
				continue
			gold_2 = d[c][3]
			#Replace if the current value is greater than the original maximum
			if gold_2>=0:	
				if gold_2 > gold_swt1:
					gold_swt1 = gold_2
					gold_country_2 = c
			else:
				if gold_2 < gold_swt1:
					gold_swt1 = gold_2
					gold_country_2 = c

		top_k2.append(gold_country_2)
	return top_k2
print(answer22(country1,1))

		
#3
#Find the country with the biggest difference between their summer and winter gold medal counts relative to their total gold medal count
def answer23(d,k):
	top_k=[]
	for i in range(k):
		gold_swt = 0
		gold_country_1 = ""
		for c in d:
			if c in top_k:
				continue
			gold_1 = d[c][3]
			total=d[c][2]	
			#Replace if the current value is greater than the original maximum
			if gold_1/total>gold_swt: 
				gold_swt=gold_1/total 
				gold_country_1=c
		top_k.append(gold_country_1)
	return top_k
print(answer23(di,1))

