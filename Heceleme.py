def hecele(s):
    s3=[]
    l=0
    p=0
    for i in s:
        if s[l] == ' ':
            s3.append(' ')
            l+=1
            p=l
            continue
        else:
            if s[l] == 'a' or s[l] == 'e' or s[l] == 'i' or s[l] == 'o' or s[l] == 'u':
                if s[l] == s[-1]:
                    for j in range(p,l+1):
                        s3.append(s[j])
                else:
                    if s[l+1] == s[-1]:
                        for j in range(p,l+2):
                            s3.append(s[j])
                    else:
                        if s[l+1] == ' ':
                            for j in range(p,l+1):
                                s3.append(s[j])
                            p=l+2
                        elif s[l+1] == 'a' or s[l+1] == 'e' or s[l+1] == 'i' or s[l+1] == 'o' or s[l+1] == 'u':
                            for j in range(p,l+1):
                                s3.append(s[j])
                            s3.append('-')
                            p=l+1
                        else:
                            if s[l+2] == s[-1]:
                                if s[l+2] == 'a' or s[l+2] == 'e' or s[l+2] == 'i' or s[l+2] == 'o' or s[l+2] == 'u':
                                    for j in range(p,l+1):
                                        s3.append(s[j])
                                    s3.append('-')
                                    for j in range(l+1,l+3):
                                        s3.append(s[j])
                                else:
                                    for j in range(p,l+3):
                                        s3.append(s[j])
                            else:
                                if s[l+2] == ' ':
                                    for j in range(p,l+2):
                                        s3.append(s[j])
                                    p=l+3
                                elif s[l+2] == 'a' or s[l+2] == 'e' or s[l+2] == 'i' or s[l+2] == 'o' or s[l+2] == 'u':
                                    for j in range(p,l+1):
                                        s3.append(s[j])
                                    s3.append('-')
                                    p=l+1
                                else:
                                    if s[l+3] == ' ':
                                        for j in range(p,l+3):
                                            s3.append(s[j])
                                        p=l+4
                                    elif s[l+3] == 'a' or s[l+3] == 'e' or s[l+3] == 'i' or s[l+3] == 'o' or s[l+3] == 'u':
                                        for j in range(p,l+2):
                                            s3.append(s[j])
                                        s3.append('-')
                                        p=l+2
                                    else:
                                        for j in range(p,l+3):
                                            s3.append(s[j])
                                        s3.append('-')
                                        p=l+3
                        
        l+=1
    s2 = ''.join(s3)
    return s2

print(hecele("aort cokmu cok onemli mi kanka"))
