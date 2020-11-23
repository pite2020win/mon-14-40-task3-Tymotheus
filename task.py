from School import School, Student, Class
import logging


def main():
    logging.basicConfig(level=logging.INFO, format='%(message)s')

    logging.info("Initialising the class diary")
    students = [Student("Duncan Idaho", [4.0, 5.0, 4.5]), Student("Paul Atreides", [5.0, 5.0, 5.0]),
                Student("Gurney Halleck", [4.0, 4.0, 4.5]), Student("Leto Atreides", [5.0, 4.0, 4.5]),
                Student("Thufir Hawat", [5.0, 4.0, 4.5]), Student("Miles Teg", [5.0, 5.0, 5.0, 4.5])]

    students_more = [Student("Vladimir Harkonnen", [3.0, 3.0, 3.0, 3.0]), Student("Feyd Rautha", [4.0, 2.0, 5.0]),
                     Student("Peter de Vries", [4.0, 3.5, 4.0])]

    students_other_school = [Student("Shaddam Corrino", [4.0, 3.5]), Student("Irulan Corrino", [4.5, 4.5]),
                             Student("Farad'n Corrino", [5.0, 5.0, 4.5])]
    class1 = Class("1A", students)
    class2 = Class("1B", students_more)
    class3 = Class("3C", students_other_school)

    class3.print_students()
    logging.info("Class {} average is {}".format(class3.name, class3.class_average()))

    school1 = School("Arrakis", [class1, class2])
    school2 = School("Salusa Secundus", [class3])
    logging.info("\nGetting the overall school average")
    logging.info("School {} average: {}".format(school1.name, school1.total_average()))
    logging.info("School {} average: {}".format(school2.name, school2.total_average()))

    logging.info("\nChecking average by student's name and class name")
    logging.info("Average of {} is {}".format("Paul Atreides", school1.get_student_average("1A", "Paul Atreides")))
    logging.info("\nChecking average of non existing student")
    logging.info("Average of {} is {}".format("Serena Butler", school1.get_student_average("0X", "Serena Butler")))

    logging.info("\nGetting full information about the particular student")
    logging.info(school1.classes[0].students[0].get_full_info())

    logging.info("")
    school1.print_all_students()
    school1.save_school_to_json()
    school2.save_school_to_json()


if __name__ == "__main__":
    main()
