from js import document

CLUB_INFO = {
    "robotics": {
        "Name": "Robotics Club",
        "Description": "Design, build, and program robots.",
        "Meeting Time": "Tuesday, 3:30-4:30 PM",
        "Location": "Room 101",
        "Adviser": "Mr. Smith",
        "Number of Members": "25",
        "Category": "Academic"
    },
    "mb": {
        "Name": "Marching Band",
        "Description": "Learn and perform various instruments.",
        "Meeting Time": "Mon/Tue, 2:30-4:00 PM",
        "Location": "Room 304",
        "Adviser": "Mr. De Leon",
        "Number of Members": "46",
        "Category": "Non-Academic"
    },
    "glee": {
        "Name": "Glee Club",
        "Description": "Perform vocal music pieces.",
        "Meeting Time": "Tuesday, 3:30-4:30 PM",
        "Location": "Room 203",
        "Adviser": "Mr. Reyes",
        "Number of Members": "29",
        "Category": "Non-Academic"
    },
    "sci": {
        "Name": "Science Club",
        "Description": "Explore scientific fields through experiments.",
        "Meeting Time": "Thursday, 2:30-3:30 PM",
        "Location": "Room 110",
        "Adviser": "Ms. Garcia",
        "Number of Members": "10",
        "Category": "Academic"
    }
}

def show_club_info(*args):
    select_element = document.getElementById("clubs")
    club_key = select_element.value
    
    club = CLUB_INFO.get(club_key)
    result_box = document.getElementById("result-box")
    info_div = document.getElementById("club-info")

    if club:
        info_html = f"""
        <h4 class="text-danger">{club['Name']}</h4>
        <hr>
        <p><strong>Description:</strong> {club['Description']}</p>
        <p><strong>Meeting Time:</strong> {club['Meeting Time']}</p>
        <p><strong>Location:</strong> {club['Location']}</p>
        <p><strong>Adviser:</strong> {club['Adviser']}</p>
        <p><strong>Number of Members:</strong> {club['Number of Members']}</p>
        <p><strong>Category:</strong> <span class="badge bg-secondary">{club['Category']}</span></p>
        """
        
        info_div.innerHTML = info_html
        result_box.style.display = "block"
    else:
        info_div.innerHTML = "<p>Club information not found.</p>"
        result_box.style.display = "block"