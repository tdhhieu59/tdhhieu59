k=open('d:/a.txt','r')
char,wc,lc=0,0,0
for line in k:
    for k in rangge(0,len(line)):
        char +=1
        if(line[k]==' '):
            wc+=1
        if(line[k]=='\n'):
            wc, lc=wc+1, lc=1
print("The no.of chars is %d\n The no.of words in%d\n The no.of lines is %d%(char,wc,lc))
import turtle, random
colors=["red","green","blue","orange","purple","pink","yellow"]
painter=turtle.Turtle()
painter.pensize(3)
for i in range(10):
    color=random.choice(colors)
    painter.pencolor(color)
    painter.circle(100)
    painter.right(30)
    painter.left(60)
    painter.setposition(0, 0)
