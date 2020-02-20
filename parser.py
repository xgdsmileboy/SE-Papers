#!/usr/bin/env python
# coding=utf-8

import json

mapping={'synthesis' : 'program synthesis', 
		'localization' : 'fault localization',
		'repair' : 'program repair'}

def init(topic):
	json_file='%s/%s.json' % (topic.capitalize(), topic)
	target_file='%s/Readme.md' % (topic.capitalize())
	header='### Roadmap for %s\n' % mapping[topic]
	return json_file, target_file, header

def extract_time(json):
    try:
        return int(json['year'])
    except KeyError:
        return 0

def by_date(json_array, header, target_file):
	id = 1
	with open(target_file, 'w') as f:
		f.write(header)
		for item in json_array:
			if item['url'] == "":
				f.write(u'%d. __%s__, *[%s %d]*\n\n' % (id, item['title'], item['conf'], item['year']))
			else:
				f.write(u'%d. __[%s](%s)__, *[%s %d]*\n\n' % (id, item['title'], item['url'], item['conf'], item['year']))
			f.write(u'\t%s\n\n' % item['authors'])
			id = id + 1

if __name__ == '__main__':
	for topic in ['repair','synthesis','localization']:
		json_file, target_file, header = init(topic)
		with open(json_file, encoding='utf-8') as f:
			loaded_json = json.load(f)
			loaded_json.sort(key=extract_time, reverse=True)
			by_date(loaded_json, header, target_file)

