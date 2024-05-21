export function getStudentsByLocation(students, city) {
    const studentsCity = students.filter(student => student.location === city);
    return studentsCity;
}

