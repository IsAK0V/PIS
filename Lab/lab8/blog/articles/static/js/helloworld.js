console.log("helloworld.js loaded");

var groupmates = [
    {
        "name": "Василий",
        "group": "912-2",
        "age": 19,
        "marks": [4, 3, 5, 5, 4]
    },
    {
        "name": "Анна",
        "group": "912-1",
        "age": 18,
        "marks": [3, 2, 3, 4, 3]
    },
    {
        "name": "Георгий",
        "group": "912-2",
        "age": 19,
        "marks": [3, 5, 4, 3, 5]
    },
    {
        "name": "Валентина",
        "group": "912-1",
        "age": 18,
        "marks": [5, 5, 5, 4, 5]
    }
];

console.log(groupmates);

var rpad = function(str, length) {
    str = str.toString();
    while (str.length < length) {
        str = str + ' ';
    }
    return str;
};

var printStudents = function(students) {
    console.log(
        rpad("Имя студента", 15),
        rpad("Группа", 8),
        rpad("Возраст", 8),
        rpad("Оценки", 20)
    );

    for (var i = 0; i <= students.length - 1; i++) {
        console.log(
            rpad(students[i]['name'], 15),
            rpad(students[i]['group'], 8),
            rpad(students[i]['age'], 8),
            rpad(students[i]['marks'], 20)
        );
    }

    console.log('\n');
};

printStudents(groupmates);

var filterStudentsByGroup = function(students, group) {
    var result = [];
    for (var i = 0; i <= students.length - 1; i++) {
        if (students[i]['group'] == group) {
            result.push(students[i]);
        }
    }
    return result;
};

console.log("Студенты группы 912-2:");
printStudents(filterStudentsByGroup(groupmates, "912-2"));