import hashlib   

def md5(origin):
	md5_parser = hashlib.md5()   
	md5_parser.update(origin)   
	return md5_parser.hexdigest()
