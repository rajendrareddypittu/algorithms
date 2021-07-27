def avg_word_length(str):
	line_length=0
	if str==None:
		return
	if len(str.strip())<1 or str==None:
		print("invalid string")
		return
	else:
		words=str.strip().replace(","," ").replace("."," ").split(' ')
		count=len(words)
		for word in words:
			line_length=line_length+len(word)
		avg_word_len=	line_length/count
		print("avg", avg_word_len)
		return



avg_word_length("")
avg_word_length(None)
avg_word_length("hello,world.welco")
avg_word_length("hello world welco")				
			
			
