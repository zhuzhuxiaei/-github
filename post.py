import requests
import re
def post():
	try:	
		information=open("information.txt","rt")
	except:
		return 0;	
	login=information.readline()
	login=login.split("\n")[0]
	password=information.readline()
	password=password.split("\n")[0]
	repositories=information.readline()
	repositories=repositories.split("\n")[0]
	way=input("文本在本机的路径与名称")
	filename=way.split('/')[-1]
	try:	
		localfile=open(way,'rt')
	except:
		print("文件打开失败")
		return 0;	
	value=''	
	for line in localfile:
		value+=line
	localfile.close()
	url1="https://github.com/session"
	url2="https://github.com/"+str(login)+"/"+str(repositories)
	url3=url2+"/new/master"
	data_denglu={
        "commit":"Sign+in",
        "utf8":"✓",
        "authenticity_token":"BQ775aXgK0ZlS6BKPrMuIOiVbDezQj7DQpzpA6MzwmQIxPL4wk1VvO8tXAJuCFMNk/zvI4ysMvVOxOPWZ+Jnmg==",
        "login":login,
        "password":password}
	cookies_denglu={
        "_ga":"GA1.2.753903281.1505531409",
        "_gh_sess":"eyJzZXNzaW9uX2lkIjoiZjY4MTBiZDY4YzkwYTA0YWQ0YTM3MmJlNjdlZjU0ZDEiLCJsYXN0X3JlYWRfZnJvbV9yZXBsaWNhcyI6MTUwOTAwMjQ2NTY1MSwiY29udGV4dCI6Ii8iLCJzcHlfcmVwbyI6InpodXpodXhpYWVpLy0iLCJzcHlfcmVwb19hdCI6MTUwOTAwMjMyNSwibGFzdF93cml0ZSI6MTUwOTAwMjM0NjYxOSwicmVmZXJyYWxfY29kZSI6Imh0dHBzOi8vZ2l0aHViLmNvbS8iLCJfY3NyZl90b2tlbiI6ImNiL0FoaEN2cmlVVXVSNURSendlcHFZUlNqL0prNXNwdS9JUSs4RXlESzQ9IiwiZmxhc2giOnsiZGlzY2FyZCI6W10sImZsYXNoZXMiOnsiYW5hbHl0aWNzX2xvY2F0aW9uX3F1ZXJ5X3N0cmlwIjoidHJ1ZSJ9fX0=--5ae52916dd2bdd5ea254116d0cc8793b05366b3b",
        "_octo":"GH1.1.368302907.1505531424",
        "logged_in":"no",
        "tz":"Asia/Shanghai"
        }
    
   
	s=requests.Session()
	
	r1=s.post(url=url1,data=data_denglu,cookies=cookies_denglu)
	
	r2=s.get(url=url2)
	
	authenticity_tokeN=re.findall(r'authenticity_token\" type=\"hidden\" value=\".*?\" /></div>',r2.text)
	authenticity_toke=authenticity_tokeN[9]
	authenticity_token=authenticity_toke[41:129]

	data_tijiaoyemian={
	"utf8":"✓",
	"authenticity_token":authenticity_token}
	r3=s.post(url=url3,data=data_tijiaoyemian)
	print(r3.status_code)
	authenticity_tokeN2=re.findall(r'authenticity_token\" type=\"hidden\" value=\".*?\" /></div>',r3.text)
	authenticity_toke2=authenticity_tokeN2[7]
	authenticity_token2=authenticity_toke2[41:129]
	commiT=re.findall(r'name=\"commit\" class=\"js-commit-oid\" value=\".*?\">',r3.text)
	commi=commiT[0]
	commit=commi[43:83]

	data_tijiao={
	"utf8":"✓",
	"authenticity_token":authenticity_token2,
	"filename":filename,
	"new_filename":filename,
    	"commit":commit,
	"same_repo":"1",
	"pr":"",
	"content_changed":"true",
	"value":value,
	"message":"",
	"placeholder_message":"Create+"+str(filename),
	"description":"",
	"commit-choice":"direct",
	"target_branch":"master",
	"quick_pull":""}
	r4=s.post(url="https://github.com/zhuzhuxiaei/-/create/master",data=data_tijiao)
		
	if(r4.status_code==200): 
		print("创建成功")
	return 0;
post()
