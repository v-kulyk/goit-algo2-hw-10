class Teacher:
    def __init__(self, first_name, last_name, age, email, can_teach_subjects):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.can_teach_subjects = set(can_teach_subjects)
        self.assigned_subjects = set()

def create_schedule(subjects, teachers):
    remaining_subjects = set(subjects)
    selected_teachers = []
    
    # Reset assigned subjects for all teachers
    for teacher in teachers:
        teacher.assigned_subjects = set()
    
    while remaining_subjects:
        best_teacher = None
        best_coverage = 0
        best_age = float('inf')
        
        for teacher in teachers:
            if teacher in selected_teachers:
                continue
            # Calculate the coverage for current teacher
            coverage = teacher.can_teach_subjects & remaining_subjects
            coverage_count = len(coverage)
            
            if coverage_count == 0:
                continue
            
            # Update best_teacher based on coverage and age
            if coverage_count > best_coverage:
                best_coverage = coverage_count
                best_teacher = teacher
                best_age = teacher.age
            elif coverage_count == best_coverage:
                if teacher.age < best_age:
                    best_teacher = teacher
                    best_age = teacher.age
        
        # If no teacher can cover remaining subjects, return None
        if best_teacher is None:
            return None
        
        # Assign the covered subjects to the best_teacher
        covered_subjects = best_teacher.can_teach_subjects & remaining_subjects
        best_teacher.assigned_subjects = covered_subjects.copy()
        selected_teachers.append(best_teacher)
        remaining_subjects -= covered_subjects
    
    return selected_teachers

if __name__ == '__main__':
    subjects = {'Математика', 'Фізика', 'Хімія', 'Інформатика', 'Біологія'}
    
    teachers = [
        Teacher('Олександр', 'Іваненко', 45, 'o.ivanenko@example.com', {'Математика', 'Фізика'}),
        Teacher('Марія', 'Петренко', 38, 'm.petrenko@example.com', {'Хімія'}),
        Teacher('Сергій', 'Коваленко', 50, 's.kovalenko@example.com', {'Інформатика', 'Математика'}),
        Teacher('Наталія', 'Шевченко', 29, 'n.shevchenko@example.com', {'Біологія', 'Хімія'}),
        Teacher('Дмитро', 'Бондаренко', 35, 'd.bondarenko@example.com', {'Фізика', 'Інформатика'}),
        Teacher('Олена', 'Гриценко', 42, 'o.grytsenko@example.com', {'Біологія'}),
    ]
    
    schedule = create_schedule(subjects, teachers)
    
    if schedule:
        print("Розклад занять:")
        for teacher in schedule:
            subjects_list = sorted(list(teacher.assigned_subjects))
            print(f"{teacher.first_name} {teacher.last_name}, {teacher.age} років, email: {teacher.email}")
            print(f"   Викладає предмети: {', '.join(subjects_list)}\n")
    else:
        print("Неможливо покрити всі предмети наявними викладачами.")