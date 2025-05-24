# Example CLI input and expected results
format:
 Description
 CLI Input
 Expected URL fetch

### base url: 
python main.py 
https://himalayas.app/jobs

### job specific:
python main.py -r 'software engineer'
https://himalayas.app/jobs/software-engineer

### job and country:
python main.py -r 'software engineer' -l 'united states'
https://himalayas.app/jobs/countries/united-states/software-engineer


### job, country, and experience:
python main.py -r 'software engineer' -l 'united states' -e 'entry level'
https://himalayas.app/jobs/countries/united-states/software-engineer?experience=entry-level

### job, country, 2 experiences, 6 job types:
python main.py -r 'software engineer' -l 'united states' -e 'entry level, mid-level' -t 'part time, contractor, temporary, intern, volunteer, other'
https://himalayas.app/jobs/countries/united-states/software-engineer?experience=entry-level%2Cmid-level&type=part-time%2Ccontractor%2Ctemporary%2Cintern%2Cvolunteer%2Cother

### page 5 base url
python main.py -p 5
https://himalayas.app/jobs/p=5

https://himalayas.app/jobs/countries/united-states/software-engineer?&entry-level&full-time