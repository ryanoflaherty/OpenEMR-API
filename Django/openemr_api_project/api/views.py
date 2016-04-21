from django.contrib.auth.models import User
from django.contrib.auth import login as login_user, logout as logout_user
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from forms import LoginForm, CrispyPasswordChangeForm, UserCreateForm, UserUpdateForm
from models import PatientData, MedicalHistory, Forms, HistoryData, Metadata, FormVitals, FormRos, FormReviewofs, FormEncounter
from rest_framework import viewsets, status
from serializers import UserSerializer, PatientDataSerializer, MetadataSerializer, HistoryDataSerializer
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
from django.utils import timezone
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.http import HttpResponse
import datetime


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

sys_messages = {
	'created': 'The user was successfully created',
	'deactivated': 'The user was successfully deactivated',
	'activated': 'The user was successfully activated',
}


# Token (With Expiration)
##########################################################
class ObtainExpiringAuthToken(ObtainAuthToken):
	def post(self, request):
		serializer = self.serializer_class(data=request.data)
		if serializer.is_valid():
			token, created = Token.objects.get_or_create(user=serializer.validated_data['user'])

			utc_now = timezone.now()
			if not created and token.created < utc_now - datetime.timedelta(days=2):
				token.delete()
				token = Token.objects.create(user=serializer.object['user'])
				token.created = datetime.datetime.utcnow()
				token.save()

			return Response({'token': token.key})

		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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

	# TODO if there is time, create a class/build angular to update these metrics

	# Get general metrics (Historical Data)
	# Most popular area (presence), duration of visits, internet, new users/user count

	internet_status = 0.0
	count = 0
	duration = timezone.timedelta(0, 0)

	hist_meta = Metadata.objects.all()
	records_created = hist_meta.count()
	if records_created:
		for meta in hist_meta:
			internet_status += int(meta.internet)
			if meta.duration:
				duration += meta.duration
			count += 1

		avg_internet = (internet_status / count)
		internet_status = (((avg_internet - 1) / 2) * 100)
		duration = (duration / count)
		# Scrub microseconds off
		duration = duration - timezone.timedelta(microseconds=duration.microseconds)

	active_users = User.objects.all().count()

	hist_stats_dict = {
		'records_created': records_created,
		'internet_status': "%.2f%% Health" % internet_status,
		'active_users': active_users,
		'duration': duration,
	}

	# Daily metrics
	# New users, records created, new patients, active users today, internet status, duration
	internet_status = 0.0
	count = 0
	duration = timezone.timedelta(0, 0)

	daily_meta = Metadata.objects.filter(date__lte=timezone.now(), date__gt=timezone.now()-timezone.timedelta(days=1))
	records_created = daily_meta.count()
	if records_created:
		for meta in daily_meta:
			internet_status += int(meta.internet)
			duration += meta.duration
			count += 1

		avg_internet = (internet_status/count)
		internet_status = (((avg_internet-1)/2) * 100)
		duration = (duration/count)
		# Scrub microseconds off
		duration = duration - timezone.timedelta(microseconds=duration.microseconds)

	active_users = User.objects.filter(last_login__lte=timezone.now(), last_login__gt=timezone.now()-timezone.timedelta(days=1)).count()

	daily_stats_dict = {
		'records_created': records_created,
		'internet_status': "%.2f%% Health" % internet_status,
		'active_users': active_users,
		'duration': duration,
	}

	# TODO Region based metrics

	return render(request, template_name, {'daily_stats': daily_stats_dict, 'hist_stats': hist_stats_dict})


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
	template_name = templates['users']
	users = User.objects.all()
	args = {
		'users': users,
	}
	if 'message' in request.GET:
		args['message'] = sys_messages[request.GET['message']]

	return render(request, template_name, args)


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
		return redirect('/users/overview')


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
	return redirect('/users/overview?message=deactivated')


class ActivateUser(LoginRequiredMixin, StaffuserRequiredMixin, TemplateView):
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
			user.is_active = True
			try:
				user.save()
				return redirect('/accounts/activate/done/')
			except ValidationError as e:
				error.append(e)
				return render(request, self.template_name, {'errors': error})

		else:
			error.append("No username found in request.")
			return render(request, self.template_name, {'error': error})


