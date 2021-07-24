def possibleways_for_sum(options,sum,new_sum,way,oldel):
	if new_sum>sum:
		print("NA")
		return
	if new_sum==sum:
		print("way :",list(way))
		return
	if new_sum<sum:
		#print("rem_sum<sum")
		#options.remove(oldel)
		for ele in options:
					newop=options.copy()
					newop.remove(ele)
					possibleways_for_sum(newop[:],sum,new_sum+int(ele),way+str(ele),ele)
		return
		
options=[1,2,3]
sum=5
ele=''
way=''
possibleways_for_sum(options[:],sum,0,way,ele)
print(way)
