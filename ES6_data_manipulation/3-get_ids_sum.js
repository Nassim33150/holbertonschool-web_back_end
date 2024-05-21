export function getStudentIdsSum() {
	const sumIds = students.reduce((sum, student) => sum + student.id, 0);

	return sumIds;
}
