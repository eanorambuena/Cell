from mother import n
from cell import *
celular1=Cell("celular1","mother",1)
celular1.reproduction()
execute(celular1.newname)
if celular1.count==n:
 clearall(n)