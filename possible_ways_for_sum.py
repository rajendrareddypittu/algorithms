def possibleways_for_sum(ind,options,sum,new_sum,way,oldel):
	if ind>len(options):
		print("ind>op and ind=",ind)
		return
	if new_sum>sum:
		print("NA")
		return
	if new_sum==sum:
		print("way :",list(way))
		return
	if new_sum<sum:
		print("rem_sum<sum")
		#options.remove(oldel)
		for i in range(ind,len(options)):
					print("i",i)
					ele=options[i]
			
					newop=options.copy()
					#newop.remove(ele)
					#print(i,sum,new_sum+int(ele),list(way+str(ele)),ele)
					possibleways_for_sum(i+1,newop[:],sum,new_sum+int(ele),way+str(ele),ele)
		
	return	
		
options=[1,2,3]
sum=4
ele=''
way=''
possibleways_for_sum(0,options[:],sum,0,way,ele)
print(way)
