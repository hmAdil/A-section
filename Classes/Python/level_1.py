def readfile():
    with open('music_festival.txt','r') as f:
        rows=f.readlines()
    return rows
def subproblem1():
    rows=readfile()
    genres=[]
    count=0
    for line in rows:
        count+=1
        rec=line.split(',')
        print(rec)
        genre=rec[1].strip()
        print(genre)
        if genre not in genres:
            genres.append(genre)
    return(count,len(genres))
def subproblem2(event_type,artist,gener,date,time,stage):
    new_event=f"{event_type}:{artist},{gener},{date},{time},{stage}:\n"
    rows=readfile()
    with open ("music_festival.txt",'a') as f1:
        if not rows[-1].endswith('\n'):
            f1.write('\n')
        f1.write(new_event)
    print('New event inserted.')

def subproblem3():
    rows = readfile()
    genre_count = {}
    for line in rows:
        genre =line.split(",")[1].strip()
        if genre in genre_count:
            genre_count[genre]+=1
        else:
            genre_count[genre]=1
    if genre_count:
        print("event count by genre")
        for genre,count in genre_count.items():
            print(f'{genre}:{count}')
    else:
        print('no data to display')

def subproblem4(artist_name):
    rows=readfile()
    flag=0
    for line in rows:
        artist=line.split(',')[0].split(':')[1].strip()
        if artist.lower()== artist_name.lower():
            rows.remove(line)
            flag=1
        with open ('music_festival.txt',"w") as f1:
            f1.writelines(rows)
        if flag:
            print(f'event by {artist_name} is removed')
        else:
            print(f'no event found by {artist_name}')
 

def subproblem5():
    time_count ={}
    rows = readfile()
    for line in rows:
        time = line.split(',')[3].strip()
        if time in time_count:
            time_count[time]+=1
        else:
            time_count[time]=1
    if time_count:
         for time , count in time_count.itmes():
             print(f'{time}:{count} events')
    else:
        print(f'no event found')
        
def subprobleem6():
    rows = readfile()
    genre_summary={}

    for line in rows:
        rec = line.split(',')
        genre = rec[1].split()
        event_type=rec[0].split(':')[0].split
        artist=rec[0].split(':')[1].strip()
        if genre not in genre_summary:
            genre_summary[genre]-[]
            genre_summary[genre].append(f'{event_type} by {artist}')

    if genre_summary:
        print('total events: ' , sum(len(events) for events in genre_summary.values()))
    print(genre_summary)

def subproblem7():
    open("music_festival.txt","w").close()
    print("all events are deleted")

def return_artist(x):
    return x[0].split(':')[1].strip()

def subproblem8():
    rows = readfile()
    events = []
    for line in rows:
        rec = line.split(',')
        events.append(rec)
    if events:
        events.sort(key=return_artist)
        for events in events:
            print(','.join(event).strip())
        else:
            print('no event to display')

    
while True:
    print('enter subproblem choice and enter 0 to exit\n')
    ch=int(input('enter choice'))
    if ch==1:
        total_events,unique_genres = subproblem1()
        if total_events==0 and unique_genres==0:
            print('no data')
        else:
            print(f'total events are {total_events}')    
            print(f'unique genres are {unique_genres}')
    elif ch==2:
        event_type=input("enter event type").strip()
        artist=input("enter artist").strip()
        genre=input("enter genre").strip()
        date=input("enter date as YYYY-MM-DD").strip()
        time=input("enter time as HH:MM AM/PM").strip()
        stage=input("enter stage number").strip()
        subproblem2(event_type,artist,genre,date,time,stage)

    elif ch==3:
        subproblem3()
    elif ch==4:
        artist_name =input("enter artist name").strip()
        subproblem(artist_name)

    elif ch==5:
        subproblem5()

    elif ch==6:
        subproblem6()

    elif ch==7:
        subproblem7()

    elif ch == 8:
        subproblem8()
        
    elif ch==0:
        break

    else:
        print('invalid choice')    
