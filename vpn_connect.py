
session_dict = {}
for line in open('vpn_connect.csv','r'):
    tup = str(line.strip()).split(',')
    t = tup[0]
    userid = tup[1]
    event_name = tup[2]
    version = tup[3]
    session_id = tup[4]
    sessionId = tup[5]
    #print('%s\t%s\t%s\t%s\t%s\t%s'%(t,userid,event_name,version,session_id,sessionId))
    sid = ''
    if (event_name == 'vpn_connect_step'):
        sid = userid+'_'+session_id
    else:
        sid = userid+'_'+ sessionId

    if not sid in session_dict:
        session_dict[sid] = []
    session_dict[sid].append(event_name)

for k in session_dict:
    v = session_dict[k]
    print(k,v)