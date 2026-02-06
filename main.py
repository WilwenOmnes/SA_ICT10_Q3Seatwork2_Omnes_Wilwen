from pyscript import display, document


def intrams_checker(e):
    document.getElementById('output').innerHTML = ''
    document.getElementById('image').innerHTML = ''

    reg_el = document.querySelector('input[name="registration"]:checked')
    clear_el = document.querySelector('input[name="clearance"]:checked')

    if reg_el is None or clear_el is None:
        display("Please answer all Yes / No questions.", target="output")
        return

    registration = reg_el.value
    clearance = clear_el.value
    pe_grade = document.getElementById("pe_grade").value
    grade_level = int(document.getElementById("level").value)
    section = document.getElementById("section").value
    sport = document.getElementById("sport").value

    # third option in case you cant reselect yes or no
    if registration == "undecided" or clearance == "undecided":
        display("Please pick yes or no.", target="output")
        return

    if registration != "registered":
        display(
            "Not eligible: student is not registered for Intrams.",
            target="output"
        )
        return

    if clearance != "cleared":
        display(
            "Not eligible: medical clearance required.",
            target="output"
        )
        return

    # If elif and else statements plus specifications if you are part of the team or not instantly.
    if grade_level in [7, 10] and section == "emerald":
        display(
            f"Congrats! You are part of the Green Hornets {sport.title()} Tryout!",
            target="output"
        )
        document.getElementById("image").innerHTML = "<img src='GREEN.jpg'>"

    elif grade_level in [7, 10] and section == "ruby":
        display(
            f"Congrats! You are part of the Yellow Tigers {sport.title()} Tryout!",
            target="output"
        )
        document.getElementById("image").innerHTML = "<img src='YELLOW.jpg'>"

    elif grade_level in [8, 9] and section == "emerald":
        display(
            f"Congrats! You are part of the Red Bulldogs {sport.title()} Tryout!",
            target="output"
        )
        document.getElementById("image").innerHTML = "<img src='RED.jpg'>"

    elif grade_level in [8, 9] and section == "ruby":
        display(
            f"Congrats! You are part of the Blue Bears {sport.title()} Tryout!",
            target="output"
        )
        document.getElementById("image").innerHTML = "<img src='BLUE.jpg'>"

    else:
        display(
            "Congrats! You are registered for Intrams. Please wait for further instructions.",
            target="output"
        )