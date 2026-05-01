def suggest_career(personality):

    career_map = {
        "extrovert": [
            "Human Resource Manager",
            "Marketing Manager",
            "Sales Executive",
            "Public Relations Officer",
            "Business Development Manager"
        ],
        "introvert": [
            "Software Developer",
            "Data Analyst",
            "Graphic Designer",
            "Research Scientist",
            "Content Writer"
        ]
    }

    return career_map.get(personality, ["Career not found"])