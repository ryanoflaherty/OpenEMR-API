from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as login_user, logout as logout_user
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.admin.views.decorators import staff_member_required
from forms import LoginForm, CrispyPasswordChangeForm, UserCreateForm, UserUpdateForm
from models import PatientData, MedicalHistory, Forms, HistoryData, Visit
from rest_framework import viewsets
from serializers import UserSerializer, PatientDataSerializer, ListMedicalHistorySerializer, CreateUpdateMedicalHistorySerializer, FormsSerializer, HistoryDataSerializer, VisitSerializer
from django.shortcuts import render, redirect
from rest_framework import filters, generics
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response
from django.core.cache import cache
from django.contrib.auth import update_session_auth_hash
from django.views.generic.base import TemplateView
from braces.views import LoginRequiredMixin, StaffuserRequiredMixin
from django.core.exceptions import ValidationError


# Templates
##########################################################
templates = {
	'home': 'sb-admin-2/index.html',
	'help': 'sb-admin-2/help.html',
	'about': 'sb-admin-2/about.html',
	'login': 'sb-admin-2/login.html',
	'logout': 'sb-admin-2/logout.html',
	'analytics': 'sb-admin-2/analytics.html',
	'dashboard': 'sb-admin-2/dashboard.html',
	'lack_permissions': 'sb-admin-2/lack_permissions.html',
	'manage_user': 'sb-admin-2/manage_selected_user.html',
	'users': 'sb-admin-2/users.html',
	'password_change_form': 'sb-admin-2/password_change_form.html',
	'password_change_done': 'sb-admin-2/password_change_done.html',
	'register_user': 'sb-admin-2/registration_form.html',
	'registration_complete': 'sb-admin-2/registration_complete.html',
	'delete': 'sb-admin-2/delete.html',
	'user_deleted': 'sb-admin-2/user_deleted.html',
}


# Public Views (Anyone can view)
##########################################################
def index_guest(request):
	"""
	Landing page for unauthorized guests.
	"""
	template_name = templates['home']
	return render(request, template_name)


def help(request):
	"""
	Help page.
	"""
	template_name = templates['help']
	return render(request, template_name)


def about(request):
	"""
	About page.
	"""
	template_name = templates['about']
	return render(request, template_name)


def unauthorized(request=None):
	"""
	Alert user that they lack the appropriate permissions.
	"""
	template_name = templates['lack_permissions']
	return render(request, template_name)


class Login(TemplateView):
	"""
	Template view that handles GET and POST requests to log a user in.  This class does not require authentication to
	access.

	get(): Returns the login form to the user if they aren't signed in. Otherwise they are redirected to the Dashboard.
	post(): Validates user input against LoginForm().  If there are no errors, log the user in.  Otherwise return the
			form back to the user with validation errors highlighted.
	"""
	template_name = templates['login']

	def get(self, request, *args, **kwargs):
		if not request.user.is_authenticated():
			login_form = LoginForm()
			return render(request, self.template_name, {'login_form': login_form})
		else:
			return redirect('index')

	def post(self, request):
		form = LoginForm(None, request.POST or None)
		if form.is_valid():
			login_user(request, form.get_user())
			return redirect('index', permanent=True)
		else:
			return render(request, self.template_name, {'login_form': form})


# Views available to any logged in user
##########################################################
@login_required(login_url='/remotehcs', redirect_field_name='')
def index(request):
	"""
	This view returns the dashboard to an authenticated user.  The @login_required decorator will send visitors to the
	visitor homepage
	"""
	template_name = templates['dashboard']
	return render(request, template_name)


@login_required()
def analytics(request):
	"""
	Analytics page with useful data and statistics for the users.
	"""
	template_name = templates['analytics']
	return render(request, template_name)


@login_required()
def logout(request):
	"""
	Logout the active user.
	"""
	template_name = templates['logout']
	logout_user(request)
	return render(request, template_name)


class PasswordChange(LoginRequiredMixin, TemplateView):
	"""
	This view allows users to change their password after they provide their old password.
	"""
	template_name = templates['password_change_form']

	def get(self, request, *args, **kwargs):
		password_change_form = CrispyPasswordChangeForm(request.user)
		return render(request, self.template_name, {'password_change_form': password_change_form})

	def post(self, request):
		form = CrispyPasswordChangeForm(user=request.user, data=request.POST)
		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			return redirect('/accounts/password_reset/done/')
		else:
			return render(request, self.template_name, {'password_change_form': form})


@login_required()
def password_change_done(request):
	"""
	This view lets the user know their password was successfully changed.
	"""
	return render(request, templates['password_change_done'])


