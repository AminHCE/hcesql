from db import create_student, create_course, create_student_course, get_student, get_course, get_student_course, \
    read, write, clear


def check_value(value):
    return True if '=' in value else False


def commander(command):
    command_ = command.split(' ')
    if command_[0] == 'insert':
        db_name = command_[2]
        value_1 = command_[-1]
        value_2 = command_[-2]
        value_3 = command_[-3]

        data = {}
        if check_value(value_1):
            value_ = value_1.split('=')
            data[value_[0]] = value_[1]
        if check_value(value_2):
            value_ = value_2.split('=')
            data[value_[0]] = value_[1]
        if check_value(value_3):
            value_ = value_3.split('=')
            data[value_[0]] = value_[1]

        function_name = 'create_' + db_name
        result = eval(function_name + "(data)")

        db_file_name = db_name + '.bin'
        db_data = read(db_file_name)
        db_data.append(result)
        write(db_data, db_file_name)
        return 'done'

    if command_[0] == 'update':
        db_name = command_[1]
        query_value = command_[-1]
        update_value = command_[-3]

        query_data = []
        update_data = []
        if check_value(query_value):
            query_data = query_value.split('=')
        if check_value(update_value):
            update_data = update_value.split('=')

        db_file_name = db_name + '.bin'
        db_data = read(db_file_name)

        for item in db_data:
            if 'code' in query_data[0]:
                query_data[1] = int(query_data[1])
            if 'code' in update_data[0]:
                update_data[1] = int(update_data[1])

            if item[query_data[0]] == query_data[1]:
                item[update_data[0]] = update_data[1]

        clear(db_file_name)
        write(db_data, db_file_name)
        return 'done'

    if command_[0] == 'delete':
        db_name = command_[2]
        value_1 = command_[-1]
        value_2 = command_[-3]

        value1 = []
        value2 = []
        if check_value(value_1):
            value1 = value_1.split('=')
        if check_value(value_2):
            value2 = value_2.split('=')

        db_file_name = db_name + '.bin'
        db_data = read(db_file_name)

        for item in db_data:
            if 'code' in value1[0]:
                value1[1] = int(value1[1])
            if 'code' in value2[0]:
                value2[1] = int(value2[1])

            if item[value1[0]] == value1[1] and item[value2[0]] == value2[1]:
                item['active'] = 0

        clear(db_file_name)
        write(db_data, db_file_name)
        return 'done'

    if command_[0] == 'select':
        db_name = command_[2]
        value_1 = command_[-1]

        value_ = []
        if check_value(value_1):
            value_ = value_1.split('=')

        db_file_name = db_name + '.bin'
        db_data = read(db_file_name)

        query = ''
        for item in db_data:
            if 'code' in value_[0]:
                value_[1] = int(value_[1])

            switch = ''
            if value_[0] == 'st_code':
                switch = 'course_code'
            else:
                switch = 'st_code'

            if item[value_[0]] == value_[1]:
                function_name = 'get_' + db_name
                result = eval(function_name + "(item, switch)")
                query += result + '\n'

        return query
