# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User


# # Create your forms here.

# class NewUserForm(UserCreationForm):
# 	class Meta:
# 		model = User
# 		fields = ("username", "password1", "password2")

# 	def save(self, commit=True):
# 		user = super(NewUserForm, self).save(commit=False)
# 		if commit:
# 			user.save()
# 		return user
