const club_display = document.getElementsByClassName("card-list")[0];

function createClubCard(_name, _staff, _president, _email, _meeting_times, _location, _description, in1, in2, in3) {
	const card = document.createElement('article');
	card.className = "card";

	const name = document.createElement('h2');
	name.className = "card-header";
	name.innerText = _name;

	const president = document.createElement('p');
	president.className = "card-header";
	president.innerText = _president;

	const meeting_times = document.createElement('p');
	meeting_times.className = "card-header";
	meeting_times.innerText = _meeting_times;

	const email = document.createElement('p');
	email.className = "card-header";
	email.innerText = "Email: " _email;

	const description = document.createElement('p');
	description.className = "card-header";
	description.innerText = _description;

	const interest1 = document.createElement('a');
	interest1.className = "tags";
	interest1.innerText = in1;

	card.append(name);
	card.append(president);
	card.append(meeting_times);
	card.append(email);
	card.append(description);
	card.append(interest1);

	return card;
}

//club_display.appendChild(createClubCard("testing", "liao", "abhinav", "abhinav.palacharla@gmail.com", "Monday (3pm), Friday (Lunch)", "A101", "this is just a test.", "science", "computer science", "business"));
