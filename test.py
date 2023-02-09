import selenium_project

adres = selenium_project.deprem_adresi_bul()

with open("list_var.txt", "a") as file:
    for tweet in adres:
        file.write(
            "**************************************************\n")

        file.write("""Tweet:
        Atan: {}

        Zaman: {}

        ICERIK:{}        
        """.format(tweet["UserTags"], tweet["TimeStamps"], tweet["Body"]))

        file.write(
            "**************************************************\n\n")
