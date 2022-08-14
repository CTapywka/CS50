usr_input = input()
extensions = {".gif" : "image/gif", ".jpg" : "image/jpeg", ".jpeg" : "image/jpeg",
".png" : "image/png", ".pdf" : "application/pdf", ".txt" : "text/plain", ".zip" : "application/zip"
}
Flag = 0
for k in extensions:
    if k in usr_input:
        print(extensions[k])
        Flag +=1
if Flag == 0:
    print('application/octet-stream')