# Admin Views
##########################################################
class UserManagement(LoginRequiredMixin, StaffuserRequiredMixin, TemplateView):
	"""
	This view is exclusive to admin users and allows them to edit user profiles.
	"""
	template_name = templates['manage_user']
	permission_required = 'request.user.is_staff'
	raise_exception = True

	def get(self, request, *args, **kwargs):
		if 'username' in request.GET:
			username = request.GET['username']
			user = User.objects.get(username=username)
			form = UserUpdateForm()
			return render(request, self.template_name, {'user_update_form': form, 'selected_user': user,})
		else:
			return render(request, templates['users'], args)

	def post(self, request):
		form = UserUpdateForm()
		if form.is_valid():
			form.save()
			request.session["temp_user"] = {
				'username': request.POST["username"],
				'new': False,
			}
			return redirect('/accounts/register/done/')
		else:
			return render(request, self.template_name, {'user_update_form': form})


@staff_member_required(login_url='/unauthorized/', redirect_field_name='/accounts/login')
@login_required()
def user_overview(request):
	"""
	Return a table of users to the admin. Only admin can see this page. Other authenticated users are sent to an error
	page.
	"""
	users = User.objects.all()
	args = {
		'users': users,
	}
	if 'message' in request.GET:
		args = {
			'message': 'The user was successfully deleted!'
		}
	return render(request, 'sb-admin-2/users.html', args)


class CreateUser(LoginRequiredMixin, StaffuserRequiredMixin, TemplateView):
	"""
	This view allows an admin to provision a new account.
	"""
	template_name = templates['register_user']
	permission_required = 'request.user.is_staff'
	raise_exception = True

	def get(self, request, *args, **kwargs):
		form = UserCreateForm()
		return render(request, self.template_name, {'user_create_form': form})

	def post(self, request):
		form = UserCreateForm(request.POST)
		if form.is_valid():
			form.save()
			request.session["temp_user"] = {
				'username': request.POST["username"],
				'new': True,
			}
			return redirect('/accounts/register/done/')
		else:
			return render(request, self.template_name, {'user_create_form': form})


@staff_member_required(login_url='/unauthorized/', redirect_field_name='/accounts/login')
@login_required()
def user_create_done(request):
	"""
	This view provides the admin with a success screen when they update/create a user.
	"""
	new_user = request.session["temp_user"]["username"]
	is_new = request.session["temp_user"]["new"]

	if new_user:
		request.session["temp_user"] = ""
		user = User.objects.get(username=new_user)
		return render(request, templates['registration_complete'], {'new_user': user, 'is_new': is_new})
	else:
		return redirect('/users/overview/')


class DeleteUser(LoginRequiredMixin, StaffuserRequiredMixin, TemplateView):
	"""
	This view allows an admin to delete a user account (make inactive, as is Django best practice).
	"""
	template_name = templates['users']
	permission_required = 'request.user.is_staff'
	raise_exception = True

	def get(self, request, *args, **kwargs):
		error = []

		if 'username' in request.GET:
			username = request.GET['username']
			user = User.objects.get(username=username)
			user.is_active = False
			try:
				user.save()
				return redirect('/accounts/delete/done/')
			except ValidationError as e:
				error.append(e)
				return render(request, self.template_name, {'errors': error})

		else:
			error.append("No username found in request.")
			return render(request, self.template_name, {'error': error})


@staff_member_required(login_url='/unauthorized/', redirect_field_name='/accounts/login')
@login_required()
def delete_user_done(request=None):
	message = "success"
	return redirect('/users/overview?message=' + str(message))


# API Views
##########################################################
@api_view(['GET'])
def api_root(request, format=None):
	"""
	This view constructs the API root for browsable API.
	"""
	return Response({
		'records/': reverse('medical-record-create-update', request=request, format=format),
		'records/patient-data': reverse('patient-data-list', request=request, format=format),
		'records/{pubpid}/visits': reverse('visits-list', request=request, format=format, kwargs={'pubpid': '28005573'}),
		#'users': reverse('users', request=request, format=format),
	})


class VisitsHistoryList(generics.ListAPIView):
	"""
	This view allow the user to use .list() or .retrieve() for patient visits data based on the users pubpid.
	"""
	serializer_class = ListMedicalHistorySerializer

	def get_queryset(self):
		public_pid = self.kwargs['pubpid']
		return MedicalHistory.objects.filter(patient_data__pubpid=public_pid)
	"""
	def get_queryset(self):
		public_pid = self.kwargs['pubpid']
		mh_cache_query = str("MH-" + public_pid)
		cached = cache.get(mh_cache_query)
		if cached:
			return cached
		else:
			queryset = MedicalHistory.objects.filter(patient_data__pubpid=public_pid)
			cache.set(mh_cache_query, queryset, 3600)
			return queryset
	"""



