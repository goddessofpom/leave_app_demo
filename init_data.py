import os
import django

if __name__ == "__main__":
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'leave_app.settings')
    django.setup()

    from django.contrib.auth.models import User, Permission
    from django.contrib.contenttypes.models import ContentType

    content_type = ContentType.objects.get_for_model(User)

    student_perm = Permission.objects.create(codename="student_perm", name="学生权限", content_type=content_type)
    teacher_perm = Permission.objects.create(codename="teacher_perm", name="老师权限", content_type=content_type)

    student = User.objects.create_user(username="student1", password="123456")
    teacher = User.objects.create_user(username="teacher1", password="123456")

    student.user_permissions.add(student_perm)
    teacher.user_permissions.add(teacher_perm)
