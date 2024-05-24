export function updateStudentGradeByCity(students, city, newGrades = []) {
    return students
        .filter(({ location }) => location === city)
        .map(student => {
            const gradeObj = newGrades.find(({ studentId }) => studentId === student.id);
            return {
                ...student,
                grade: gradeObj ? gradeObj.grade : 'N/A',
            };
        });
}
