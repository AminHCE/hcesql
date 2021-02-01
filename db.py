import ast


def clear(db_name):
    file = open(db_name, 'wb')
    file.write(str('').encode('ascii'))
    file.close()


def write(data, db_name):
    file = open(db_name, 'wb')
    file.write(str(data).encode('ascii'))
    file.close()


def read(db_name):
    file = open(db_name, 'rb')
    line = file.read()
    if line:
        return ast.literal_eval(line.decode('ascii'))
    else:
        return []


def get_student(data, switch):
    return '{st_code},{st_name},{st_family}'.format(
        st_name=data['st_name'],
        st_family=data['st_family'],
        st_code=data['st_code']
    )


def create_student(data):
    if (len(data['st_name']) > 20) or (type(data['st_name']) is not str):
        return None

    elif (len(data['st_family']) > 20) or (type(data['st_family']) is not str):
        return None

    elif type(data['st_code']) is not int:
        try:
            data['st_code'] = int(data['st_code'])

        except:
            print('error3')
            return None

    data['st_name'] = data['st_name'].replace("_", " ")
    data['st_family'] = data['st_family'].replace("_", " ")

    return data


def get_course(data, switch):
    return '{course_code},{course_name}'.format(
        course_code=data['course_code'],
        course_name=data['course_name']
    )


def create_course(data):
    if (len(data['course_name']) > 20) or (type(data['course_name']) is not str):
        return None

    elif type(data['course_code']) is not int:
        try:
            data['course_code'] = int(data['course_code'])

        except:
            return None

    data['course_name'] = data['course_name'].replace("_", " ")

    return data


def get_student_course(data, switch):
    return '{data}'.format(data=data[switch])


def create_student_course(data):
    if type(data['st_code']) is not int:
        try:
            data['st_code'] = int(data['st_code'])

        except:
            return None

    if type(data['course_code']) is not int:
        try:
            data['course_code'] = int(data['course_code'])

        except:
            return None

    data['active'] = 1
    return data
