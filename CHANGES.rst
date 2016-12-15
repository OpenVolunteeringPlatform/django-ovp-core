===========
Change log
===========

v0.1.0
-----------
* Start project
* Update README

v0.1.1
-----------
* Add codeship and codecov badge
* Add pypi badge
* Add OvpSchemaGenerator, which fixes multiple methods on @list_route or @detail_route

v0.1.2
-----------
* Fix schema exception

v0.1.3
-----------
* Add address model
* Add skills and causes

v0.1.4
----------
* Create GoogleAddressSerializer

v0.1.5
-----------
* Add address validator

v0.1.6
-----------
* Move BaseMail from ovp-users to ovp-core
* Introduce empty base email
* Improve address tests and coverage
* Alter get_city_state() order

v1.0.0
-----------
* Add tests for email module(BaseMail and EmailThread classes)
* Add test for OVPSchemaGenerator
* Add test for address_validate 

v1.0.1
-----------
* Replace distutils with setuptools

v1.0.2
-----------
* Add .egg-info to .gitignore

v1.0.3
-----------
* Remove OVPSchemaGenerator
* Upgrade drf to 3.5.3

v1.0.4
-----------
* Remove unecessary imports from test_execution
* Only read DEFAULT_SEND_EMAIL if .async_mail is None(not None and False as before)

v1.0.5
-----------
* Add startup route returning skills and causes
* Add contact form route

v1.0.6
-----------
* Change default maps api language to en-US
* Create OVP_CORE.MAPS_API_LANGUAGE setting

v1.0.7
-----------
* Fix tests broken by last release

v1.0.8
-----------
* Create GoogleAddressCityStateSerializer

v1.0.9
-----------
* Add 'phone' field to contact view

v1.0.10
-----------
* Set up internationalization on startup route and add pt_BR locale

v1.0.11
-----------
* Create GoogleAddressLatLngSerializer

v1.0.12
-----------
* Create EmptySerializer

v1.0.13[request]
-----------
* Remove city_state() sublocality assertion
