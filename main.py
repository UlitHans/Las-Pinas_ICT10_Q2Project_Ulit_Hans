from pyscript import document

def show_info(event=None):
    output = document.getElementById("output")

    details = [
        "Meeting Time: 3PM - 5PM",
        "Location: Basketball Court",
        "Adviser: Coach Tare",
        "Category: Non-Academic"
    ]

    members = sorted({"Ac Mactal", "Kleiser Fermocil", "Kyler Santos", "Cade Chua", "Victor Buenvinida"})
    positions = ["Guard", "Forward", "Center"]

    result = f"""
        <h5>Club Details</h5>
        <ul>{"".join(f"<li>{item}</li>" for item in details)}</ul>

        <h5>Members</h5>
        <ul>{"".join(f"<li>{m}</li>" for m in members)}</ul>

        <h5>Player Positions</h5>
        <ul>{"".join(f"<li>{p}</li>" for p in positions)}</ul>
    """

    output.innerHTML = result
