import re

regex_ipv6="(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))"
regex_ipv4="^([01]?\d\d?|2[0-4]\d|25[0-5])(?:\.[01]?\d\d?|\.2[0-4]\d|\.25[0-5]){3}(?:\/[0-2]\d|\/3[0-2])?$"
regex_url="^(?:http(s)?:\/\/)?[\w.-]+(?:\.[\w\.-]+)+[\w\-\._~:/?#[\]@!\$&'\(\)\*\+,;=.]+$"
regex_as="[A][S][0-9]{5,6}"

async def whatis(input: str):
    
    v6=re.compile(regex_ipv6)
    res_v6=v6.match(input)
    v4=re.compile(regex_ipv4)
    res_v4=v4.match(input)
    url=re.compile(regex_url)
    res_url=url.match(input)
    AS=re.compile(regex_as)
    res_as=AS.match(input)
    
    if res_v6!= None:
        return "v6"
    elif res_v4 != None:
        return "v4"
    elif res_url != None:
        return "url"
    elif res_as != None:
        return "AS"
    else:
        return "no_match"
    