def possibleways_for_sum(options,sum,new_sum,way):
	if new_sum>sum:
		print("NA")
		return
	if new_sum==sum:
		print("way :",list(way))
		return
	if new_sum<sum:
		#print("rem_sum<sum")
		for ele in options:
					possibleways_for_sum(options,sum,new_sum+int(ele),way+str(ele))
		return
		
options=[1,2]
sum=4
possibleways_for_sum(options,sum,0,'')
