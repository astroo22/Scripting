#jonathan starkey
#! python3

start = {'Weezer': {'Jan 30, 2018': ['Concrete Gold', 'Etihad Stadium', 'Melbourne, VIC'],
                'Jun 16, 2018': ['Montebello Rockfest 2018', 'Montebello Marina', 'Montebello, QC']},
     'Tenacious D': {'May 06, 2018': ['Shaky Knees Music Festival 2018', 'Central Park', 'Atlanta, GA'],
                     'Jun 16, 2018': ['Montebello Rockfest 2018', 'Montebello Marina', 'Montebello, QC']},
     'Lamb of God': {'Jun 09, 2018': ['Final World Tour: North America 2018', 'Keybank Pavilion', ' \tBurgettstown, PA'],
                     'Jun 16, 2018': ['Montebello Rockfest 2018', 'Montebello Marina', 'Montebello, QC']},
     'Ed Sheeran': {'Mar 10, 2018': ['Ed Sheeran with Missy Higgins', 'Etihad Stadium', ' \tMelbourne, VIC']},
     'Cold War Kids': {'Jun 02, 2018': ['XFEST 2018', 'Keybank Pavilion', 'Burgettstown, PA']},
     'Steel Panther': {'Oct 21, 2017': ['Aftershock', 'Discovery Park', 'Sacramento, CA']}}


counter = 0
l = []
for k,v in start.items():
    l.append([k])
    l.append(start[k])
    
    
    
print(l[1])
