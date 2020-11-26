import sqlite3
from Club import Club



conn = sqlite3.connect("clubs.db")
c = conn.cursor()

club = Club("Academic League", "Swanson", "Priyanka Babu & Nikki Wu", "priyanka.n.babu@gmail.com & nikki.27@gmail.com", "Mon, Teu, Wed. @ 3:32 - 5pm", "L116", "To encourage global awareness through trivia competitions", "Trivia", "Competition", "Academics")
c.execute("""INSERT INTO club_info VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", (club.name, club.staff, club.president, club.email, club.meeting_times, club.location, club.description, club.interest1, club.interest2, club.interest3))

#club = Club("ACE Club", "N/A", "Emma Hong", "emmashines@yahoo.com", "Mondays every other week", "N/A", "Awareness, Community, and Empowerment Club: empowering individuals by adressing local environmental and social health concerns in community", "Environment", "Health", "N/A")
#c.execute("""INSERT INTO club_info VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", (club.name, club.staff, club.president, club.email, club.meeting_times, club.location, club.description), club.interest1, club.interest2, club.interest3)

#club = Club("American Red Cross", "Pytel", "Jean Kim", "jeaneonkim@gmail.com", "Mon. @ Lunch", "K101", "To provide volunteer opportunities and help others in need", "Community", "Health", "Volunteering")
#c.execute("""INSERT INTO club_info VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", (club.name, club.staff, club.president, club.email, club.meeting_times, club.location, club.description, club.interest1, club.interest2, club.interest3))

#club = Club("APC", "Liao", "Daniel Ovedo", "acticingredstone@gmail.com", "Every other thurs. @ 3:30-4:30 pm", "K105", "To bing together students who share an interest in physics", "Physics", "Science", "Academics")
#c.execute("""INSERT INTO club_info VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", (club.name, club.staff, club.president, club.email, club.meeting_times, club.location, club.description, club.interest1, club.interest2, club.interest3))

#club = Club("Best Buddies", "Conlon", "Toby Gallant & Bella Genovese", "tobyjgallant@gmail.com & iagenovese4@gmail.com", "Mon. @ Lunch", "J112, P111, PAC Lawn", "To create friendships with students with and without IDD", "Community", "Health", "Friendship")
#c.execute("""INSERT INTO club_info VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", (club.name, club.staff, club.president, club.email, club.meeting_times, club.location, club.description, club.interest1, club.interest2, club.interest3))

conn.commit()
conn.close()
