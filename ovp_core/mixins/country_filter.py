class CountryFilterMixin():
  def filter_by_country(self, request, query_set, address_param):
    if request.user.is_superuser:
      return query_set

    user_groups = request.user.groups.all()
    if len(user_groups) == 0:
      return query_set.filter(owner=user)

    user_contries = []
    for group in user_groups:
      if group.name.startswith('mng-'):
        user_contries.append(group.name.split('-')[1].upper())

    if len(user_contries) == 0:
      return query_set.filter(owner=user)

    filter_params = {}

    filter_params[address_param + '__address_components__short_name__in'] = user_contries
    filter_params[address_param + '__address_components__types__name__exact'] = 'country'

    return query_set.filter(**filter_params)
