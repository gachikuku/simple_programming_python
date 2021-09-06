def piglatin(s: str, un: int) -> str:

    s = [s]
    text = s[0].split()

    if un == 0:
        
        ans = []
        
        for i in text:
        
            i_list = list(i)
            rmvd = i_list[0]
            i_list.remove(rmvd)
            i_list.append(rmvd)
            i_list.append("a")
            i_list.append("y")
            ans.append(i_list)
            
        
        aans = []
        
        for k in ans:
            kk = "".join(k)
            aans.append(kk)
        
        aaans = " ".join(aans)
        
        return aaans


    elif un == 1:
        
        bans = []
        
        for ii in text:
        
            ii_list = list(ii)
            addd = ii_list[-3]
            ii_list.remove(addd)
            ii_list.insert(0,addd)
            ii_list.remove(ii_list[-1])
            ii_list.remove(ii_list[-1])
            bans.append(ii_list)
            
        
        baans = []
        
        for jk in bans:
            jkk = "".join(jk)
            baans.append(jkk)
        
        baaans = " ".join(baans)
        
        return baaans
    


print(piglatin("Iii wan too have rough sex with you",1))

