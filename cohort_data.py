"""Functions to parse a file containing student data."""


def all_houses(filename):
    """Return a set of all house names in the given file.

    For example:
      >>> unique_houses('cohort_data.txt')
      {"Dumbledore's Army", 'Gryffindor', ..., 'Slytherin'}

    Arguments:
      - filename (str): the path to a data file

    Return:
      - set[str]: a set of strings
    """
    
    house_name = []
    # open file
    file = open(filename)
    # loop through lines
    for line in file:
      line = line.split("|")
      # add name if name exists in line
      if len(line[2]) > 0:
        house_name.append(line[2])
      
    houses = set(house_name)

    return houses


def students_by_cohort(filename, cohort='All'):
    """Return a list of students' full names by cohort.

    Names are sorted in alphabetical order. If a cohort isn't
    given, return a list of all students. For example:
      >>> students_by_cohort('cohort_data.txt')
      ['Adrian Pucey', 'Alicia Spinnet', ..., 'Zacharias Smith']

      >>> students_by_cohort('cohort_data.txt', cohort='Fall 2015')
      ['Angelina Johnson', 'Cho Chang', ..., 'Terence Higgs', 'Theodore Nott']

      >>> students_by_cohort('cohort_data.txt', cohort='Winter 2016')
      ['Adrian Pucey', 'Andrew Kirke', ..., 'Roger Davies', 'Susan Bones']

      >>> students_by_cohort('cohort_data.txt', cohort='Spring 2016')
      ['Cormac McLaggen', 'Demelza Robins', ..., 'Zacharias Smith']

      >>> students_by_cohort('cohort_data.txt', cohort='Summer 2016')
      ['Alicia Spinnet', 'Dean Thomas', ..., 'Terry Boot', 'Vincent Crabbe']

    Arguments:
      - filename (str): the path to a data file
      - cohort (str): optional, the name of a cohort

    Return:
      - list[list]: a list of lists
    """
   
    students = []

    # TODO: replace this with your code
    file = open(filename)
    
    for line in file:
      line = line.split("|")
      # if cohort != "All":
       # print(len(cohort), len(line[4]), cohort, line[4])
      if cohort == "All":
        if len(line[2]) > 0:
            students.append(str(line[0]+" "+ line[1]))
      
      elif line[4].strip() == cohort:
        # print("cohort is ", cohort)
        if len(line[2]) > 0:
          students.append(str(line[0]+" "+ line[1]))
      
  

    return sorted(students)