@staff_member_required(login_url='/unauthorized/', redirect_field_name='/accounts/login')
@login_required()
def activate_user_done(request=None):
	return redirect('/users/overview?message=activated')


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
		if form.form_name.title() == str("Vitals").title():
			visits[dict[str(form.encounter)]]["glucose"] = form.form_vitals.glucose
			visits[dict[str(form.encounter)]]["pulse"] = form.form_vitals.pulse
			visits[dict[str(form.encounter)]]["bps"] = form.form_vitals.bps
			visits[dict[str(form.encounter)]]["bpd"] = form.form_vitals.bpd
			visits[dict[str(form.encounter)]]["height"] = form.form_vitals.height
			visits[dict[str(form.encounter)]]["weight"] = form.form_vitals.weight
			visits[dict[str(form.encounter)]]["bmi"] = form.form_vitals.bmi
		if form.form_name.title() == str("Review Of Systems Checks").title():
			visits[dict[str(form.encounter)]]['dry_mouth'] = form.form_reviewofs.dry_mouth
			visits[dict[str(form.encounter)]]['high_blood_pressure'] = form.form_reviewofs.high_blood_pressure
		if form.form_name.title() == str("Review Of Systems").title():
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

	# Step 1 Get Metadata and Validate PatientData
	# Read in meta data for preprocessing, store data for use later in analytics
	# Check metadata for info about the patient
	if 'metadata' in request.data:			# TODO Make a Metadata class
		meta = request.data['metadata']		# if there is metadata, get it

		if meta['patient_exists'].title() == "No":					# Check to see if the patient exists based on meta
			# TODO create a function that makes sure that this is a
			# new patient even though it was specified
			new_patient = request.data['patient_data']				# Get new patient from the POST if it doesn't exist
			serializer = PatientDataSerializer(data=new_patient)	# Serialize POSTed data

			if serializer.is_valid():								# If the data is valid
				med_his = serializer.save()									# Create a new patient data instance
				pid = med_his.pid
			else:
				return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

		else:															# If patient exists, retrieve object from DB
			existing_patient = request.data['patient_data']['pubpid']
			med_his = MedicalHistory.objects.get(patient_data__pubpid=int(existing_patient))
			pid = med_his.pid

		# After getting/creating patient, save the meta data
		meta['pubpid'] = PatientData.objects.get(pid=pid)
		serializer = MetadataSerializer(data=meta)
		if serializer.is_valid():
			serializer.save()
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	# TODO If meta not provided at all, check to see if the patient exists. As of now, it is a REQUIRED field.

	# Step 2 - Parse POST to get HistoryData attributes
	# Parse history_data key, pass it to the HistoryDataSerializer

	history_data = request.data['history_data']
	history_data['pid'] = int(pid)
	serializer = HistoryDataSerializer(data=history_data)
	if serializer.is_valid():
		serializer.save()
	else:
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	# Step 3 - Parse POST to get Vists attributes
	# Parse the visit key

	visit = request.data['visit']

	user = visit['user']
	# Optional Date
	if 'date' in visit:
		date = visit['date']
	else:
		date = timezone.now()
	glucose = visit['glucose']
	pulse = visit['pulse']
	bps = visit['bps']
	bpd = visit['bpd']
	height = visit['height']
	weight = visit['weight']
	bmi = visit['bmi']
	dry_mouth = visit['dry_mouth']
	high_blood_pressure = visit['high_blood_pressure']
	n_numbness = visit['n_numbness']
	n_weakness = visit['n_weakness']
	p = visit['p']
	diabetes = visit['diabetes']

	# Note - Due to the fact that OpenEMR has a row in forms for every encounter, vitals, ros, review_ofs,
	# we need to create 6 different objects.  Next we create an object for all of the information
	# we get from the API.  Serializers are inefficient as well, data validation is handled by the model as
	# of right now.

	# TODO Make a validation class for Forms and derivatives

	# Get latest encounter
	latest_form = Forms.objects.latest('id')
	encounter = latest_form.encounter + 1

	# Create Form + Encounter
	form_e = Forms.objects.create(
		date=date,
		pid=pid,
		deleted=0,
		med_his=med_his,
		encounter=encounter,
		form_name="New Patient Encounter"
	)
	form_encounter = FormEncounter.objects.create(
		id = form_e,
		pid=form_e.pid,
		date=form_e.date,
		encounter=encounter,
	)

	# Create Form + Vitals Objects
	form_v = Forms.objects.create(
		date=date,
		pid=pid,
		deleted=0,
		med_his=med_his,
		encounter=encounter,
		form_name="Vitals"
	)
	form_vitals = FormVitals.objects.create(
		id=form_v,
		pid=form_v.pid,
		date=form_v.date,
		user=user,
		pulse=pulse,
		bps=bps,
		bpd=bpd,
		height=height,
		weight=weight,
		bmi=bmi,
		glucose=glucose
	)

	# Create Form + Ros
	form_r1 = Forms.objects.create(
		date=date,
		pid=pid,
		deleted=0,
		med_his=med_his,
		encounter=encounter,
		form_name="Review of Systems"
	)
	form_ros = FormRos(
		id=form_r1,
		date=form_r1.date,
		pid=form_r1.pid,
		p=p,
		n_numbness=n_numbness,
		n_weakness=n_weakness,
		diabetes=diabetes
	)

	# Create Form + Reviewofs
	form_r2 = Forms.objects.create(
		date=date,
		pid=pid,
		deleted=0,
		med_his=med_his,
		encounter=encounter,
		form_name="Review of Systems Checks"
	)
	form_reviewofs = FormReviewofs(
		id=form_r2,
		pid=form_r2.pid,
		date=form_r2.date,
		dry_mouth=dry_mouth,
		high_blood_pressure=high_blood_pressure,
	)

	# TODO If the visit does not successfully happen, send back a 400 Error

	# Let the user know the POST was successful
	if request.method == 'POST':
		return Response(status=status.HTTP_201_CREATED)


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


