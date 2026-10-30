import sqlite3
conn = sqlite3.connect('youtube_video.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos(
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        time TEXT NOT NULL
    )
''')
def List_videos():
    cursor.execute('SELECT * FROM videos')
    for rows in cursor.fetchall():
        print(rows)

def Add_videos(name,time):
    cursor.execute(
        "INSERT INTO videos(name,time) VALUES(?,?)",
        (name,time))
    conn.commit()

def update_videos(video_id,new_videos,new_time):
    cursor.execute(
        'UPDATE videos SET name = ?,time=? WHERE id=?'
        ,(new_videos,new_time,video_id))
    conn.commit()

def delete_videos(videos_id):
    cursor.execute('DELETE FROM videos WHERE id = ?',(videos_id,))
    conn.commit()
    
def main():
    while True:
        print("\n Youtube manager app with db")
        print('1.List videos')
        print('2.Add videos')
        print('3.Update videos')
        print('4.Delete videos')
        print('5.exist')
        choice = input('enter the choice :')

        if choice == '1':
            List_videos()
        elif choice == '2':
            name = input("enter the videos name:")
            time = input('enter the time:')
            Add_videos(name,time)
        elif choice == '3':
            videos_id = input("enter the videos id:")
            name = input("enter the videos name:")
            time = input("enter the time :")
            update_videos(videos_id,name,time)
        elif choice =='4':
            videos_id = input("enter the videos name:")
            delete_videos(videos_id)
        elif choice == '5':
            exit()
        else:
            print("invalid operations")
            
if __name__ == "__main__":
    try:
        main()
    finally:
        conn.close()


