def generate_invitations(template, attendees):
    if type(template) != str:
        print("Error: template must be a string.")
        return

    if type(attendees) != list:
        print("Error: attendees must be a list.")
        return

    if template == "":
        print("Template is empty, no output files generated.")
        return

    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    for i in range(len(attendees)):
        person = attendees[i]

        name = person.get("name", "N/A")
        event_title = person.get("event_title", "N/A")
        event_date = person.get("event_date", "N/A")
        event_location = person.get("event_location", "N/A")

        result = template
        result = result.replace("{name}", str(name))
        result = result.replace("{event_title}", str(event_title))
        result = result.replace("{event_date}", str(event_date))
        result = result.replace("{event_location}", str(event_location))

        file = open(f"output_{i+1}.txt", "w")
        file.write(result)
        file.close()
