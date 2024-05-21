import requests
import base64
link= requests.get('https://panel1.nimplus.space/api/user/account/subscribe/58f6aa6913476d0839937d15a48b250f?type=android&ip=0&flow=1')
##########DECODE#############
decode=link.text
tr1 = decode.encode("ascii")
tr2 = base64.b64decode(tr1) 
decrypt = tr2.decode("ascii") 
############################
string = decrypt
new_string = string.replace("55317", "  ")
new_string2=new_string.replace("Tunnel3%20","SPEED5%E2%80%A2%E1%B4%9B%E1%B4%9C%C9%B4%C9%B4%E1%B4%87%CA%9F%E2%80%A2")
new_string3=new_string2.replace("Tunnel4(vless)","SPEED7%E2%80%A2%E1%B4%9B%E1%B4%9C%C9%B4%C9%B4%E1%B4%87%CA%9F%E2%80%A2")
new_string4=new_string3.replace("%D8%A2%D9%84%D9%85%D8%A7%D9%86%20(ws)%20","WS%E2%80%A2%C9%A2%E1%B4%87%CA%80%E2%80%A2")
new_string5=new_string4.replace("%D8%A8%D9%84%DA%98%DB%8C%DA%A9","WS%E2%80%A2%CA%99%E1%B4%87%CA%9F%E2%80%A2")
new_string6=new_string5.replace("%D8%AA%D8%B1%DA%A9%DB%8C%D9%87(http)%20","HTTP%E2%80%A2%E1%B4%9B%E1%B4%9C%CA%80%E2%80%A2")
new_string7=new_string6.replace("%D8%AC%D9%85%D9%87%D9%88%D8%B1%DB%8C%20%DA%86%DA%A9(ws)%20","WS%E2%80%A2%E1%B4%84%CA%9C%E1%B4%A2%E2%80%A2")
new_string8=new_string7.replace("%D9%86%D8%B1%D9%88%DA%98%20(ws)%20","WS%E2%80%A2%C9%B4%E1%B4%8F%CA%80%E2%80%A2")
new_string9=new_string8.replace("%D9%87%D9%84%D9%86%D8%AF(New%20Ws)%20","WS%E2%80%A2%C9%B4%E1%B4%87%E1%B4%85%E2%80%A2")
new_string10=new_string9.replace("Tunnel1(vless)%20","SPEED3%E2%80%A2%E1%B4%9B%E1%B4%9C%C9%B4%C9%B4%E1%B4%87%CA%9F%E2%80%A2")
new_string11=new_string10.replace("%D8%A7%D9%86%D9%82%D8%B6%D8%A7","")
new_string12=new_string11.replace("D8%AF%D8%B1%D8%B5%D8%AF%20%D8%A7%D8%B2%20%DA%A9%D9%84%20%D8%AD%D8%AC%D9%85"," ")
##########ENCODE#############
my_string = new_string12
encoded_string = base64.b64encode(my_string.encode("utf-8"))
#print(encoded_string.decode())
#############################
file = open("output.html", "w")

# Write HTML content

file.write(encoded_string.decode('ascii'))


# Close the file
file.close()