@api_view(['GET'])
def list_visits(request, pubpid, format=None):
	"""
	Function based view to return flat representation of patient visits.
	:param request: HTTP Request
	:param pubpid: Public patient id, used to perform queries
	:param format: .json or .api
	:return: dict of patients visit history
	"""

	med_his = cache.get(str("MH-" + pubpid))

	if med_his:
		history_data = HistoryData.objects.filter(pid=med_his.pid).latest('date')
		#forms = Forms.objects.prefetch_related('form_reviewofs', 'form_ros', 'form_vitals').filter(pid=med_his.pid)
		forms = Forms.objects.filter(pid=med_his.pid)
	else:
		med_his = MedicalHistory.objects.get(patient_data__pubpid=pubpid)
		history_data = HistoryData.objects.filter(pid=med_his.pid).latest('date')
		forms = Forms.objects.filter(pid=med_his.pid)

	# Create dictionary to serialize
	visits = []
	dict = {}
	for form in forms:
		if str(form.encounter) not in dict:
			dict[str(form.encounter)] = len(visits)
			visits.append({"date": form.date, "user": form.user})
		if form.form_name == "Vitals":
			visits[dict[str(form.encounter)]]["glucose"] = form.form_vitals.glucose
			visits[dict[str(form.encounter)]]["pulse"] = form.form_vitals.pulse
			visits[dict[str(form.encounter)]]["bps"] = form.form_vitals.bps
			visits[dict[str(form.encounter)]]["bpd"] = form.form_vitals.bpd
			visits[dict[str(form.encounter)]]["height"] = form.form_vitals.height
			visits[dict[str(form.encounter)]]["weight"] = form.form_vitals.weight
			visits[dict[str(form.encounter)]]["bmi"] = form.form_vitals.bmi
		if form.form_name == "Review of Systems Checks":
			visits[dict[str(form.encounter)]]['dry_mouth'] = form.form_reviewofs.dry_mouth
			visits[dict[str(form.encounter)]]['high_blood_pressure'] = form.form_reviewofs.high_blood_pressure
		if form.form_name == "Review Of Systems":
			visits[dict[str(form.encounter)]]['numbness'] = form.form_ros.n_numbness
			visits[dict[str(form.encounter)]]['pregnant'] = form.form_ros.p
			visits[dict[str(form.encounter)]]['dizziness'] = form.form_ros.n_weakness
			visits[dict[str(form.encounter)]]['diabetes'] = form.form_ros.diabetes

	if request.method == 'GET':
		history_data_serializer = HistoryDataSerializer(history_data)

		serializer = {
			'history_data': history_data_serializer.data,
			'visits': visits,
		}
		return Response(serializer)


@api_view(['POST'])
def create_visit(request, format=None):
	"""
	This view allow the user to view and modify MedicalHistory records.
	:param request:
	:param format:
	:return:
	"""

	if request.method == 'POST':
		print(request.data)
		return Response({'message': 'success', 'data': request.data})


class PatientDataList(generics.ListAPIView):
	"""
	This view allow the user to use .list() or .retrieve() for patient data, as well as search by all fields.

	Since this is the first class accessed, cache Visits when accessed
	"""
	serializer_class = PatientDataSerializer
	filter_backends = (filters.DjangoFilterBackend,)
	filter_fields = ('pid', 'pubpid', 'ss', 'fname', 'lname', 'mname', 'dob', 'sex', 'status', 'email', 'street', 'postal_code', 'city', 'state', 'country_code')

	def get_queryset(self):
		pubpid = self.request.query_params.get('pubpid', None)
		queryset = PatientData.objects.all()

		if pubpid is not None:
			queryset = queryset.filter(pubpid=pubpid)
			pd_cache_query = str("PD-" + pubpid)
			pd_cached = cache.get(pd_cache_query)

			if not pd_cached:
				cache.set(pd_cache_query, queryset, 3600)
				for q in queryset:
					related = MedicalHistory.objects.filter(pid=q.pid.pid)
					cache.set('MH-' + str(pubpid), related[0])

		return queryset


class CreateUpdateMedicalRecord(generics.CreateAPIView, generics.UpdateAPIView):
	"""
	This view allow the user to view and modify MedicalHistory records.
	"""
	queryset = MedicalHistory.objects.all()
	serializer_class = CreateUpdateMedicalHistorySerializer


class UserViewSet(viewsets.ModelViewSet):
	"""
	This view allow the user to view and modify users.
	"""
	queryset = User.objects.all()
	serializer_class = UserSerializer


class FormsList(generics.ListAPIView):
	queryset = Forms.objects.all()
	serializer_class = FormsSerializer