class MetadataView(generics.ListAPIView, generics.UpdateAPIView, generics.CreateAPIView):
	"""
	This view allow the user to view and modify MedicalHistory records.
	"""
	queryset = Metadata.objects.all()
	serializer_class = MetadataSerializer


class UserViewSet(viewsets.ModelViewSet):
	"""
	This view allow the user to view and modify users.
	"""
	queryset = User.objects.all()
	serializer_class = UserSerializer


"""
dict = {
		'meta': {
			'latitude': True,
			'longitude': True,
			'datetime': True,
			'duration': True, # length of visit, timestamp.end - timestamp.start
			'user': True, # who performed the test (useful because I can compare to the token to avoid fraud)
			'patient_exists': True, # Search was successful, patient is in the DB
			'internet': True, # Tuple, rank the internet connection
		},
		'patient_data': {
		},
		'visit': {
			"weight": True,
			"bpd": True,
			"dry_mouth": True,
			"bmi": True,
			"high_blood_pressure": True,
			"height": True,
			"bps": True,
			"pulse": True,
			"glucose": null,
		}
	}


cURL Testing

# Get Token
curl -H "Content-Type: application/json" -X POST -d '{"username":"nmorrisn","password":"seniordesign15"}' localhost:8000/api/token/

# GET patient data
curl -X GET "localhost:8000/api/records/patient-data?pubpid=28005573" -H "Authorization: Token 22f0fbbbe579ecaa4acc19b8011931aabae8fe0a"

# GET visits
curl -X GET "http://http-env.us-east-1.elasticbeanstalk.com/api/records/28005573/visits" -H "Authorization: Token b7b1b9eb162121622e50231e3be5ad01b81f7ce9"

# POST visit
curl -H "Authorization: Token b7b1b9eb162121622e50231e3be5ad01b81f7ce9" -X POST -d '{"pubpid": "28005573", "gov_id": "12345678", "date": "2016-04-11T20:35:25Z", "fname": "Ryan", "lname": "O'Flaherty", "mname": "A", "dob": "1994-11-19", "sex": "Male", "status": "single", "email": "ryflare@bu.edu", "address": "316 St. Paul Street", "postal_code": "02446", "city": "Brookline", "state": "MA", "country_code": "USA", "phone_contact": "","phone_cell": "845-258-0884"}' http://http-env.us-east-1.elasticbeanstalk.com/api/records/


curl -H "Authorization: Token b7b1b9eb162121622e50231e3be5ad01b81f7ce9" -X POST -d '{"pubpid": "28005573",
"gov_id": "12345678",
"date": "2016-04-11T20:35:25Z",
"fname": "Ryan",
"lname": "O'Flaherty",
"mname": "A",
"dob": "1994-11-19",
"sex": "Male",
"status": "single",
"email": "ryflare@bu.edu",
"address": "316 St. Paul Street",
"postal_code": "02446",
"city": "Brookline",
"state": "MA",
"country_code": "USA",
"phone_contact": "",
"phone_cell": "845-258-0884"}' http://http-env.us-east-1.elasticbeanstalk.com/api/records/
"""