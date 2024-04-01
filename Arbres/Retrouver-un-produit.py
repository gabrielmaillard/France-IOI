int(input())
KversCode = ["."] + list(map(int, input().split()))

def CodeVersCode(code_): 
	if KversCode[code_] == 0:
		print(code_, end=" ")
	else:
		CodeVersCode(KversCode[code_])
		print(code_, end=" ")

int(input())
codesRecherches = list(map(int, input().split()))

for codeRecherche in codesRecherches:
	CodeVersCode(codeRecherche)
	print()