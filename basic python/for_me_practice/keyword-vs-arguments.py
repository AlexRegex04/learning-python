
# Types of Arguments
# 1.Positional arguments

# def team(*arg):
#     print(arg)  # print a tuple
#     print(arg[0], "is working on an", arg[1])


# def team(company, name='Rakib'):
#     print(f"{name} is working on an {company} company")


# team("Wordpress")


# def team(name, project):
#     print(name, "is working on an", project)
# team(project="Edpresso", name='FemCode')


# def team(name, project, members=None):
#     team.name = name
#     team.project = project
#     team.members = members
#     print(name, "is working on an", project)
# team("FemCode", project="Edpresso")

'''
    *args: for non-keyworded/positional arguments
    **kwargs: for keyworded arguments.
'''
# *args


# def team(*members):
#     # members == <class 'tuple'>
#     print(type(members))  # ('Abena', 'Marilyn')
#     for member in members:
#         print(member)


# team("Abena", "Marilyn")

# ! *arg => tuple
# ! **kyword => dictionary

# # #### **kwargs


def team(**details):

    for key, value in details.items():
        print("{}: {}".format(key, value))


team(Name="FemCode", Project="Edpresso", Number="Two Members")


# def team(*members, **features):
#     # ('Abena', 'Marilyn')
#     print(members)

#     # {'Name': 'FemCode', 'Project': 'Edpresso', 'Number': 'Two Members'}

#     print(features)

#     # for member in members:
#     # print(member)

#     # for key, value in features.items():
#     #     print("{}: {}".format(key, value))


# team("Abena", "Marilyn", Name="FemCode",
#      Project="Edpresso", Number="Two Members")
