fk = "com.rafalbuchner.mirroringDrawingGlobal"
gk = "com.rafalbuchner.mirroringDrawingLocal"
f = CurrentFont()
for g in f:
	if gk in g.lib:
		del g.lib[gk]
if fk in f.lib:
	del f.lib[fk]