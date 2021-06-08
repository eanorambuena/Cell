from main import n
from cell import *
c1=Cell("c1","main",1)
c1.reproduction()
execute(c1.newname)
if c1.count==n:
 clearall(n)