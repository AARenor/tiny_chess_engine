import json,os,urllib.request as u
U=os.getenv("MAKEFUN_ENV_URL","")
V=[0,100,320,330,500,900,0]
IM=9999
N8=(33,31,18,14,-14,-18,-31,-33)
R4=(1,16,-1,-16)
B4=(15,17,-15,-17)
D8=R4+B4
bd=[0]*128;stm=0;ep=-1;cr="";kg=[4,116];hs=[];nodes=0;BUD=65000;pl=[];K=[0]*64;kp=0
T=[[0]*128 for _ in range(8)]
for i in range(128):
 if i&0x88:continue
 r,f=i>>4,i&7;c=abs(2*f-7)+abs(2*r-7)
 T[1][i]=4*r+(14 if r>2 and 2<f<5 else 0)
 T[2][i]=24-3*c;T[3][i]=16-2*c;T[4][i]=(0,0,6,10,15,25,0,0)[r]
 T[6][i]=(0,25,15,0,0,15,25,0)[f]-12*r;T[7][i]=28-3*c
class S(Exception):pass
def load(f):
 global bd,stm,ep,cr,kg,pl
 p=f.split();bd=[0]*128;pl=[];s=112
 for c in p[0]:
  if c=="/":s-=24;continue
  if c<"9":s+=int(c);continue
  v=".PNBRQKpnbrqk".index(c);v=v if v<7 else v+2;bd[s]=v;pl.append(s)
  if v&7==6:kg[v>>3]=s
  s+=1
 stm=p[1]<"c";cr=p[2]
 ep=-1 if p[3]=='-' else (int(p[3][1])-1)*16+"abcdefgh".index(p[3][0])
def atk(s):
 global stm
 o=bd[s];bd[s]=1+8*stm
 stm^=1;r=any(m[2]==s for m in gen(1));stm^=1
 bd[s]=o
 return r
def gen(cap=0):
 ms=[];b=bd;s=stm;d=16-32*s
 for f in pl:
  p=b[f]
  if p>>3!=s:continue
  t=p&7
  if t==1:
   to=f+d
   if not to&0x88 and not b[to]:
    if to>>4 in(0,7):ms.append((900,f,to,5))
    elif not cap:
     ms.append((f*128+to==kp,f,to,0))
     if f>>4==1+5*s and not b[to+d]:ms.append((0,f,to+d,0))
   for dd in (d-1,d+1):
    to=f+dd
    if to&0x88:continue
    q=b[to]
    if q and q>>3!=s:ms.append((800+V[q&7],f,to,5) if to>>4 in(0,7) else (V[q&7]*8,f,to,0))
    elif to==ep:ms.append((800,f,to,0))
  else:
   ds=(N8,B4,R4,D8,D8)[t-2]
   for dd in ds:
    to=f+dd
    while not to&0x88:
     q=b[to]
     if q:
      if q>>3!=s:ms.append((V[q&7]*8-V[t],f,to,0))
      break
     if not cap:ms.append((f*128+to==kp,f,to,0))
     if t==2 or t==6:break
     to+=dd
   if t==6 and not cap and f in(4,116):
    for k in(2,-2):
     if "KQkq"[2*s+(k<0)] in cr and not b[f+k//2] and not b[f+k] and not(k<0 and b[f-3]) and not atk(f) and not atk(f+k//2) and not atk(f+k):ms.append((0,f,f+k,0))
 return ms
def mk(f,to,pr):
 global ep,cr,stm,bd,kg,pl
 hs.append((bd[:],cr,ep,kg[:],stm,pl[:]))
 p=bd[f];t=p&7
 if t==1 and to==ep and not bd[to]:q=to+32*stm-16;bd[q]=0;pl.remove(q)
 if t==6 and abs(to-f)==2:
  rf,rt=(f+3,to-1) if to>f else (f-4,to+1)
  bd[rf]=0;bd[rt]=p-2;pl.remove(rf);pl.append(rt)
 q=bd[to]
 if q:pl.remove(to)
 bd[f]=0;bd[to]=pr+8*stm if pr else p;pl.remove(f);pl.append(to)
 if t==6:kg[stm]=to
 ep=-1
 if t==1 and abs(to-f)==32:ep=(f+to)>>1
 for i in (f,to):cr=cr.replace({0:"Q",4:"KQ",7:"K",112:"q",116:"kq",119:"k"}.get(i,""),"")
 stm^=1
def um():
 global ep,cr,stm,bd,kg,pl
 bd,cr,ep,kg,stm,pl=hs.pop()
def ev():
 s=m=bw=bb=0
 for i in pl:
  p=bd[i]
  t=p&7;w=p<9
  s+=(V[t]+T[t][i if w else i^112])*(2*w-1)
  if t>1:m+=V[t]
  if t==3:bw+=w;bb+=1-w
 k=T[6+(m<3600)]
 s+=k[kg[0]]-k[kg[1]^112]+(bw>1)*30-(bb>1)*30
 return s-2*s*stm
def ab(d,a,b,ply):
 global nodes,kp
 nodes+=1
 if nodes>BUD:raise S
 if bd[kg[stm]]!=6+8*stm:return -IM+ply
 if d<1:
  s=ev()
  if s>a:a=s
  best=a
  if a>=b:return a
  ms=gen(1)
 else:
  best=-IM+ply
  kp=K[ply]
  ms=gen()
 ms.sort(reverse=True)
 for sc,f,to,pr in ms:
  mk(f,to,pr);v=-ab(d and d-1,-b,-a,ply+1);um()
  if v>best:best=v
  if v>a:
   a=v
   if a>=b:
    if d and not pr:K[ply]=f*128+to
    return v
 sp=2-IM+ply
 return(atk(kg[stm])and-IM+ply or 0)if best==sp else best
def think(fen,legal):
 global nodes
 nodes=0;K[:]=[0]*64;load(fen)
 sq=lambda s:ord(s[0])-97+(int(s[1])-1)*16
 ms=[(sq(m[:2]),sq(m[2:4]),5 if len(m)>4 else 0,m) for m in legal]
 best=ms[0][3];order=[*range(len(ms))]
 for d in range(1,40):
  sc={};a=-IM
  try:
   for i in order:
    mk(*ms[i][:3]);v=-ab(d-1,-IM,-a,1);um();sc[i]=v
    if v>a:a=v;best=ms[i][3]
  except S:
   while hs:um()
   break
  order.sort(key=lambda i:-sc[i])
 return best
def post(p,b):
 return json.load(u.urlopen(u.Request(U+p,json.dumps(b).encode())))
def main():
 g=post("/game",{})
 while g["status"]!="done":
  if g["status"]=="your_move":g=post("/move",{"game":g["game"],"move":think(g["fen"],g["legal_moves"])})
  else:g=post("/game",{})
U and main()
