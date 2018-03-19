from django.conf.urls import url

from app.api.reader.reader_login import ReaderLogin
from app.api.reader.reader_logout import ReaderLogout
from app.api.reader.reader_signup import ReaderSignup

urlpatterns = [
	url(r'^signup/$', ReaderSignup.as_view(), name="reader_registration"),
	url(r'^login/$', ReaderLogin.as_view(), name="reader_login"),
	url(r'^logout/$', ReaderLogout.as_view(), name="reader_logout"),

]
