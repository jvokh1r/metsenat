from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import SponsorStudent, Sponsor, Student


@receiver(pre_save, sender=Student)
def update_sponsor_and_student(sender, instance, **kwargs):
    # Получаем текущий объект Student из базы данных
    if instance.pk:
        old_student = Student.objects.get(pk=instance.pk)
    else:
        old_student = None

    # Проверяем изменение поля contract
    if old_student and instance.contract != old_student.contract and instance.contract < old_student.contract:
        # Вычисляем разницу в контрактах
        contract_diff = old_student.contract - instance.contract

        # Обновляем spend_amount у связанных спонсоров
        sponsors = Sponsor.objects.filter(sponsorstudent__student=instance)
        for sponsor in sponsors:
            sponsor.spend_amount -= contract_diff
            sponsor.save()

        # Обновляем sponsored_amount у текущего студента
        instance.sponsored_amount = contract_diff


        # Обновляем amount у связанных спонсоров
        for sponsor in sponsors:
            sponsor.amount += contract_diff
            sponsor.save()