def all_names_by_house(filename):
    """Return a list that contains rosters for all houses, ghosts, instructors.

    Rosters appear in this order:
    - Dumbledore's Army
    - Gryffindor
    - Hufflepuff
    - Ravenclaw
    - Slytherin
    - Ghosts
    - Instructors

    Each roster is a list of names sorted in alphabetical order.

    For example:
      >>> rosters = hogwarts_by_house('cohort_data.txt')
      >>> len(rosters)
      7

      >>> rosters[0]
      ['Alicia Spinnet', ..., 'Theodore Nott']
      >>> rosters[-1]
      ['Filius Flitwick', ..., 'Severus Snape']

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[list]: a list of lists
    """
    # Harry|Potter|Gryffindor|McGonagall|Fall 2015
    # 0     | 1   | 2         | 3       | 4
    # firstn| last| housename | Advisor | cohort
    # Friendly|Friar|         |         |G
    # Filius|Flitwick|        |         |I

    dumbledores_army = []
    gryffindor = []
    hufflepuff = []
    ravenclaw = []
    slytherin = []
    ghosts = []
    instructors = []

    # TODO: replace this with your code
    file = open(filename)

    for line in file:
      line = line.split("|")

      if line[2].strip() == "Dumbledore's Army":
        dumbledores_army.append(str(line[0]+" "+ line[1]))

      elif line[2].strip() == "Gryffindor":
        gryffindor.append(str(line[0]+" "+ line[1]))
      
      elif line[2].strip() == "Ravenclaw":
        ravenclaw.append(str(line[0]+" "+ line[1]))
      
      elif line[2].strip() == "Slytherin":
        slytherin.append(str(line[0]+" "+ line[1]))
      
      elif line[2].strip() == "Hufflepuff":
        hufflepuff.append(str(line[0]+" "+ line[1]))

      elif len(line[2]) == 0:
        if line[4].strip() == "G":
          ghosts.append(str(line[0]+" "+ line[1]))

        elif line[4].strip() == "I":
          instructors.append(str(line[0]+" "+ line[1]))

      

    return [sorted(dumbledores_army), sorted(gryffindor), sorted(hufflepuff), sorted(ravenclaw), 
            sorted(slytherin), sorted(ghosts), sorted(instructors)]


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (full_name, house, advisor, cohort)

    Iterate over the data to create a big list of tuples that individually
    hold all the data for each person. (full_name, house, advisor, cohort)

    For example:
      >>> all_student_data('cohort_data.txt')
      [('Harry Potter', 'Gryffindor', 'McGonagall', 'Fall 2015'), ..., ]

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[tuple]: a list of tuples
    """
     # Harry|Potter|Gryffindor|McGonagall|Fall 2015
    # 0     | 1   | 2         | 3       | 4
    # firstn| last| housename | Advisor | cohort
    # Friendly|Friar|         |         |G
    # Filius|Flitwick|        |         |I

    all_data = []

    # TODO: replace this with your code
    file = open(filename)
    # loop through file and append
    for line in file:
      line = line.split("|")
      all_data.append((str(line[0] + " "+line[1]), line[2], line[3], line[4].strip()))

    return all_data


def get_cohort_for(filename, name):
    """Given someone's name, return the cohort they belong to.

    Return None if the person doesn't exist. For example:
      >>> get_cohort_for('cohort_data.txt', 'Harry Potter')
      'Fall 2015'

      >>> get_cohort_for('cohort_data.txt', 'Hannah Abbott')
      'Winter 2016'

      >>> get_cohort_for('cohort_data.txt', 'Balloonicorn')
      None

    Arguments:
      - filename (str): the path to a data file
      - name (str): a person's full name

    Return:
      - str: the person's cohort or None
    """

    # open file
    file = open(filename)
    # loop over filenames
    for line in file:
      line = line.split("|") 
      # makes the first name string
      first_name = line[0]+ " "+ line[1]
      # print(first_name, name)
      # check if line is the desired name
      if name == first_name:
        return line[4].strip()
    
    return None


def find_duped_last_names(filename):
    """Return a set of duplicated last names that exist in the data.

    For example:
      >>> find_name_duplicates('cohort_data.txt')
      {'Creevey', 'Weasley', 'Patil'}

    Arguments:
      - filename (str): the path to a data file

    Return:
      - set[str]: a set of strings
    """

    # TODO: replace this with your code
    last_name = []
    duplicates = []
    file_ = open(filename)
    # loop over filenames
    for line in file_:
      # split entries into a list
      line = line.split("|")
      # if the last name is already in last_name, add to duplicates
      if line[1].strip() in last_name:
          duplicates.append(line[1].strip())
      
      last_name.append(line[1].strip())

    return set(duplicates)

    



def get_housemates_for(filename, name):
    """Return a set of housemates for the given student.

    Given a student's name, return a list of their housemates. Housemates are
    students who belong to the same house and were in the same cohort as the
    given student.

    For example:
    >>> get_housemates_for('cohort_data.txt', 'Hermione Granger')
    {'Angelina Johnson', ..., 'Seamus Finnigan'}
    """

    # TODO: replace this with your code
    house_mates = []
    list_of_students = []
    file_ = open(filename)
    # find cohort for the given name in function
    # list_of_all_houses = all_names_by_house(filename)
    # desired_cohort = get_cohort_for(filename, name)
    # loop over filenames
    for line in file_:
      # split entries into a list
      line = line.split("|")
      first_name = line[0].strip() + " "+ line[1].strip()
      # print(first_name, name, len(first_name), len(name))
      if first_name == name:
        house_of_person = line[2]
        needed_cohort = line[4].strip()
        # print(house_of_person)
        break
    
    tuples = all_data(filename)
    for student in tuples:
      if student[3] == needed_cohort and student[1] == house_of_person:
        if student[0] != name:
          house_mates.append(student[0])
      
    
    
    return(set(house_mates))

##############################################################################
# END OF MAIN EXERCISE.  Yay!  You did it! You Rock!
#

if __name__ == '__main__':
    import doctest

    result = doctest.testfile('doctests.py',
                              report=False,
                              optionflags=(
                                  doctest.REPORT_ONLY_FIRST_FAILURE
                              ))
    doctest.master.summarize(1)
    if result.failed == 0:
        print('ALL TESTS PASSED')
