import json

def formatJSON(source):
	rest = json.loads(source)
	return json.dumps(rest, ensure_ascii=False, indent=4, separators=(',', ':'))

if __name__ == '__main__':
	print(formatJSON('''
		[{"field":"affirmInstructionName","sort":"asc"},
		{"field":"affirmInstructionCode","sort":"desc"},
		{"field":"affirmInstructionName","sort":"desc"}]
		'''))