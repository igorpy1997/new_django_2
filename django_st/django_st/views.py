from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django_st.models import User


class ItemView(TemplateView):
    template_name = "main_screen.html"

    def get(self, request, *args, **kwargs):
        return render(request=request, template_name=self.template_name)


class ElementsView(TemplateView):
    template_name = "show_student_list.html"

    def get(self, request, *args, **kwargs):
        # usr = User(name="Igor", language="J")  # create new model instance
        # usr.save()  # seve to db
        users = User.objects.all().values()
        # print(users)
        return render(request=request, template_name=self.template_name, context={"users": users})


class AddElementView(TemplateView):
    template_name = "add_menu.html"

    def get(self, request, *args, **kwargs):
        return render(request=request, template_name=self.template_name)

    def post(self, request, *args, **kwargs):
        new_user = User(
            name=request.POST.get("name", ''),
            language=request.POST.get("language", ''),
            course=request.POST.get("course", ''),
            grade=request.POST.get("grade", '')
        )
        new_user.save()
        return redirect('/show_base_elements')

class DeleteElementView(TemplateView):

    def post(self, request, *args, **kwargs):
        delete_user = User.objects.filter(id=request.POST.get("user_id", ''))
        delete_user.delete()
        return redirect('/show_base_elements')

class EditUserView(TemplateView):

    template_name = "edit_menu.html"

    def get(self, request, id, *args, **kwargs):
        user = User.objects.get(id=int(id))
        print(user)
        return render(request=request, template_name=self.template_name, context={"user": user})

    def post(self, request, *args, **kwargs):
        user_id = kwargs['id']  # Отримати id користувача з URL-шаблону
        try:
            edited_user = User.objects.get(id=user_id)  # Отримати об'єкт користувача з бази даних за id
        except User.DoesNotExist:
            # Обробка випадку, коли користувача не знайдено
            return HttpResponse('User not found', status=404)

        # Оновити поля користувача з даними з POST-запиту
        edited_user.name = request.POST.get("name", '')
        edited_user.language = request.POST.get("language", '')
        edited_user.course = request.POST.get("course", '')
        edited_user.grade = request.POST.get("grade", '')

        edited_user.save()  # Зберегти зміни

        return redirect('/show_base_elements')
