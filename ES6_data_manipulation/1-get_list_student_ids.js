export default function getListStudentIds(students) {
  let newArr = [];
  if (students instanceof Array) {
    newArr = students.map((student) => student.id);
  }

  return newArr;
}
