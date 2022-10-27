all_students = ["나연", "정연", "모모", "사나", "지효", "미나", "다현", "채영", "쯔위"]
present_students = ["정연", "모모", "채영", "쯔위", "사나", "나연", "미나", "다현"]

# normal way, O(n2)
def get_absent_student(all_array, present_array):
    result = []
    for i in all_array:
        if i not in present_array:
            result.append(i)
    return result

def get_absent_student2(all_array, present_array):
    student_dict = dict()
    for key in all_array: # O(N)
        student_dict[key] = 0
    
    for key in present_array: # O(N)
        del student_dict[key]
        
    for result in student_dict:
        return result


print(get_absent_student(all_students, present_students))
print(get_absent_student2(all_students, present_students))