t=int(input())
while(t):
    a1,b1= map(int,input().split())
    a2,b2= map(int,input().split())
    a3,b3= map(int,input().split())
    a4,b4= map(int,input().split())
    a=[a1,a2,a3,a4]
    print((max(a)-min(a))**2)
    
    
    t-=1