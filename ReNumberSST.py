import re


start = 0
def renum(matched):
    global start
    value=int(matched.group('id'))
    newid=str(start).zfill(10)
    start += 1
    return str("id="+'"'+newid+'"')


s='''   <si id="0000000002">
    <text>Wenn man den Dreh ein bisschen raus hat, reizen einen immer schwierigere Objekte.</text>
  <si id="0000000009">'''

print(re.sub(r"id=\"(?P<id>\d+)\"",renum,s,count=0,flags=re.M))
